from binarytree import Node
import re

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = ''

    for char in expression:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[char]:
                postfix += stack.pop()
            stack.append(char)

    while stack:
        postfix += stack.pop()

    return postfix

def construct_expression_tree(postfix_expression):
    stack = []

    for char in postfix_expression:
        if char.isalnum():
            stack.append(Node(char))
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(char, left, right))

    return stack.pop()

def infix_to_expression_tree(infix_expression):
    postfix_expression = infix_to_postfix(infix_expression)
    return construct_expression_tree(postfix_expression)

def main():
    infix_expression = input("Enter an infix expression: ")
    infix_expression = re.sub(r'\s+', '', infix_expression)  # Remove whitespace
    expression_tree = infix_to_expression_tree(infix_expression)
    print("Expression Tree:")
    print(expression_tree)

if __name__ == "__main__":
    main()
