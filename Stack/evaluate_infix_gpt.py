def evaluate_infix(expression):
    # define operator precedence
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    # initialize stacks for operators and operands
    operator_stack = []
    operand_stack = []

    # iterate over each character in the expression
    for char in expression:
        if char.isdigit():
            operand_stack.append(int(char))
        elif char in ["+", "-", "*", "/"]:
            # pop operators from operator stack until we find one with lower precedence
            while (
                len(operator_stack) > 0
                and precedence[operator_stack[-1]] >= precedence[char]
            ):
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                operator = operator_stack.pop()

                result = None
                if operator == "+":
                    result = op1 + op2
                elif operator == "-":
                    result = op1 - op2
                elif operator == "*":
                    result = op1 * op2
                elif operator == "/":
                    result = op1 / op2

                operand_stack.append(result)

            operator_stack.append(char)

    # pop any remaining operators and evaluate them
    while len(operator_stack) > 0:
        op2 = operand_stack.pop()
        op1 = operand_stack.pop()
        operator = operator_stack.pop()

        result = None
        if operator == "+":
            result = op1 + op2
        elif operator == "-":
            result = op1 - op2
        elif operator == "*":
            result = op1 * op2
        elif operator == "/":
            result = op1 / op2

        operand_stack.append(result)

    return operand_stack.pop()


expression = "5 + 4 * 3"
result = evaluate_infix(expression)
print(result)  # Output: 17
