import unittest

# Importing my own files
from textnode import TextNode, TextType

# TestTextNode class
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


# Test Program starts here
if __name__ == "__main__":
    unittest.main()