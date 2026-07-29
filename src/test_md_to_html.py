import unittest
from md_to_html import markdown_to_html_node


class TestBlockFunctions(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


#     def test_h1_image_block(self):
#         md = """
# # Tolkien Fan Club
#
# ![JRR Tolkien sitting](/images/tolkien.png)
#
# """
#
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             '<div><h1>Tolkien Fan Club</h1><img src="/images/tolekein.png"></img></div>',
#         )

    def test_ordered_list(self):
        md = """
# hey

1. First item
2. Second item with **bold** text
3. Third item with _italic_ text


"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>hey</h1><ol><li>First item</li><li>Second item with <b>bold</b> text</li><li>Third item with <i>italic</i> text</li></ol></div>",
        )

