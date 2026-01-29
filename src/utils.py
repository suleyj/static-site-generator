from htmlnode import LeafNode
from textnode import TextNode, TextType
import re


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("no matching text type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_text = old_node.text.split(delimiter)

        if len(split_text) % 2 == 0:
            raise Exception("missing delimeter")

        for i in range(len(split_text)):
            if split_text[i] == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                continue

            new_nodes.append(TextNode(split_text[i], text_type))

    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        if old_node.text == "" :
            continue

        images = extract_markdown_images(old_node.text)


        if len(images) == 0:
            new_nodes.append(TextNode(old_node.text, TextType.TEXT))
            continue;

        text_to_split = old_node.text

        for i in range(len(images)):
            image_alt, image_link = images[i]

            sections = text_to_split.split(f"![{image_alt}]({image_link})", 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

            if (len(images) - 1 == i) and (sections[1] != ""):
                new_nodes.append(TextNode(sections[1], TextType.TEXT))


            text_to_split = sections[1]

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        if old_node.text == "" :
            continue

        links = extract_markdown_links(old_node.text)

        if len(links) == 0:
            new_nodes.append(TextNode(old_node.text, TextType.TEXT))
            continue

        text_to_split = old_node.text

        for i in range(len(links)):
            link_text, link_url = links[i]

            sections = text_to_split.split(f"[{link_text}]({link_url})", 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            if (len(links) - 1 == i) and (sections[1] != ""):
                new_nodes.append(TextNode(sections[1], TextType.TEXT))

            text_to_split = sections[1]

    return new_nodes

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    image_nodes = split_nodes_image([text_node])
    link_nodes = split_nodes_link(image_nodes)
    italic_nodes = split_nodes_delimiter(link_nodes, '_', TextType.ITALIC)
    bold_nodes = split_nodes_delimiter(italic_nodes, '**', TextType.BOLD)
    code_nodes = split_nodes_delimiter(bold_nodes, '`', TextType.CODE)

    return code_nodes


def markdown_to_blocks(markdown):
    blocks = []
    split_blocks = markdown.split("\n\n")

    for block in split_blocks:
        block = block.strip()
        if block != "":
            blocks.append(block)

    return blocks



