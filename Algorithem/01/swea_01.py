for tc in range(1, 11):
    tc_len = int(input())
    case = list(map(int, input().split()))
    temp = 0
    result = 0
    if tc_len <= 1000 and tc_len == len(case):
        for idx, num in enumerate(case):
            if 1 < idx < tc_len-2:
                for i in range(-2,3):
                    if i:
                        if num <= case[idx + i]:
                            temp = 0
                            break
                    if num < case[idx + i]:
                        temp = 0
                        break
                    if temp ==0:
                        if num > case[idx + i]:
                            temp = num - case[idx + i]
                    else:
                        if num > case[idx + i]:
                            if temp > num - case[idx + i]:
                                temp = num - case[idx + i]

                result += temp
                temp = 0
    print('#{} {}'.format(tc,result))

