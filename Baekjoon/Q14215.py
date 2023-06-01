a, b, c = map(int, input().split())
if a >= b and a >= c:
    if a >= b + c:
        a = b + c - 1
elif b >= c and b >= a:
    if b >= a + c:
        b = a + c - 1
elif c >= a and c >= b:
    if c >= a + b:
        c = a + b - 1
print(a+b+c)