import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()
answer = []
for i in range(1, n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<", end='')
for i in range(n-1):
    print(answer[i], end=', ')
print(answer[-1], end='')
print(">")