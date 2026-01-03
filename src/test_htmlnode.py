import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_repr(self):
        node = HTMLNode('dir', None, [HTMLNode('p', 'paragraph', None, {'align-self': 'center'})] )
        self.assertEqual(f"{node}", "HTMLNode(dir, None, [HTMLNode(p, paragraph, None, {'align-self': 'center'})], None)")

    def test_prop_to_html(self):
        node = HTMLNode('p', 'paragraph', None, {'align-self': 'center', 'justify-content': 'center'})
        self.assertEqual(node.props_to_html(), ' align-self="center" justify-content="center"')

    def test_repr_None(self):
        node = HTMLNode('p', 'paragraph', None, {'align-self': 'center', 'justify-content': 'center'})
        self.assertEqual("HTMLNode(p, paragraph, None, {'align-self': 'center', 'justify-content': 'center'})", f"{node}")

if __name__ == "__main__":
    unittest.main()
