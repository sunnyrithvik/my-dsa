def evaluate_prefix(expression):
    stack = []
    operators = {"+", "-", "*", "/"}

    # reverse the order of characters in the expression
    expression = expression[::-1]

    # iterate over each character in the expression
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            result = None

            if char == "+":
                result = op1 + op2
            elif char == "-":
                result = op1 - op2
            elif char == "*":
                result = op1 * op2
            elif char == "/":
                result = op1 / op2

            stack.append(result)

    return stack.pop()


expression = "+ 5 * 4 3"
result = evaluate_prefix(expression)
print(result)  # Output: 17
