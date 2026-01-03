
from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super(ParentNode, self).__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("All parent nodes must have a tag.")
        if self.children == None or len(self.children) == 0:
            raise ValueError("All parent nodes must have atleast one children.")

        children_string = ""

        for child in self.children:
            children_string += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"

