import unittest

from textnode import TextNode, TextType
from utils import text_node_to_html_node

class TestUtilFunctions(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("tiger image", TextType.IMAGE, "https://www.birds.com/bird.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, { "src": "https://www.birds.com/bird.png", "alt": "tiger image"} )
