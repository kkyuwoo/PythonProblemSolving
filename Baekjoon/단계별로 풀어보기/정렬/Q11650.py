n = int(input())
dot = []
for i in range(n):
    x, y = map(int, input().split())
    dot.append((x, y))
dot.sort()
for i in range(n):
    print(dot[i][0], dot[i][1])