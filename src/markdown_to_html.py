import re
from src.functions import text_node_to_html_node, text_to_textnodes
from src.leafnode import LeafNode
from src.parentnode import ParentNode
from src.block_functions import BlockType, markdown_to_blocks, block_to_block_type


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    leafnodes = []

    for block in blocks:
        if not block:
            continue
        type = block_to_block_type(block)
        leafnodes += block_to_nodes(block, type)

    return ParentNode("div", leafnodes)


def block_to_nodes(block, type):
    children = []
    match type:
        case BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(block.replace("\n", " "))
            for node in text_nodes:
                children.append(text_node_to_html_node(node))
            return [ParentNode("p", children)]
        case BlockType.HEADING:
            lines = block.split("\n")
            for line in lines:
                if line[0] == "#":
                    heading_count = block[6:].count("#")
                    children.append(LeafNode(f"h{heading_count}", line))
                else:
                    nodes = text_to_textnodes(block)
                    for node in nodes:
                        children.append(text_node_to_html_node(node))
            return children
        case BlockType.CODE:
            return [ParentNode("pre", [LeafNode("code", block[3:-3])])]
        case BlockType.QUOTE:
            text_nodes = text_to_textnodes(block)
            for node in text_nodes:
                children.append(text_node_to_html_node(node))
            return [ParentNode("blockquote", children)]
        case BlockType.ORDERED_LIST:
            lines = block.split("\n")
            for line in lines:
                if re.match(line, r".^[[0-9]+\."):
                    children.append(LeafNode("li", re.sub(r".^[[0-9]+\.", "", line)))
                else:
                    nodes = text_to_textnodes(block)
                    for node in nodes:
                        children.append(text_node_to_html_node(node))
            return [ParentNode("ol", children)]
        case BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            for line in lines:
                if re.match(r"^- ", line):
                    children.append(LeafNode("li", re.sub(r".^- ", "", line)))
                else:
                    nodes = text_to_textnodes(block)
                    for node in nodes:
                        children.append(text_node_to_html_node(node))
            return [ParentNode("ul", children)]

    return []
