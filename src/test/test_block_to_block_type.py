import unittest

from src.block_functions import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        type = block_to_block_type("test")
        self.assertEqual(BlockType.PARAGRAPH, type)

    def test_heading(self):
        type = block_to_block_type("### heading")
        self.assertEqual(BlockType.HEADING, type)

    def test_code(self):
        type = block_to_block_type(
            """```
            code
```"""
        )
        self.assertEqual(BlockType.CODE, type)

    def test_ordered_list(self):
        type = block_to_block_type("1. meine liste")
        self.assertEqual(BlockType.ORDERED_LIST, type)

    def test_unordered_list(self):
        type = block_to_block_type("- meine liste")
        self.assertEqual(BlockType.UNORDERED_LIST, type)

    def test_quote(self):
        type = block_to_block_type("> meine liste")
        self.assertEqual(BlockType.QUOTE, type)
