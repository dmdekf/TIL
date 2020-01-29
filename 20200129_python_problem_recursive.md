# 20200129

## python

### 04_data_structure_-01

<문제풀이>

`sorted(key, reverse)`

```
Signature: sorted(iterable, /, *, key=None내가 원하는 함수기준을 적용 가능., reverse=False)
Docstring:
Return a new list containing all items from the iterable in ascending order.

A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order.
Type:      builtin_function_or_method
```

```
def is_triangular(number):
    result=0
    for i in range(number):        
        if result == number:
            break
        result += i
        if result > number:
            return False
    return True
```

```python
def is_triangular(num):
    return True if (((1+8*num)**0.5 - 1) / 2) == int((((1+8*num)**0.5 - 1) / 2)) else False
```

```python
def check_score(answer, mine):
    return max(0,sum([4 if a == m else -1 for a, m in list(zip(answer, mine)) ]))
```

```python
def check_score(answer, mine):
    return max(0,sum([4 if a == m else -1 for a, m in list(zip(answer, mine)) if m])) 빈스트링은('') false
```

max(0,x)

```
Docstring:
max(iterable, *[, default=obj, key=func]) -> value
max(arg1, arg2, *args, *[, key=func]) -> value

With a single iterable argument, return its biggest item. The
default keyword-only argument specifies an object to return if
the provided iterable is empty.
With two or more arguments, return the largest argument.
Type:      builtin_function_or_method
```

sorted(x)

집합의 요소를 정렬한 리스트를 return함.



### 재귀 함수(recursive function)

### recursive - 

divide&conquer== DP(Dynamic programming)

알고리즘 구현 중 dp에서 재귀적 구현이 사용된다.

- optimal substructure, 재귀적 구현이 가능한가.

```python
def recur()
	base case #종료조건
    recursive step #점점 작아지는 형태로 이루어진다
```

곱셈기준일 경우 항상 시작을 1로 하기.

팩토리얼 구하기

```python
def factorial(num):
    if num ==1 :
        return 1
    else:
        return num * factorial(num-1)
```

![팩톨팩톨](https://user-images.githubusercontent.com/52446416/61354150-7b6b9480-a8ac-11e9-9172-81a33e092e85.png)



![image-20200129145839151](C:\Users\multicampus\TIL\20200129_python_problem_.assets\image-20200129145839151.png)

첫번째 실행된 함수는 리턴값이 오기 전까지 끝나지 않는다. (나의 리턴값에 함수가 되어있으므로 모든 함수계산이 끝날 때 끝남.)





python sroted()

쪼개서 부분을 sort하고 합칠 때 다시 sort...

tim sort - 효율성이 좋다.

merge sort



컴퓨터의 문제 해결 방법 : 최적화, 시뮬레이션

모두 재귀적 방법이 사용된다.



![image-20200129174434733](C:\Users\multicampus\TIL\20200129_python_problem_recursive.assets\image-20200129174434733.png)

제곱근구하기

![image-20200129174434733](D:\Git\TIL\20200129_python_problem_recursive.assets\image-20200129174434733.png)





## tip

wolframalpa: 수식 풀어주는 사이트.



주피터노트북 에러

json에러해결

I would suggest looking into the raw `.ipnb` file using a text editor. You might be able to just find the error by having a quick look.

I have done this in the past and found there was a "diff" in there, resulting from a bad/unfinished Git conflict. Jupyter can't open a file in this state as the conflict basically leaves a syntax error in the JSON, which cannot then be parsed.

In my case, I was able to manually delete one of the parts - the notebook then opened as usual.

#### Example - it might look something like this:

```
 <<<<<<< HEAD:mergetest
 This is my third line
 =======
 This is a fourth line I am adding
 >>>>>>> 4e2b407f501b68f8588aa645acafffa0224b9b78:mergetest
```

So you would just delete one side of this, leaving for example:

```
 This is a fourth line I am adding
```

[Source of conflict example.](http://genomewiki.ucsc.edu/index.php/Resolving_merge_conflicts_in_Git)