from argparse import ArgumentParser
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from hackathon2026.rag import rag_answer_service


def main() -> None:
    parser = ArgumentParser(description="Ask a question against the KB RAG system.")
    parser.add_argument("question")
    args = parser.parse_args()

    result = rag_answer_service.answer(args.question)
    print(result["answer"])
    if result.get("citations"):
        print("\nCitations:")
        for citation in result["citations"]:
            print(f"- {citation}")


if __name__ == "__main__":
    main()
