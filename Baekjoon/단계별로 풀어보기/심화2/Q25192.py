import sys
n = int(sys.stdin.readline())
dic = {}
result = 0
for i in range(n):
    s = sys.stdin.readline().strip()
    if s == "ENTER":
        for key, value in dic.items():
            if value == 1:
                result += 1
        dic = {}
    else:
        if s not in dic:
            dic[s] = 1

for key, value in dic.items():
    if value == 1:
        result += 1

print(result)