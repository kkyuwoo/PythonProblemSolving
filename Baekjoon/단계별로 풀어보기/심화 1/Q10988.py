s = input()
reverse = ''
for i in s:
    reverse = i + reverse
if reverse == s:
    print(1)
else:
    print(0)