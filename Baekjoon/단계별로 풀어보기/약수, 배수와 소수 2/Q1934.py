import math
import sys
t = int(input())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a, b))