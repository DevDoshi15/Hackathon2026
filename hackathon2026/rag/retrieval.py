import math
import re
from collections import Counter
from pathlib import Path
from typing import Any

from hackathon2026.rag.vector_store import load_manifest, search_vector_store


def hybrid_retrieve(
    question: str,
    vector_store_id: str,
    manifest_path: Path,
    vector_k: int = 12,
    keyword_k: int = 12,
    final_k: int = 10,
) -> list[dict[str, Any]]:
    vector_results = search_vector_store(vector_store_id, question, max_results=vector_k)
    keyword_results = keyword_search(question, manifest_path, top_k=keyword_k)
    return reciprocal_rank_fusion(vector_results, keyword_results, final_k=final_k)


def keyword_search(question: str, manifest_path: Path, top_k: int = 12) -> list[dict[str, Any]]:
    records = load_manifest(manifest_path)
    query_terms = _tokenize(question)
    if not query_terms:
        return []

    scored = []
    total_docs = len(records) or 1
    doc_frequency = Counter()
    tokenized_records = []

    for record in records:
        tokens = _tokenize(_record_search_text(record))
        tokenized_records.append((record, tokens))
        doc_frequency.update(set(tokens))

    for record, tokens in tokenized_records:
        if not tokens:
            continue
        token_counts = Counter(tokens)
        score = 0.0
        for term in query_terms:
            term_frequency = token_counts[term]
            if not term_frequency:
                continue
            inverse_doc_frequency = math.log((total_docs + 1) / (doc_frequency[term] + 1)) + 1
            score += term_frequency * inverse_doc_frequency
        if score:
            scored.append((_manifest_record_to_result(record, score), score))

    scored.sort(key=lambda item: item[1], reverse=True)
    return [item[0] for item in scored[:top_k]]


def reciprocal_rank_fusion(
    vector_results: list[dict[str, Any]],
    keyword_results: list[dict[str, Any]],
    final_k: int = 10,
    rank_constant: int = 60,
) -> list[dict[str, Any]]:
    fused: dict[str, dict[str, Any]] = {}

    for source_name, results in [("vector", vector_results), ("keyword", keyword_results)]:
        for rank, result in enumerate(results, start=1):
            chunk_id = _result_chunk_id(result)
            if not chunk_id:
                chunk_id = f"{source_name}:{rank}:{result.get('filename', '')}"
            if chunk_id not in fused:
                fused[chunk_id] = {**result, "chunk_id": chunk_id, "retrieval_sources": []}
            fused[chunk_id]["retrieval_sources"].append(source_name)
            fused[chunk_id]["rrf_score"] = fused[chunk_id].get("rrf_score", 0.0) + 1 / (rank_constant + rank)

    return sorted(fused.values(), key=lambda item: item["rrf_score"], reverse=True)[:final_k]


def _manifest_record_to_result(record: dict[str, Any], score: float) -> dict[str, Any]:
    attributes = {
        "chunk_id": record.get("chunk_id", ""),
        "article_id": record.get("article_id", ""),
        "title": record.get("title", ""),
        "url": record.get("url", ""),
        "section": record.get("section", ""),
        "chunk_type": record.get("chunk_type", ""),
        "source_path": record.get("source_path", ""),
    }
    return {
        "score": score,
        "content": record.get("content", ""),
        "attributes": attributes,
        "filename": f"{record.get('chunk_id', '')}.md",
    }


def _record_search_text(record: dict[str, Any]) -> str:
    return " ".join(
        [
            str(record.get("title", "")),
            str(record.get("section", "")),
            str(record.get("content", "")),
        ]
    )


def _result_chunk_id(result: dict[str, Any]) -> str:
    return str((result.get("attributes") or {}).get("chunk_id", ""))


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z0-9_]+", text.lower())
