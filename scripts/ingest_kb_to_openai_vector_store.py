from argparse import ArgumentParser
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from hackathon2026.rag.chunking import chunk_articles
from hackathon2026.rag.markdown_loader import load_markdown_articles
from hackathon2026.rag.vector_store import (
    create_vector_store,
    upload_chunks_to_vector_store,
    write_manifest,
)


def main() -> None:
    parser = ArgumentParser(description="Ingest markdown KB articles into an OpenAI Vector Store.")
    parser.add_argument(
        "--source-dir",
        default="hackathon2026/data/KB Articles",
        help="Folder containing markdown KB articles.",
    )
    parser.add_argument(
        "--manifest",
        default="hackathon2026/data/rag/chunks.jsonl",
        help="Local chunk manifest used for keyword retrieval and citations.",
    )
    parser.add_argument(
        "--vector-store-name",
        default="hackathon2026-kb",
        help="Name for the OpenAI Vector Store.",
    )
    parser.add_argument(
        "--vector-store-id",
        default="",
        help="Existing OpenAI Vector Store id. If omitted, a new store is created.",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=1800,
        help="Approximate max characters per text chunk. Tables and code blocks stay intact.",
    )
    args = parser.parse_args()

    articles = load_markdown_articles(Path(args.source_dir))
    chunks = chunk_articles(articles, max_chars=args.max_chars)
    manifest_path = Path(args.manifest)
    write_manifest(chunks, manifest_path)

    vector_store_id = args.vector_store_id or create_vector_store(args.vector_store_name)
    uploaded = upload_chunks_to_vector_store(chunks, vector_store_id)

    print(f"Articles parsed: {len(articles)}")
    print(f"Chunks uploaded: {len(uploaded)}")
    print(f"Vector store id: {vector_store_id}")
    print(f"Manifest path: {manifest_path}")
    print("Add these to hackathon2026/.env:")
    print(f"OPENAI_VECTOR_STORE_ID={vector_store_id}")
    print(f"KB_CHUNK_MANIFEST={manifest_path.as_posix()}")


if __name__ == "__main__":
    main()
