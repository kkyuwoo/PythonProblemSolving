import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}
for i in range(n):
    s = sys.stdin.readline().strip()
    if s not in dic and len(s) >= m:
        dic[s] = 1
    elif s in dic:
        dic[s] += 1
dic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for key, value in dic:
    print(key)