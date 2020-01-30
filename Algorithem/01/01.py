arr = list(input())
count = [0]*10
# for i in range(6):
#     count[int(arr[i])] += 1
# print(count)

for x in arr:
    count[int(x)] += 1
print(count)