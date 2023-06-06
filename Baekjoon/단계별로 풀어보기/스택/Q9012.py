import sys
t = int(sys.stdin.readline())
for i in range(t):
    stack = list(sys.stdin.readline().strip())
    total = 0
    for i in stack:
        if i == '(':
            total += 1
        else:
            total -= 1
        if total < 0:
            break
    if total == 0:
        print("YES")
    else:
        print("NO")