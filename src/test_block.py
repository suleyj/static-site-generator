import unittest
from markdown_blocks import block_to_block_type, BlockType


class TestBlockFunctions(unittest.TestCase):
    def test_heading_min_level(self):
        block = """
# This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_max_level(self):
        block = """
###### This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_above_max(self):
        block = """
####### This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.HEADING)

    def test_code_block(self):
        block = """
```
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
```
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_invalid_start_ticks_code_block(self):
        block = """
``
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
```
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.CODE)

    def test_invalid_end_ticks_code_block(self):
        block = """
```
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
``
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.CODE)

    def test_code_block_missing_new_line(self):
        block = """
```This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
```
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.CODE)

    def test_block_quote(self):
        block = """
>This is another paragraph with _italic_ text and `code` here
>This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_missing_chevron_block_quote(self):
        block = """
>This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.QUOTE)

    def test_emptyline_block_quote(self):
        block = """
>This is another paragraph with _italic_ text and `code` here

>This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.QUOTE)

    def test_space_block_quote(self):
        block = """
>This is another paragraph with _italic_ text and `code` here
> This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_empty_text_block_quote(self):
        block = """
>This is another paragraph with _italic_ text and `code` here
>
>This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_unordered_list(self):
        block = """
- This is another paragraph with _italic_ text and `code` here
- This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ULIST)

    def test_missing_space_unordered_list(self):
        block = """
-This is another paragraph with _italic_ text and `code` here
- This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.ULIST)

    def test_missing_dash_unordered_list(self):
        block = """
This is another paragraph with _italic_ text and `code` here
- This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.ULIST)

    def test_ordered_list(self):
        block = """
1 This is another paragraph with _italic_ text and `code` here
2 This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.OLIST)

    def test_invalid_numbers_ordered_list(self):
        block = """
1 This is another paragraph with _italic_ text and `code` here
3 This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.OLIST)

    def test_paragraph_block(self):
        block = """
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""
        block = block.strip()

        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
