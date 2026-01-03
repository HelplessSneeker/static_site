from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.props = props
        super(LeafNode, self).__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag == None:
            return self.value
        html_props = self.props_to_html()
        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"

