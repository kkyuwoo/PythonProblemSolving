answer = ''
while(True) :
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    if n >= m:
        if n % m == 0:
            answer = "multiple"
        else:
            answer = "neither"
    else:
        if m % n == 0:
            answer = "factor"
        else:
            answer = "neither"
    print(answer)
