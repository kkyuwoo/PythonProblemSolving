while True:
    a, b, c = map(int, input().split())
    result = ''
    if a == 0 and b == 0 and c == 0:
        break
    if a != b and a != c and b != c:
        result = "Scalene"
    if a == b and a == c and b == c:
        result = "Equilateral"
    if (a == b and b != c and a != c) or (a == c and a != b and b != c) or (b == c and b != a and c != a):
        result = "Isosceles"
    if a > b and a > c:
        if a >= b + c:
            result = "Invalid"
    elif b > c and b > a:
        if b >= a + c:
            result = "Invalid"
    elif c > a and c > b:
        if c >= a + b:
            result = "Invalid"
    print(result)