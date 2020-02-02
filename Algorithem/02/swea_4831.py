
# k = 최대이동횟수
# m 충전기 설치 개수
# n : 도달지점.
tc = int(input())
for t in range(1, tc+1):
    k, n, m = list(map(int, input().split()))
    install = list(map(int, input().split()))
    temp = 0
    cnt = 0
    while temp + k < n:
        result = []
        for i in install:
            if temp < i <= temp+k:
                result.append(i)
        if result == []:
            cnt = 0
            break
        temp = result[-1]
        cnt += 1
    print('#{} {}'.format(t, cnt))
