for tc in range(1,11):
    try_num=int(input())
    case_num=list(map(int,input().split()))
    num_num=[0]*101
    cnt = 0
    minnum =0
    maxnum = 0
    
    for c in case_num:
        num_num[c] +=1

    for _ in range(try_num):
        
        maxcnt = True
        mincnt = True
        for idx,i in enumerate(num_num):
            if i and mincnt :
                num_num[idx] -=1
                num_num[idx+1] +=1
                if num_num[idx]:
                    minnum = idx
                else:
                    minnum =idx+1
                mincnt =False
            if num_num[-idx-1] and maxcnt :
                num_num[-idx-1] -=1
                num_num[-idx-2] +=1
                if num_num[-idx-1]:
                    maxnum = -idx-1+101
                else:
                    maxnum = -idx-2+101
                maxcnt = False
            if (maxnum - minnum)==0 or (maxnum - minnum)==1 :
                break
            if not (maxcnt and mincnt):
                break
    cnt = maxnum - minnum

    print('#{} {}'.format(tc,cnt))