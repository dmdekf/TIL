# 20200217

## python - OOP advanced

클래스 변수

값이 복제되지 않았다.

공간상의 공유가 아닌 name lookup으로 처리.

인스턴스의 어트리뷰트와 클래스 어트리뷰트는 독립적이다.

```python
# 인스턴스 => 클래스 => 전역 순서로 이름공간을 탐색하기 때문에, 접근하게 됩니다.
```

```
class TestClass:

    class_variable = '클래스 변수'
    

print(TestClass.class_variable)  # '클래스 변수'
TestClass.class_variable = 'class variable'
print(TestClass.class_variable)  # 'class variable'

tc = TestClass() # 인스턴스로 클래스 변수에 접근 가능.
print(tc, tc.class_variable)  
tc.class_variable = '변경' # 인스턴스만의 값 생성.
print(tc, tc.class_variable)  
print(TestClass.class_variable)
tc1 = TestClass()
print(tc1.class_variable)
-------------------
클래스 변수
class variable
<__main__.TestClass object at 0x000002584B93B400> class variable
<__main__.TestClass object at 0x000002584B93B400> 변경
class variable
class variable
```

#### 인스턴스 메서드 - self

#### 클래스 메서드 -클래스 사용 권장.

##### 클래스가 사용 or 인스턴스들이 공유하는 메서드

#### 스태틱(정적) 메서드 - 클래스 사용 권장. - 데이터와 무관. 클래스를 단순히 이름공간으로 사용.

```
class Car:
    @classmethod
    def park(cls):
        print('멈춤')
    
    #sudo constructor(초기화에 가깝다. __new__가 생성자 .)
    def __init__(self,name):
        self.name = name
    
    def drive(self):
        print('부릉부릉')
    
    @staticmethod
    def wash():
        print('쓱싹')

Jeep = Car('Jeep')
Jeep.drive()
Jeep.park()
Car.park()
Car.wash()
Jeep.wash()
---------------------------
class MyClass:
    def instance_method(self):
        return self
    
    @classmethod
    def class_method(cls):
        return cls
    
    @staticmethod
    def static_method():
        return 'empty'
```



#### 정리

##### 정리 1 - 인스턴스와 메서드

- 인스턴스는, 3가지 메서드 모두에 접근할 수 있다.
- 하지만 인스턴스에서 클래스 메서드와 스태틱 메서드는 호출하지 않아야 한다. (가능하다 != 사용한다)
- 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계한다.

##### 정리 2 - 클래스와 메서드

- 클래스는, 3가지 메서드 모두에 접근할 수 있다.
- 하지만 클래스에서 인스턴스 메서드는 호출하지 않다. (가능하다 != 사용한다)
- 클래스가 할 행동은 다음 원칙에 따라 설계한다.
  - 클래스 자체(`cls`)와 그 `속성에 접근할 필요가 있다`면 클래스 메서드로 정의한다.
  - 클래스와 클래스 속성에 접근할 필요가 없다면 스태틱 메서드로 정의한다.
    - @staticmethod 데코레이터가 없는 함수의 경우 파이썬은 인스턴스 자체를 첫번째 인자로 인식한다. (self)

