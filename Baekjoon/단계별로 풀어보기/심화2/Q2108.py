import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()
print(int(round(sum(arr)/n,0)))
print(arr[n//2])

dic = {}

for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

mx = max(dic.values())
mx_dic = []

for i in dic:
    if mx == dic[i]:
        mx_dic.append(i)
if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])
print(max(arr)-min(arr))