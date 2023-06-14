import sys
while True:
    s = sys.stdin.readline().rstrip()
    stack = []
    if s == ".":
        break
    result = "yes"
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[":
            stack.append(s[i])
        elif s[i] == ")" or s[i] == "]":
            if len(stack) == 0:
                result = "no"
                break
            else:
                top = stack.pop()
        if s[i] == ")" and top != "(":
            result = "no"
            break
        elif s[i] == "]" and top != "[":
            result = "no"
            break
    if len(stack) != 0:
        result = "no"
    print(result)
