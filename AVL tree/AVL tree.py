from binarytree import build, Node

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if not node:
        return 0
    return node.height

def balance_factor(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right
    
    x.right = y
    y.left = T2
    
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    
    y.left = x
    x.right = T2
    
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    
    return y

def insert(root, value):
    if not root:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    
    balance = balance_factor(root)
    
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

def build_avl_tree(elements):
    root = None
    for element in elements:
        root = insert(root, element)
    return root

def convert_to_binarytree(avl_root):
    if not avl_root:
        return None
    node = Node(avl_root.value)
    node.left = convert_to_binarytree(avl_root.left)
    node.right = convert_to_binarytree(avl_root.right)
    return node

# Example usage
elements = [10, 5, 15, 2, 7, 12, 20]
avl_root = build_avl_tree(elements)
binary_tree_root = convert_to_binarytree(avl_root)

print("AVL Tree:")
print(avl_root)
print("\nBinary Tree:")
print(binary_tree_root)
