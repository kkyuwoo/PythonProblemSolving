n = int(input())
result = 0
xarr = []
yarr = []
for i in range(n):
    x, y = map(int, input().split())
    xarr.append(x)
    yarr.append(y)
result = (max(xarr)-min(xarr))*(max(yarr)-min(yarr))
if n == 1:
    result = 0
print(result)
