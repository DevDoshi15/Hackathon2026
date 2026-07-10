import os
from pathlib import Path
from typing import Any

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from hackathon2026.rag.retrieval import hybrid_retrieve
from hackathon2026.utils.env import load_project_env


class RerankedChunk(BaseModel):
    chunk_id: str
    relevance_score: int = Field(..., ge=0, le=100)
    reason: str


class RerankedChunks(BaseModel):
    chunks: list[RerankedChunk]


class RagAnswer(BaseModel):
    answer: str
    citations: list[str]


class RagAnswerService:
    def answer(self, question: str) -> dict[str, Any]:
        load_project_env()
        vector_store_id = os.getenv("OPENAI_VECTOR_STORE_ID", "")
        manifest_path = Path(os.getenv("KB_CHUNK_MANIFEST", "hackathon2026/data/rag/chunks.jsonl"))

        if not vector_store_id:
            return {
                "answer": "RAG is not configured yet. Run the ingest script and set OPENAI_VECTOR_STORE_ID.",
                "citations": [],
                "chunks": [],
                "configured": False,
            }

        chunks = hybrid_retrieve(
            question=question,
            vector_store_id=vector_store_id,
            manifest_path=manifest_path,
        )
        if not chunks:
            return {
                "answer": "I could not find relevant KB context for this question.",
                "citations": [],
                "chunks": [],
                "configured": True,
            }

        reranked_chunks = self._rerank(question, chunks)
        selected_chunks = reranked_chunks[:5]
        answer = self._generate_answer(question, selected_chunks)

        return {
            "answer": answer.answer,
            "citations": answer.citations,
            "chunks": [_citation_payload(chunk) for chunk in selected_chunks],
            "configured": True,
        }

    def _rerank(self, question: str, chunks: list[dict[str, Any]]) -> list[dict[str, Any]]:
        if not chunks:
            return []

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Rerank knowledge chunks for answering the question. Score each chunk from 0 to 100. Prefer exact API, field, table, enum, and workflow evidence.",
                ),
                ("human", "Question:\n{question}\n\nChunks:\n{chunks}"),
            ]
        )
        model = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
        chain = prompt | model.with_structured_output(RerankedChunks)
        rerank_result = chain.invoke({"question": question, "chunks": _format_chunks_for_prompt(chunks)})
        scores = {chunk.chunk_id: chunk.relevance_score for chunk in rerank_result.chunks}

        return sorted(
            chunks,
            key=lambda chunk: scores.get(_chunk_id(chunk), 0),
            reverse=True,
        )

    def _generate_answer(self, question: str, chunks: list[dict[str, Any]]) -> RagAnswer:
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "Answer using only the provided context. Include citations using the article title and URL. If the context does not answer the question, say what is missing.",
                ),
                ("human", "Question:\n{question}\n\nContext:\n{context}"),
            ]
        )
        model = ChatOpenAI(model="gpt-4.1-mini", temperature=0)
        chain = prompt | model.with_structured_output(RagAnswer)
        return chain.invoke({"question": question, "context": _format_chunks_for_prompt(chunks)})


def _format_chunks_for_prompt(chunks: list[dict[str, Any]]) -> str:
    formatted = []
    for index, chunk in enumerate(chunks, start=1):
        attributes = chunk.get("attributes") or {}
        formatted.append(
            "\n".join(
                [
                    f"[{index}] chunk_id: {_chunk_id(chunk)}",
                    f"title: {attributes.get('title', '')}",
                    f"url: {attributes.get('url', '')}",
                    f"section: {attributes.get('section', '')}",
                    f"content:\n{chunk.get('content', '')}",
                ]
            )
        )
    return "\n\n---\n\n".join(formatted)


def _chunk_id(chunk: dict[str, Any]) -> str:
    return str((chunk.get("attributes") or {}).get("chunk_id") or chunk.get("chunk_id") or "")


def _citation_payload(chunk: dict[str, Any]) -> dict[str, Any]:
    attributes = chunk.get("attributes") or {}
    return {
        "chunk_id": _chunk_id(chunk),
        "article_id": attributes.get("article_id", ""),
        "title": attributes.get("title", ""),
        "url": attributes.get("url", ""),
        "section": attributes.get("section", ""),
        "retrieval_sources": chunk.get("retrieval_sources", []),
    }


load_project_env()
rag_answer_service = RagAnswerService()
