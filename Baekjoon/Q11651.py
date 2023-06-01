n = int(input())
dot = []
for i in range(n):
    x, y = map(int, input().split())
    dot.append([y, x])
dot.sort()
for i in range(n):
    print(dot[i][1], dot[i][0])