import sys
n = int(sys.stdin.readline())
dic = {}
result = 1
for i in range(n):
    a, b = sys.stdin.readline().split()
    if a == "ChongChong":
        dic[b] = 1
    elif b == "ChongChong":
        dic[a] = 1
    elif a in dic:
        if dic[a] == 1:
            dic[b] = 1
    elif b in dic:
        if dic[b] == 1:
            dic[a] = 1

for i in range(len(dic)):
    result += 1
print(result)