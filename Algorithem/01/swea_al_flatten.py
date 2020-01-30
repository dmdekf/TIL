for tc in range(1,11):
    try_num=int(input())
    case_num=list(map(int,input().split()))
    num_num=[0]*100
    cnt = 0
    for _ in range(try_num-1):
        for index in range(100-1):
            swap = False
            for index2 in range(100 -index-1,):
                if case_num[index2] > case_num[index2+1]:
                    case_num[index2] , case_num[index2+1] =  case_num[index2+1], case_num[index2]
                    swap = True
                if swap == False:
                    break
            case_num[0] +=1
            case_num[-1] -=1


        # for i in case_num:
        #     num_num[i] +=1
        # for index in
    print('#{} {}'.format(tc,result))