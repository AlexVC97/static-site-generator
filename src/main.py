# Importing my own files
from textnode import TextNode, TextType

# Functions
def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)


# Program starts here
if __name__ == "__main__":
    main()