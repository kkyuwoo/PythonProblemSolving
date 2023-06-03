import math
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    for i in range(n, 4*(10**10)):
        factors = True
        if i == 1:
            factors = False
        if i == 2 or i == 0:
            print(2)
            break
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                factors = False
                break
        if factors == True:
            print(i)
            break