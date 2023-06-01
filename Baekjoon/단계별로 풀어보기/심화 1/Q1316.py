n = int(input())

group = 0
for i in range(n):
    w = input()
    count = 0
    for j in range(len(w)-1):
        if w[j] != w[j+1]:
            if w[j] in w[j+1:]:
                count +=1
    if count == 0:
        group +=1

print(group)