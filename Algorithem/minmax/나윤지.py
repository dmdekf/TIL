tc = int(input())
for t in range(1,tc+1):
    num_len = int(input())
    numbers = list(map(int,input().split()))
    print('#{} {}'.format(t, max(numbers)-min(numbers)))