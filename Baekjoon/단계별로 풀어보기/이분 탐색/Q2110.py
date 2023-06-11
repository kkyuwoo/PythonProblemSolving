import sys
n, c = map(int, sys.stdin.readline().split())
home = []
for i in range(n):
    home.append(int(sys.stdin.readline().strip()))
home.sort()
start = 1 #가능한 최소 거리
end = home[n-1] - home[0] #가능한 최대 거리
result = 0

while (start <= end):
    mid = (start+end)//2 #가장 인접한 두 공유기 사이의 거리
    now = home[0]
    cnt = 1
    #현재의 mid 값을 이용해 공유기 설치
    for i in range(1, n): #두 번째 공유기부터 마지막까지
        if home[i] >= now + mid: #두 번째 값이 시작값 + 거리 보다 크면
            now = home[i]
            cnt += 1 #공유기 설치
    if cnt >= c: #c개 이상의 공유기를 설치할 수 있는 경우 거리 증가
        start = mid + 1
        result = mid
    else: #c개 이상의 공유기 설치할 수 없는 경우 거리 감소
        end = mid - 1
print(result)