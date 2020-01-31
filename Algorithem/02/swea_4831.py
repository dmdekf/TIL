# n = 종점정류장

# k = 최대이동횟수
# m 충전기 설치 개수
# m의 정류장 번호. 
# 1.최대 이동 횟수  n / k
# x = 최소 중전해야 할 횟수
# m = 충전기 설치 개수 < x: break
# 2. k이내에서 충전기 번호가 제일 클 경우 선택, cnt +1 k +=k
# n 도달해야 하는 정류장.

tc = int(input())
for t in range(1,tc+1):
    result = []
    numbers = list(map(int,input().split()))
    install = list(map(int,input().split()))
    k, n, m = numbers[0],numbers[1],numbers[2]
    re_num = 0
    if n // k > m:
        re_num = 0
        break
    for x in range(len(install)-1):
        if install[x+1]-install[x] < k:
            re_num = len(install)
        else:
            re_num = 0
            break
            
    if len(install) > n//k:
        re_num = n // k
    else:
        re_num = len(install)

    print('#{} {}'.format(t, re_num))
                    
