from binarytree import Node
import random

# Function to create a binary search tree from a list of values
def insert_node(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert_node(root.left, value)
        else:
            root.right = insert_node(root.right, value)
    return root

# Function to perform in-order traversal and collect values (tree sort)
def in_order_traversal(root, sorted_values):
    if root:
        in_order_traversal(root.left, sorted_values)
        sorted_values.append(root.value)
        in_order_traversal(root.right, sorted_values)

# Create a list of random values
random_values = [random.randint(1, 100) for i in range(10)]

# Build the binary search tree
bst_root = None
for value in random_values:
    bst_root = insert_node(bst_root, value)

# Display the tree using binarytree library
print("Binary Search Tree:")
print(bst_root)

# Perform tree sort (in-order traversal)
sorted_values = []
in_order_traversal(bst_root, sorted_values)
print("Sorted values:")
print(sorted_values)
