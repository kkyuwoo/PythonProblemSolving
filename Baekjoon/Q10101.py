a = int(input())
b = int(input())
c = int(input())
result = ''

if a == 60 and b == 60 and c == 60:
    result = "Equilateral"
elif a+b+c == 180 and (a==b or b==c or a==c):
    result = "Isosceles"
elif a+b+c == 180 and (a!=b and a!=c and b!=c):
    result = "Scalene"
elif a+b+c != 180:
    result = "Error"

print(result)