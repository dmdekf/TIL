num =[1, 3, 5, 7, 9]
x = 3
for i in range(len(num)-1):
    if num[i+1]-num[i] < x:
        result = True
        
    else:
        result = False
        break
print(result)
