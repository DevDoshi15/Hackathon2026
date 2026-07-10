import re
from dataclasses import asdict, dataclass

from hackathon2026.rag.markdown_loader import KnowledgeArticle


@dataclass(frozen=True)
class KnowledgeChunk:
    chunk_id: str
    article_id: str
    title: str
    url: str
    section: str
    chunk_type: str
    content: str
    source_path: str

    def to_metadata(self) -> dict[str, str]:
        return {
            "chunk_id": self.chunk_id,
            "article_id": self.article_id,
            "title": self.title[:512],
            "url": self.url[:512],
            "section": self.section[:512],
            "chunk_type": self.chunk_type,
            "source_path": self.source_path[:512],
        }

    def to_record(self) -> dict:
        return asdict(self)


def chunk_articles(articles: list[KnowledgeArticle], max_chars: int = 1800) -> list[KnowledgeChunk]:
    chunks = []
    for article in articles:
        chunks.extend(chunk_article(article, max_chars=max_chars))
    return chunks


def chunk_article(article: KnowledgeArticle, max_chars: int = 1800) -> list[KnowledgeChunk]:
    blocks = _split_markdown_blocks(article.content)
    chunks = []
    current_section = article.title
    current_parts = []
    chunk_index = 1

    for block in blocks:
        block_text = block.strip()
        if not block_text:
            continue

        heading = _heading_text(block_text)
        if heading:
            if current_parts:
                chunks.append(_make_chunk(article, chunk_index, current_section, "text", current_parts))
                chunk_index += 1
                current_parts = []
            current_section = heading
            current_parts.append(block_text)
            continue

        if _is_table(block_text) or _is_code_fence(block_text):
            if current_parts:
                chunks.append(_make_chunk(article, chunk_index, current_section, "text", current_parts))
                chunk_index += 1
                current_parts = []
            chunks.append(_make_chunk(article, chunk_index, current_section, _block_type(block_text), [block_text]))
            chunk_index += 1
            continue

        proposed = "\n\n".join([*current_parts, block_text])
        if len(proposed) > max_chars and current_parts:
            chunks.append(_make_chunk(article, chunk_index, current_section, "text", current_parts))
            chunk_index += 1
            current_parts = [block_text]
        else:
            current_parts.append(block_text)

    if current_parts:
        chunks.append(_make_chunk(article, chunk_index, current_section, "text", current_parts))

    return chunks


def _split_markdown_blocks(text: str) -> list[str]:
    blocks = []
    current = []
    in_code_fence = False

    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code_fence = not in_code_fence
            current.append(line)
            continue

        if not in_code_fence and not line.strip():
            if current:
                blocks.append("\n".join(current))
                current = []
            continue

        current.append(line)

    if current:
        blocks.append("\n".join(current))
    return _merge_table_blocks(blocks)


def _merge_table_blocks(blocks: list[str]) -> list[str]:
    merged = []
    index = 0
    while index < len(blocks):
        block = blocks[index]
        if _is_table(block):
            table_parts = [block]
            index += 1
            while index < len(blocks) and _is_table(blocks[index]):
                table_parts.append(blocks[index])
                index += 1
            merged.append("\n".join(table_parts))
            continue
        merged.append(block)
        index += 1
    return merged


def _make_chunk(
    article: KnowledgeArticle,
    chunk_index: int,
    section: str,
    chunk_type: str,
    parts: list[str],
) -> KnowledgeChunk:
    return KnowledgeChunk(
        chunk_id=f"{article.article_id}:{chunk_index:04d}",
        article_id=article.article_id,
        title=article.title,
        url=article.url,
        section=section,
        chunk_type=chunk_type,
        content="\n\n".join(parts).strip(),
        source_path=article.source_path,
    )


def _heading_text(block: str) -> str:
    match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", block)
    return match.group(1).strip() if match else ""


def _is_table(block: str) -> bool:
    lines = [line.strip() for line in block.splitlines() if line.strip()]
    return len(lines) >= 2 and "|" in lines[0] and re.search(r"\|\s*:?-{3,}:?\s*\|", lines[1]) is not None


def _is_code_fence(block: str) -> bool:
    return block.strip().startswith("```")


def _block_type(block: str) -> str:
    if _is_table(block):
        return "table"
    if _is_code_fence(block):
        return "code"
    return "text"
