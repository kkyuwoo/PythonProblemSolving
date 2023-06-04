import sys
n, k = map(int, sys.stdin.readline().split())
result = 1
for i in range(1, n+1):
    result *= i
for i in range(1, n-k+1):
    result //= i
for i in range(1, k+1):
    result //= i
print(result)