from src.functions import text_node_to_html_node, text_to_textnodes
from src.leafnode import LeafNode
from src.parentnode import ParentNode
from src.block_functions import BlockType, markdown_to_blocks, block_to_block_type


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        if not block:
            continue
        block_type = block_to_block_type(block)
        children.append(block_to_node(block, block_type))

    return ParentNode("div", children)


def text_to_children(text: str):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children


def block_to_node(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            # join lines of the paragraph with spaces
            paragraph = " ".join(block.split("\n"))
            return ParentNode("p", text_to_children(paragraph))

        case BlockType.HEADING:
            # count leading #'s for level
            level = 0
            for ch in block:
                if ch == "#":
                    level += 1
                else:
                    break
            # skip "#"*level + following space
            text = block[level + 1 :]
            return ParentNode(f"h{level}", text_to_children(text))
        case BlockType.CODE:
            lines = block.split("\n")
            # drop first and last line (the ``` fences)
            inner_lines = lines[1:-1]
            inner = "\n".join(inner_lines) + "\n"  # add final newline
            code_leaf = LeafNode("code", inner)
            return ParentNode("pre", [code_leaf])
        case BlockType.QUOTE:
            # strip "> " from each line, join with spaces
            lines = []
            for line in block.split("\n"):
                # remove leading '>' and space
                stripped = line.lstrip(">").strip()
                lines.append(stripped)
            text = " ".join(lines)
            return ParentNode("blockquote", text_to_children(text))

        case BlockType.ORDERED_LIST:
            items = []
            for line in block.split("\n"):
                # strip leading "1. ", "2. ", etc
                _, text = line.split(". ", 1)
                items.append(ParentNode("li", text_to_children(text)))
            return ParentNode("ol", items)

        case BlockType.UNORDERED_LIST:
            items = []
            for line in block.split("\n"):
                # strip leading "- "
                text = line[2:]
                items.append(ParentNode("li", text_to_children(text)))
            return ParentNode("ul", items)

    # should never get here if all types covered
    raise ValueError(f"unsupported block type: {block_type}")
