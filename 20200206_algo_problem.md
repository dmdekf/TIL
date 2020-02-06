# 20200206

## algo 문제풀이

#### 2005 재귀

- base case : 
  - 정답을 찾았을 때
  - 못 찾았을 때
- recursive step
  - 계속 가야할 때
- 데이터 (누적) : 인자

#### 6090 단조증가 중요!

```python

def check(n):
    flag = True
    while n:
        n, r = n // 10, n % 10
        if n % 10 > r:
            return False
        
    return flag
```

