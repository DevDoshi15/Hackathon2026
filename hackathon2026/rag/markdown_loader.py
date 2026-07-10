import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class KnowledgeArticle:
    article_id: str
    title: str
    url: str
    content: str
    source_path: str


def load_markdown_articles(source_dir: Path) -> list[KnowledgeArticle]:
    return [parse_markdown_article(path) for path in sorted(source_dir.glob("**/*.md"))]


def parse_markdown_article(path: Path) -> KnowledgeArticle:
    raw_text = path.read_text(encoding="utf-8")
    url = _extract_field(raw_text, "URL")
    # Not every corpus has an explicit ID header (e.g. Request-Response docs) - fall back
    # to the filename so chunk_ids (article_id:NNNN) stay unique instead of colliding.
    article_id = _extract_field(raw_text, "ID") or path.stem
    title = _extract_title(raw_text) or path.stem.replace("-", " ").title()
    content = _strip_metadata(raw_text).strip()

    return KnowledgeArticle(
        article_id=article_id,
        title=title,
        url=url,
        content=content,
        source_path=str(path),
    )


def _extract_field(text: str, field_name: str) -> str:
    match = re.search(rf"^\s*{field_name}\s*:\s*(.+?)\s*$", text, flags=re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip() if match else ""


def _extract_title(text: str) -> str:
    match = re.search(r"^\s*#\s+(.+?)\s*$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def _strip_metadata(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if re.match(r"^\s*(URL|ID)\s*:", line, flags=re.IGNORECASE):
            continue
        lines.append(line)
    return "\n".join(lines)
