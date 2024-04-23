from binarytree import Node
import re

# Function to convert infix expression to postfix expression
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # Operator precedence dictionary
    stack = [] 
    postfix = ''

    # Iterate through each character in the expression
    for char in expression:
        if char.isalnum():  # If character is alphanumeric (operand) add it to expression
            postfix += char
        elif char == '(':  # If character is opening parenthesis push it onto the stack
            stack.append(char)
        elif char == ')':  # If character is closing parenthesis pop operators from the stack until '(' is encountered
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Pop '(' from the stack
        else:  # If character is an operator
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[char]:
                # Pop operators from the stack with higher or equal precedence and append to postfix
                postfix += stack.pop()
            stack.append(char)  # Push current operator onto the stack

    # Pop remaining operators from the stack and append to postfix
    while stack:
        postfix += stack.pop()

    return postfix  # Return the postfix expression

# Function to construct an expression tree from postfix expression
def construct_expression_tree(postfix_expression):
    stack = []

    # Iterate through each character in the postfix expression
    for char in postfix_expression:
        if char.isalnum():  # If character is alphanumeric (operand) create a leaf node and push onto the stack
            stack.append(Node(char))
        else:  # If character is an operator pop right and left operand from stack
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(char, left, right))  # Create an operator node and push onto the stack

    return stack.pop()  # Return the root of the expression tree

# Function to evaluate the expression tree
def evaluate_expression_tree(node):
    if node.left is None and node.right is None:  # If node is a leaf (operand) return the value of it
        return int(node.value)
    left_value = evaluate_expression_tree(node.left) # Recursively evaluate subtrees
    right_value = evaluate_expression_tree(node.right)
    # If the node is an operator do the operation
    if node.value == '+':
        return left_value + right_value
    elif node.value == '-':
        return left_value - right_value
    elif node.value == '*':
        return left_value * right_value
    elif node.value == '/':
        if (right_value == 0):
            print("Error: division by 0")
            exit()
        return left_value / right_value

# Function to convert expression tree to Polish notation
def to_polish_notation(node):
    if node is None:  # If node is None
        return ""  # Return empty string
    if node.left is None and node.right is None:  # If node is a leaf (operand)
        return str(node.value) # Return the operand value
    left_expr = to_polish_notation(node.left) # Recursively convert subtrees to Polish notation
    right_expr = to_polish_notation(node.right)
    return f"{node.value} {left_expr} {right_expr}" # Return node value followed by left and right expressions


def main():
    infix_expression = input("Enter an infix expression: ")
    infix_expression = re.sub(r'\s+', '', infix_expression)  # Remove whitespace from the expression
    postfix_expression = infix_to_postfix(infix_expression)  # Convert infix to postfix
    expression_tree = construct_expression_tree(postfix_expression)  # Construct to expression tree
    print("Expression Tree:")
    print(expression_tree)

    result = evaluate_expression_tree(expression_tree)  # Evaluate the expression tree
    print("Result of evaluation:", result)

    polish_notation = to_polish_notation(expression_tree)  # Convert expression tree to Polish notation
    print("Polish Notation:", polish_notation)

if __name__ == "__main__":
    main()