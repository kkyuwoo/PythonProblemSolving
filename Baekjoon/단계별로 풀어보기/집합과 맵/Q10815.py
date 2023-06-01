n = int(input())
narr = list(map(int, input().split()))
m = int(input())
marr = list(map(int, input().split()))

dic = {}

for i in marr:
    dic[i] = 0

for i in narr:
    if i in dic:
        dic[i] += 1

for i in dic:
    print(dic[i], end=' ')