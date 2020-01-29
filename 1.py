day = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
test = int(input())
t = 0
while t <= test:
    num_list = input().split()
    if num_list[0] <= num_list[2] and 0 < int(num_list[0]) < 13 and 0 < int(num_list[2]) < 13:
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])
        result = 0
        if num_list[0] == num_list[2]:
            result = num_list[3]-num_list[1]+1
        else:
            result = num_list[3]-num_list[1]+1
            for i in range(num_list[2]-1, num_list[0]-1, -1):
                result += day[i]
    print(f'#{t+1} {result}')
    t += 1
