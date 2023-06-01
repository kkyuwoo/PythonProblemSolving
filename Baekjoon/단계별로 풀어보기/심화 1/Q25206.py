total = 0
count = 0
for i in range(20):
    s = input().split()
    score = float(s[1])
    if s[2] == "A+":
        total += score * 4.5
        count += score
    elif s[2] == "A0":
        total += score * 4.0
        count += score
    elif s[2] == "B+":
        total += score * 3.5
        count += score
    elif s[2] == "B0":
        total += score * 3.0
        count += score
    elif s[2] == "C+":
        total += score * 2.5
        count += score
    elif s[2] == "C0":
        total += score * 2.0
        count += score
    elif s[2] == "D+":
        total += score * 1.5
        count += score
    elif s[2] == "D0":
        total += score * 1.0
        count += score
    elif s[2] == "F":
        total += score * 0.0
        count += score
print(f"{total/count:.6f}")

