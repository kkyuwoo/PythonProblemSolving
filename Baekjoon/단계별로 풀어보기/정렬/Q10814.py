n = int(input())
arr = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    arr.append([age, name])
arr.sort(key=lambda x : x[0])
for i in range(n):
    print(arr[i][0], arr[i][1])