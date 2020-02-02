tc = int(input())
for t in range(1, tc+1):
    n, m = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    sum_list = []
    temp = 0
    for i in range(n-m+1):
        for j in range(m):
            temp += numbers[i+j]
        sum_list.append(temp)
        temp = 0
    sum_list = sorted(sum_list)

    print('#{} {}'.format(t, sum_list[-1]-sum_list[0]))
