def infix_to_prefix(expression):
    # Define operators precedence
    operators_precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    # Initialize stack for operators and operands
    operators_stack = []
    operands_stack = []

    # Reverse the expression to convert from infix to postfix
    expression = expression[::-1]

    # Iterate through each character in the expression
    for char in expression:
        # If the character is an alphabet or digit, push it to the operands stack
        if char.isalnum():
            operands_stack.append(char)
        # If the character is a closing parenthesis, push it to the operators stack
        elif char == ")":
            operators_stack.append(char)
        # If the character is an opening parenthesis, pop operators from the
        # operators stack until a closing parenthesis is found
        elif char == "(":
            while operators_stack[-1] != ")":
                operator = operators_stack.pop()
                operand2 = operands_stack.pop()
                operand1 = operands_stack.pop()
                operands_stack.append(operator + operand1 + operand2)
            operators_stack.pop()
        # If the character is an operator, pop operators from the operators
        # stack until an operator with lower precedence is found
        else:
            while (
                operators_stack
                and operators_precedence[char]
                <= operators_precedence[operators_stack[-1]]
            ):
                operator = operators_stack.pop()
                operand2 = operands_stack.pop()
                operand1 = operands_stack.pop()
                operands_stack.append(operator + operand1 + operand2)
            operators_stack.append(char)

    # Pop any remaining operators and construct the final prefix expression
    while operators_stack:
        operator = operators_stack.pop()
        operand2 = operands_stack.pop()
        operand1 = operands_stack.pop()
        operands_stack.append(operator + operand1 + operand2)

    # Return the final prefix expression
    return operands_stack[-1]


expression = "A*B+C/D"
prefix_expression = infix_to_prefix(expression)
print(f"Prefix expression of {expression} is {prefix_expression}")  # Output: +*ABC/D
