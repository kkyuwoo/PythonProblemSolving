n = int(input())
dic = {}
for i in range(n):
    key, value = input().split()
    dic[key] = value;

result = []
for key, value in dic.items():
    if value == "enter":
        result.append(key)

result.sort(reverse=True)
for i in result:
    print(i)