import sys
n, m = map(int, input().split())
dic = {}

for i in range(1, n+1):
    key = sys.stdin.readline().strip()
    dic[key] = i
    dic[i] = key

for i in range(m):
    str = sys.stdin.readline().strip()
    if str.isdigit():
        str = int(str)
        print(dic[str])
    else:
        print(dic[str])