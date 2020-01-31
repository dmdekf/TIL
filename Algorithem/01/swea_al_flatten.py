for tc in range(1,11):
    try_num=int(input())
    case_num=list(map(int,input().split()))
    num_num=[0]*100
    cnt = 0
    for i in case_num:
        if num_num[i] =i:
            num_num[i] +=1

    for _ in range(try_num):
        for idx,i in enumerate(num_num):
            if i:
                num_num[idx] -=1
                num_num[idx+1] +=1
                break
        for idx2,i in enumerate(num_num):
            if num_num[-idx2]:
                num_num[-idx2] -=1
                num_num[-idx2-1] +=1
                break
        cnt = idx+1-idx2-1+100

    print('#{} {}'.format(tc,cnt))
