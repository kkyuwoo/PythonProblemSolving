import sys
n = int(sys.stdin.readline())
result = 0
i = 1
while i*i <= n:
    i += 1
    result += 1
print(result)