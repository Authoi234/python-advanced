class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)
    
    def add_left(self,node):
        self.left = node
    
    def add_right(self, node):
        self.right = node

def create_tree():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    nine.add_right(eight)
    three = Node(3)
    four = Node(4)
    eight.add_left(three)
    eight.add_right(four)

    return two

def print_tree(node, level=0):
    if node is not None:
        indent = "  " * level
        print(f"{indent}{node.data}")
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)

if __name__ == "__main__":
    root = create_tree()
    print_tree(root)