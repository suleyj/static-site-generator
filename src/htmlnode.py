class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""

        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'

        return props_str

    def __repr__(self):

        props_str = self.props_to_html()

        node_str = f"<{self.tag} {props_str}> {self.value}"

        if self.children:
            for children in self.children:
                node_str += children.to_html()

        node_str += f"</{self.tag}>"

        return node_str


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError

        if not self.tag:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.children:
            raise ValueError('Missing children value')

        if not self.tag:
            raise ValueError('Missing tag value')

        children = ""

        for child in self.children :
            children += child.to_html()

        return f"<{self.tag}>{children}</{self.tag}>"
