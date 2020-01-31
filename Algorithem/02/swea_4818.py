tc = int(input())
for t in range(1,tc+1):
    num_len = int(input())
    numbers = list(map(int,input().split()))
    maxn = max(numbers)
    minn = min(numbers)
    result = maxn - minn
    print('#{} {}'.format(t, result))