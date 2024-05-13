# Importing Node class from binarytree module for visualization
from binarytree import Node

# Definition of a TreeNode for AVL Tree
class TreeNode:
    def __init__(self, value):
        self.value = value  # Value stored in the node
        self.left = None    # Pointer to the left child
        self.right = None   # Pointer to the right child
        self.height = 1     # Height of the node in the AVL Tree

# Function to get the height of a node
def height(node):
    if not node:
        return 0
    return node.height

# Function to calculate the balance factor of a node
def balance_factor(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

# Function to perform a right rotation on a given node
def rotate_right(y):
    x = y.left
    T2 = x.right
    
    # Perform rotation
    x.right = y
    y.left = T2
    
    # Update heights
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    
    return x

# Function to perform a left rotation on a given node
def rotate_left(x):
    y = x.right
    T2 = y.left
    
    # Perform rotation
    y.left = x
    x.right = T2
    
    # Update heights
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    
    return y

# Function to insert a value into AVL Tree
def insert(root, value):
    if not root:
        return TreeNode(value)  # Create a new node if the tree is empty
    
    # Perform standard BST insertion
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    else:
        return root  # Value already exists
    
    # Update height of the current node
    root.height = 1 + max(height(root.left), height(root.right))
    
    # Get the balance factor of this node to check if it's unbalanced
    balance = balance_factor(root)
    
    # If unbalanced, perform necessary rotations
    if balance > 1:
        if value < root.left.value:
            return rotate_right(root)
        else:
            root.left = rotate_left(root.left)
            return rotate_right(root)
    
    if balance < -1:
        if value > root.right.value:
            return rotate_left(root)
        else:
            root.right = rotate_right(root.right)
            return rotate_left(root)
    
    return root

# Function to build an AVL Tree from a list of elements
def build_avl_tree(elements):
    root = None
    for element in elements:
        root = insert(root, element)
    return root

# Function to convert an AVL Tree to a binary tree for visualization
def convert_to_binarytree(avl_root):
    if not avl_root:
        return None
    node = Node(avl_root.value)
    node.left = convert_to_binarytree(avl_root.left)
    node.right = convert_to_binarytree(avl_root.right)
    return node

# Function to print AVL Tree as a binary tree
def print_trees(avl_root):
    binary_tree_root = convert_to_binarytree(avl_root)
    print(binary_tree_root)

# Example usage
elements = []
while True:
    try:
        value = int(input("Enter a value to insert into the AVL tree (or enter any non-integer to finish): "))
        elements.append(value)
        avl_root = build_avl_tree(elements)
        print_trees(avl_root)
    except ValueError:
        print("Finished inserting values into the AVL tree.")
        break
