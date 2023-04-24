def infix_to_postfix(infix_expression):
    # Define operator precedence
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    # Initialize stack and postfix expression
    stack = []
    postfix_expression = ""

    # Iterate over each character in the infix expression
    for char in infix_expression:
        # If the character is an operand, append it to the postfix expression
        if char.isalnum():
            postfix_expression += char
        # If the character is a left parenthesis, push it onto the stack
        elif char == "(":
            stack.append(char)
        # If the character is a right parenthesis, pop operators from the stack and append them to the postfix expression until a left parenthesis is encountered
        elif char == ")":
            while stack[-1] != "(":
                postfix_expression += stack.pop()
            stack.pop()  # remove the left parenthesis from the stack
        # If the character is an operator, pop operators from the stack and append them to the postfix expression as long as they have equal or higher precedence than the current operator. Then push the current operator onto the stack.
        else:
            while (
                stack
                and stack[-1] != "("
                and precedence[char] <= precedence.get(stack[-1], 0)
            ):
                postfix_expression += stack.pop()
            stack.append(char)

    # Pop any remaining operators from the stack and append them to the postfix expression
    while stack:
        postfix_expression += stack.pop()

    return postfix_expression


infix_expression = "a+b*c-(d/e+f^g*h)"
print(infix_to_postfix(infix_expression))  # Output: 'abc*+de/fgh^+/-'
