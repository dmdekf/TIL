for tc in range(1, 11):
    try_num = int(input())
    case_num = list(map(int, input().split()))
    case_num = sorted(case_num)
    for _ in range(try_num):
        case_num[0] += 1
        case_num[-1] -= 1
        case_num = sorted(case_num)
        if result == 1 or 0:
            break
        result = case_num[-1] - case_num[0]

    print('#{} {}'.format(tc, result))

