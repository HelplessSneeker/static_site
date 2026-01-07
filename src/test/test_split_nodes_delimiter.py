import unittest

from src.textnode import TextNode, TextType
from src.functions import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_bold(self):
        node = TextNode(
            "This is text with a **bold block** word and another **bold**",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word and another ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected_nodes)
