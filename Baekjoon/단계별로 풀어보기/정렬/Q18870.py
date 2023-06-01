# 시간 초과
# n = int(input())
# arr = list(map(int, input().split()))
# result = sorted(list(set(arr)))
# for i in range(n):
#     print(result.index(arr[i]),end=' ')

n = int(input())
arr = list(map(int, input().split()))
result = sorted(list(set(arr)))
dic = {result[i]: i for i in range(len(result))}
for i in arr:
    print(dic[i], end=' ')