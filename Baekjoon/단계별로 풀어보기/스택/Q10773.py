import sys
k = int(sys.stdin.readline())
stack = []
for i in range(k):
    n = int(sys.stdin.readline().strip())
    if n != 0:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))