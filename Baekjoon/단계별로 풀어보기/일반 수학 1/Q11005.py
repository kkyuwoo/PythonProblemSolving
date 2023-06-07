import sys
n, b = map(int, sys.stdin.readline().split())
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ''

while n:
    answer += str(arr[n%b])
    n //= b

for i in range(len(answer)-1, -1, -1):
    print(answer[i], end='')