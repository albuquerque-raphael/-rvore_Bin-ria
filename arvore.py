class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.data))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "E--- ")
            print_tree(node.right, level + 1, "D--- ")


root = Node("Avô")
root.left = Node("Pai")
root.right = Node("Tio")

root.left.left = Node("Você")
root.left.right = Node("Irmão/Irmã")

root.right.left = Node("Primo/Prima")
root.right.right = Node("Prima/Primo")

print_tree(root)
