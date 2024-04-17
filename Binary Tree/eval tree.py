from binarytree import Node  # Import Node class from binarytree library
import re  # Import regular expression module

# Function to convert infix expression to postfix expression
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # Define operator precedence
    stack = []  # Initialize an empty stack to hold operators
    postfix = ''  # Initialize an empty string to hold the postfix expression

    for char in expression:
        if char.isalnum():  # If character is alphanumeric (operand)
            postfix += char  # Append it to the postfix expression
        elif char == '(':  # If character is '('
            stack.append(char)  # Push it onto the stack
        elif char == ')':  # If character is ')'
            while stack and stack[-1] != '(':  # Pop operators from the stack and append to postfix until '(' is encountered
                postfix += stack.pop()
            stack.pop()  # Discard the '('
        else:
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[char]:
                postfix += stack.pop()  # Pop operators from the stack and append to postfix while precedence condition is met
            stack.append(char)  # Push the current operator onto the stack

    while stack:
        postfix += stack.pop()  # Append remaining operators from the stack to postfix

    return postfix  # Return the postfix expression

# Function to construct expression tree from postfix expression
def construct_expression_tree(postfix_expression):
    stack = []  # Initialize an empty stack to hold nodes

    for char in postfix_expression:
        if char.isalnum():  # If character is alphanumeric (operand)
            stack.append(Node(char))  # Create a leaf node with the operand and push onto the stack
        else:
            right = stack.pop()  # Pop the right operand node
            left = stack.pop()   # Pop the left operand node
            stack.append(Node(char, left, right))  # Create a new node with the current operator and operands, and push onto the stack

    return stack.pop()  # Return the root of the expression tree

# Function to convert infix expression to expression tree
def infix_to_expression_tree(infix_expression):
    postfix_expression = infix_to_postfix(infix_expression)  # Convert infix expression to postfix expression
    return construct_expression_tree(postfix_expression)  # Construct expression tree from postfix expression

# Function to evaluate expression tree
def evaluate_expression_tree(root):
    if root.left is None and root.right is None:
        return int(root.value)  # If node is a leaf node (operand), return its value
    else:
        left_val = evaluate_expression_tree(root.left)  # Recursively evaluate left subtree
        right_val = evaluate_expression_tree(root.right)  # Recursively evaluate right subtree
        if root.value == '+':
            return left_val + right_val  # If node is addition operator, return sum of left and right subtree values
        elif root.value == '-':
            return left_val - right_val  # If node is subtraction operator, return difference of left and right subtree values
        elif root.value == '*':
            return left_val * right_val  # If node is multiplication operator, return product of left and right subtree values
        elif root.value == '/':
            return left_val / right_val  # If node is division operator, return quotient of left and right subtree values
        elif root.value == '^':
            return left_val ** right_val  # If node is exponentiation operator, return left subtree raised to the power of right subtree

# Function to convert expression tree to Polish notation
def to_polish_notation(root):
    if root is None:
        return ''  # Base case: if root is None, return empty string
    if root.left is None and root.right is None:
        return root.value  # Base case: if node is leaf node (operand), return its value
    return root.value + ' ' + to_polish_notation(root.left) + ' ' + to_polish_notation(root.right)  # Concatenate node value with Polish notation of left and right subtrees

# Main function
def main():
    infix_expression = input("Enter an infix expression: ")  # Prompt user to enter infix expression
    infix_expression = re.sub(r'\s+', '', infix_expression)  # Remove whitespace from infix expression
    expression_tree = infix_to_expression_tree(infix_expression)  # Convert infix expression to expression tree
    print("Expression Tree:")  
    print(expression_tree)  # Print the expression tree
    
    result = evaluate_expression_tree(expression_tree)  # Evaluate the expression tree
    print("Evaluation Result:", result)  # Print the evaluation result
    
    polish_notation = to_polish_notation(expression_tree)  # Convert expression tree to Polish notation
    print("Polish Notation:", polish_notation)  # Print the Polish notation

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly