import sys
n = int(sys.stdin.readline())
result = 1
if n == 1:
    result = 0
else:
    for i in range(1, n+1):
        result *= i
    for i in range(1, n-1):
        result //= i
print(result)