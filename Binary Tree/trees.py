from binarytree import Node, tree

# Page 284
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)
eleven = Node(11)
twelve = Node(12)

one.left = two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven
four.left = eight
four.right = nine
six.left = ten
six.right = eleven
seven.right = twelve

print(one)

# Page 285

# Define the nodes
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")

# Build the tree structure
A.left = B
A.right = C
C.left = D
D.right = E

# Print the tree
print(A)

A = Node("F")
B = Node("G")
C = Node("H")
D = Node("I")
E = Node("J")

# Build the tree structure
A.left = B
A.right = C
C.left = D
D.right = E

print(A)

# Define the nodes
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")

# Build the tree structure
A.left = B
A.right = C
C.left = D
C.right = E

# Print the tree
print(A)

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)
eleven = Node(11)
twelve = Node(12)
thirteen = Node(13)

one.left = two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven
four.left = eight
four.right = nine
five.left = ten
five.right = eleven
six.left = twelve
six.right = thirteen

print(one)