t = int(input())

for i in range(t):
    q = 0
    d = 0
    n = 0
    p = 0
    x = int(input())
    x = round(x / 100, 2)
    while(x != 0):
        if x >= 0.25:
            q += 1
            x = round(x-0.25, 2)
        elif x >= 0.1:
            d += 1
            x = round(x-0.1, 2)
        elif x >= 0.05:
            n += 1
            x = round(x-0.05, 2)
        elif x >= 0.01:
            p += 1
            x = round(x-0.01, 2)
        else:
            break
    print(q,end=' ')
    print(d, end=' ')
    print(n, end=' ')
    print(p)
