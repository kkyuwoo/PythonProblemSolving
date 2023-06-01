while True:
    n = int(input())
    if n == -1:
        break
    total = 0
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
            total += i
    if total == n:
        print(n,end= '')
        print(" = ",end='')
        for i in range(len(factors)-1):
            print(factors[i],end='')
            print(" + ",end='')
        print(factors[-1])
    else:
        print(n,end=' ')
        print("is NOT perfect.")