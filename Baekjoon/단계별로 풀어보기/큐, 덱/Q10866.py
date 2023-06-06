import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque()
for i in range(n):
    s = sys.stdin.readline().strip()
    if ' ' in s:
        s = s.split()
        if s[0] == "push_back":
            d.append(s[1])
        elif s[0] == "push_front":
            d.appendleft(s[1])
    elif s == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    elif s == "back":
        if d:
            print(d[-1])
        else:
            print(-1)
    elif s == "size":
        print(len(d))
    elif s == "empty":
        if d:
            print(0)
        else:
            print(1)
    elif s == "pop_front":
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif s == "pop_back":
        if d:
            print(d.pop())
        else:
            print(-1)