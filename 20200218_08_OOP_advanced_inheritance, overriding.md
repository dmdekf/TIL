# 20200218

## python

###  08_OOP_advanced

#### 상속 중요~! `재사용`이 가능하게 한다.

**부모 클래스의 모든 속성이 자식 클래스에게 상속 **

class

attribute-속성(data,value), method

```
issubclass(하위, 상위) # subclass <->?superclass
issubclass(Parent, Person) 
issubclass(bool, int) #True 
issubclass(int, float) 
-------------------
True
True
Flase(숫자간은 상속관계 x)
```

#### super()

부모 클래스의 내용을 사용하고 할 때.

```pyth
class Person:
    def __init__(self, name, age, birthday, email):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.email = email
        
    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')

class Student(Person):
    #부모클래스(Person) 
    def __init__(self, name, age, birthday, email, student_id, grade):
        super().__init__(name, age, birthday, email)
        self.student_id = student_id
        self.grade = grade
```

#### overriding 메서드 오버라이딩 

- namelookup

> 인스턴스 -> 자식 클래스 -> 부모 클래스 -> 전역

##### 다중상속 -> 같은 attribute가 있을 경우 상속받을 클래스 우선수위가 앞인 경우를 상속.

```
class FirstChild(Mom, Dad):  -->class Mom(Person):gene = 'XX'을 받음.
    
    def sleep(self):
        print('새근새근')
    
    def cry(self):
        print('응애')
```





## tip





