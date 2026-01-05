from textnode import TextType, TextNode
from leafnode import LeafNode
import re

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.PLAIN:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {'href': text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", None, {'src': text_node.url, "alt": text_node.text})

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        text = node.text
        text_arr = text.split(delimiter)
        
        for i in range(0, len(text_arr)):
            if not text_arr[i]:
                continue
            new_nodes.append(TextNode(text_arr[i], TextType.PLAIN if i % 2 == 0 else text_type))

    return new_nodes

def extract_markdown_images(text):
    match = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return match

def extract_markdown_links(text):
    match = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return match

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        text = node.text
        text = node.text
        images = extract_markdown_images(text)
        image_counter = 0
        preped_text = re.sub(r"!\[(.*?)\]\((.*?)\)", "![]!", text)
        text_arr = preped_text.split('!')
        for t in text_arr:
            if not t:
                continue

            if t == '[]':
                new_nodes.append(TextNode(images[image_counter][0], TextType.IMAGE, images[image_counter][1]))
                image_counter += 1
                continue

            new_nodes.append(TextNode(t, TextType.PLAIN))
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        link_counter = 0
        preped_text = re.sub(r"\[(.*?)\]\((.*?)\)", "![]!", text)
        text_arr = preped_text.split('!')
        for t in text_arr:
            if not t:
                continue

            if t == '[]':
                new_nodes.append(TextNode(links[link_counter][0], TextType.LINK, links[link_counter][1]))
                link_counter += 1
                continue

            new_nodes.append(TextNode(t, TextType.PLAIN))
            
    return new_nodes

def text_to_textnodes(text):
    nodes = []
    node = TextNode(text, TextType.PLAIN)
    nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    return split_nodes_link(nodes)






