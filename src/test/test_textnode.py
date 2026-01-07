import unittest

from src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr_image(self):
        node = TextNode("This is a image", TextType.IMAGE, "test.com")
        self.assertEqual(f"{node}", "TextNode(This is a image, image, test.com)")

    def test_repr_plain(self):
        node = TextNode("This is a plain text", TextType.PLAIN)
        self.assertEqual(f"{node}", "TextNode(This is a plain text, plain, None)")


if __name__ == "__main__":
    unittest.main()
