xarr = []
yarr = []
rx = 0
ry = 0
for i in range(3):
    x, y = map(int ,input().split())
    xarr.append(x)
    yarr.append(y)
for i in xarr:
    if xarr.count(i) == 1:
        rx = i
for i in yarr:
    if yarr.count(i) == 1:
        ry = i
print(rx, end=' ')
print(ry)