import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "p",
            "hey",
            [HTMLNode("p")],
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_empty(self):
        node = HTMLNode(
            "p",
            "hey",
            [HTMLNode("p")],
        )
        self.assertEqual(node.props_to_html(), "")

    def test_to_html_exception(self):
        node = HTMLNode(
            "p",
            "hey",
            [HTMLNode("p")],
        )
        self.assertRaises(NotImplementedError, node.to_html)


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_bold(self):
        node = LeafNode("b", "Make me bold")
        self.assertEqual(node.to_html(), "<b>Make me bold</b>")


if __name__ == "__main__":
    unittest.main()
