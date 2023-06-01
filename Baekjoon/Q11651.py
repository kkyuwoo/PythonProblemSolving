n = int(input())
dot = []
for i in range(n):
    x, y = map(int, input().split())
    dot.append((x, y))
dot = sorted(dot, key=lambda x : (x[1], x[0]))
for i in range(n):
    print(dot[i][0], dot[i][1])