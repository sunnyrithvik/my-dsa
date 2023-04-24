def is_valid_parenthesis(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


# Example usage
print(is_valid_parenthesis("()[]{}"))  # True
print(is_valid_parenthesis("([)]"))  # False
