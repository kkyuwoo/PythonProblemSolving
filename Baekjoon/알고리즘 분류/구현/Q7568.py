n = int(input())

arr = []
answer = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

for i in range(n):
    count = 0
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            count += 1
    answer.append(count + 1)

for i in answer:
    print(i, end=" ")
