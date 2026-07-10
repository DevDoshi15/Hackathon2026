import json
import os
import tempfile
from pathlib import Path
from typing import Iterable

from openai import OpenAI

from hackathon2026.rag.chunking import KnowledgeChunk
from hackathon2026.utils.env import load_project_env


def get_openai_client() -> OpenAI:
    load_project_env()
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not configured.")
    return OpenAI()


def create_vector_store(name: str) -> str:
    client = get_openai_client()
    vector_store = client.vector_stores.create(name=name)
    return vector_store.id


def upload_chunks_to_vector_store(
    chunks: Iterable[KnowledgeChunk],
    vector_store_id: str,
) -> list[dict]:
    client = get_openai_client()
    uploaded = []

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        for chunk in chunks:
            chunk_file = tmp_path / f"{_safe_filename(chunk.chunk_id)}.md"
            chunk_file.write_text(_format_chunk_file(chunk), encoding="utf-8")

            with chunk_file.open("rb") as file_handle:
                uploaded_file = client.files.create(file=file_handle, purpose="assistants")

            vector_file = client.vector_stores.files.create(
                vector_store_id=vector_store_id,
                file_id=uploaded_file.id,
                attributes=chunk.to_metadata(),
            )
            uploaded.append(
                {
                    "chunk_id": chunk.chunk_id,
                    "file_id": uploaded_file.id,
                    "vector_store_file_id": vector_file.id,
                    "status": getattr(vector_file, "status", None),
                }
            )

    return uploaded


def search_vector_store(vector_store_id: str, query: str, max_results: int = 12) -> list[dict]:
    client = get_openai_client()
    result = client.vector_stores.search(
        vector_store_id=vector_store_id,
        query=query,
        max_num_results=max_results,
    )
    return [_vector_result_to_dict(item) for item in getattr(result, "data", [])]


def write_manifest(chunks: Iterable[KnowledgeChunk], manifest_path: Path) -> None:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", encoding="utf-8") as file_handle:
        for chunk in chunks:
            file_handle.write(json.dumps(chunk.to_record(), ensure_ascii=False) + "\n")


def load_manifest(manifest_path: Path) -> list[dict]:
    if not manifest_path.exists():
        return []
    return [
        json.loads(line)
        for line in manifest_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _format_chunk_file(chunk: KnowledgeChunk) -> str:
    return (
        f"article_id: {chunk.article_id}\n"
        f"title: {chunk.title}\n"
        f"url: {chunk.url}\n"
        f"section: {chunk.section}\n"
        f"chunk_id: {chunk.chunk_id}\n"
        f"chunk_type: {chunk.chunk_type}\n\n"
        f"{chunk.content}\n"
    )


def _safe_filename(value: str) -> str:
    return "".join(character if character.isalnum() or character in "-_." else "_" for character in value)


def _vector_result_to_dict(item) -> dict:
    content_parts = getattr(item, "content", []) or []
    text = "\n".join(getattr(part, "text", "") for part in content_parts)

    return {
        "file_id": getattr(item, "file_id", ""),
        "filename": getattr(item, "filename", ""),
        "score": getattr(item, "score", 0.0),
        "content": text,
        "attributes": getattr(item, "attributes", {}) or {},
    }
