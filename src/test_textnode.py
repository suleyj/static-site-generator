import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    
    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, 'url1')
        node2 = TextNode("This is a text node", TextType.BOLD, 'url2')
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.LINK, 'url')
        node2 = TextNode("This is a text node", TextType.BOLD, 'url')
        self.assertNotEqual(node, node2)


    def test_not_eq_text(self):
        node = TextNode("This is not a text node", TextType.BOLD, 'url')
        node2 = TextNode("This is a text node", TextType.BOLD, 'url')
        self.assertNotEqual(node, node2)


    def test_not_eq_url_none(self):
        node = TextNode("This is not a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD, 'url')
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(repr(node), 'TextNode(This is not a text node, bold,)' )

if __name__ == "__main__":
    unittest.main()
