tc = int(input())
for t in range(1,tc+1):
    n_len = int(input())
    number = input()
    cnt = [0]*10
    cn = 0
    result = ''
    for i in number:
        cnt[int(i)] +=1
    cn =0
    for i in range(9,0,-1):
        if cnt[i] > cn:
            result = '{} {}'.format(i, cnt[i])
            cn = cnt[i]

    print('#{} {}'.format(t,result))