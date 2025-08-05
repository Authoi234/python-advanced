def is_balanced(input_str):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in input_str:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return not stack

x = input("Enter brackets: ")
if is_balanced(x):
    print("it is balanced")
else:
    print("it is not balanced")