n = int(input())
check = 0;
for i in range(1, 1000000):
    result = 0
    result += i
    arr = list(str(i))
    for j in arr:
        result += int(j)
    if result == n:
        print(i)
        check = 1;
        break
if check == 0:
    print(0)