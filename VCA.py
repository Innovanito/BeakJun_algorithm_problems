from collections import deque


def is_properly_set(input):
    stack = []
    opening_brackets = {'(', '{', '['}
    closing_brackets = {')': '(', '}': '{', ']': '['}

    for bracket in input:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack or stack[-1] != closing_brackets[bracket]:
                return False
            stack.pop()

    return not stack


inputValue = map(str, input().strip())

print(is_properly_set(inputValue))
