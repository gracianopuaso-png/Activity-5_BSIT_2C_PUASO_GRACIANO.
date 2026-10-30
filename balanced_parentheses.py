def check_balanced(expression):
    stack = []

    matching = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for character in expression:

        if character in "([{":
            stack.append(character)

        elif character in ")]}":

            if not stack:
                return False

            if stack.pop() != matching[character]:
                return False

    return len(stack) == 0