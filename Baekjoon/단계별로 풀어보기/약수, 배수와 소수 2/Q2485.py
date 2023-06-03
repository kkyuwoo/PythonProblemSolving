import math
import sys
n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

darr = []
for i in range(1, n):
        darr.append(arr[i]-arr[i-1])

distance = math.gcd(*darr)

cnt = 0
for i in darr:
    cnt += i // distance - 1
print(cnt)