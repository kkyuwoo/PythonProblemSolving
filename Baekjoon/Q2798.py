n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []
real = 0
for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(j+1, len(arr)):
            result.append(arr[i] + arr[j] + arr[k])
for i in result:
    if i <= m and i >= real:
        real = i
print(real)