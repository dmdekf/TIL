#  N, M, K: n명 손님 m초에 k개씩 만듦
#  도착하는 시간
tc = int(input())
for t in range(1,tc+1):
    n, m , k = list(map(int,input().split()))
    arrive = list(map(int,input().split()))
    cnt = [0]*(max(arrive)+1)
    temp = 0
    result = 'Impossible'
    if min(arrive) < m:
        print('#{} {}'.format(t, result))

    else:
        for a in arrive:
            cnt[a] +=1
        for i in range(len(cnt)):
            if i % m == 0 and i != 0:
                temp +=k
            if cnt[i]:
                temp -= cnt[i]
            if temp < 0:
                result = 'Impossible'
                break
            else:
                result = 'Possible'
        print('#{} {}'.format(t, result))

 # 1 Possible
# 2 Impossible
