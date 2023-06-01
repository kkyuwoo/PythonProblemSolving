x, y, w, h = map(int, input().split())
print(min(abs(w-x), abs(h-y), abs(x-0), abs(y-0)))