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
    if re_num:
        if len(install) > n//k:
            re_num = n // k
        else:
            re_num = len(install)

    print('#{} {}'.format(t, re_num))      