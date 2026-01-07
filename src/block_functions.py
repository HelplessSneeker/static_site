from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    sanitized_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if not block:
            continue
        sanitized_blocks.append(block.strip())
    return sanitized_blocks


def block_to_block_type(markdown):
    if re.match(r"^\#{1,6} ", markdown):
        return BlockType.HEADING
    if re.match(r"^`{3}\n*\n[\s\S]*`{3}$", markdown):
        return BlockType.CODE
    if re.match(r"^> ", markdown):
        return BlockType.QUOTE
    if re.match(r"^\d.", markdown):
        return BlockType.ORDERED_LIST
    if re.match(r"^- ", markdown):
        return BlockType.UNORDERED_LIST
    return BlockType.PARAGRAPH
