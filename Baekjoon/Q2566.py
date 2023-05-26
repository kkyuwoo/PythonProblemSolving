arr = [list(map(int, input().split())) for _ in range(9)]
m = -1
ni = 0
mi = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] >= m:
            m = arr[i][j]
            ni = i
            mi = j
print(m)
print(ni+1,end=' ')
print(mi+1)