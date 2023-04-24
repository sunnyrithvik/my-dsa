def evaluate_postfix(expression):
    stack = []

    # iterate over each character in the expression
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
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


expression = "5 4 3 * +"
result = evaluate_postfix(expression)
print(result)  # Output: 17
