
def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else "#"
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return len(stack) == 0
s = "()"
print(is_valid(s))

s = "() []{}"
print(is_valid(s))

s = "(]"
print(is_valid(s))
