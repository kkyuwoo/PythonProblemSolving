import sys
n = int(sys.stdin.readline())
stack = []
answer = []
now = 1
check = 0
for i in range(n):
    num = int(sys.stdin.readline().strip())
    while now <= num:
       stack.append(now)
       answer.append("+")
       now += 1
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        check = 1
        break
if check == 0:
    for i in answer:
        print(i)