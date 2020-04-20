# SQL과 django ORM 비교

## 참고문서

[Making queries | Django documentation | Django](https://docs.djangoproject.com/en/2.2/topics/db/queries/#making-queries)

[QuerySet API reference | Django documentation | Django](https://docs.djangoproject.com/en/2.2/ref/models/querysets/#queryset-api-reference)

[Aggregation | Django documentation | Django](https://docs.djangoproject.com/en/2.2/topics/db/aggregation/#aggregation)

## **기본 준비 사항**

> Gitlab에서 프로젝트를 다운받으면 아래의 내용이 이미 반영되어 있습니다.

- django app
    - `django_extensions` 설치
    - `users` app 생성
    - csv 파일에 맞춰 `models.py` 작성 및 migrate

            $ python manage.py sqlmigrate users 0001

- `db.sqlite3` 활용 및 데이터 반영
    - `sqlite3` 실행

            $ ls
            db.sqlite3 manage.py ...
            $ sqlite3 db.sqlite3

    - csv 파일 data 로드

            sqlite > .tables
            auth_group                  django_admin_log
            auth_group_permissions      django_content_type
            auth_permission             django_migrations
            auth_user                   django_session
            auth_user_groups            auth_user_user_permissions
            users_user
            sqlite > .mode csv
            sqlite > .import users.csv users_user
            sqlite > SELECT COUNT(*) FROM users_user;
            1000

- 확인
    - sqlite3에서 스키마 확인

            sqlite > .schema users_user
        
        
        ​    

## **문제**

> 아래의 문제들을 sql문과 대응되는 orm을 작성 하세요.

### Table 생성

- django

    ```python
    # django
    class User(models.Model):
        first_name = models.CharField(max_length=10)
        last_name = models.CharField(max_length=10)
        age = models.IntegerField()
        country = models.CharField(max_length=10)
        phone = models.CharField(max_length=15)
        balance = models.IntegerField()
    ```

- SQL
    - sql.sqlite3에 동일하게 테이블 생성

        ```sql
        --sql
        CREATE TABLE "users_user" (
            "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
            "first_name" varchar(10) NOT NULL, 
            "last_name" varchar(10) NOT NULL, 
            "age" integer NOT NULL, 
            "country" varchar(10) NOT NULL, 
            "phone" varchar(15) NOT NULL, 
            "balance" integer NOT NULL);
        
        .read users_user.sql
        ```

### 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   users = User.objects.all()
   print(users.query)
   ```

      ```sql
   -- sql
   SELECT * FROM users_user
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objets.create(
   	first_name='구름',
       last_name='김',
       age=100,
       country='제주도',
       phone='010-000-0000',
       balance=100000000
   )
   ```

   ```sql
   -- sql
   INSERT INTO users_user ('first_name','last_name','age','country','phone','balance')
   VALUES ('근제','성',80,'서울','011-0000-0000',10000)
   
   INSERT INTO users_user ('first_name')
   VALUES ('근제')
   
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

   * ```bash
     NOT NULL constraint failed
     ```

3. 해당 user 레코드 조회

   > **get 쿼리 결과가 반드시 하나여야 한다.**
   >
   > **특정한 값이 여러개일 경우 오류. MultipleObjectsReturned,**
   >
   > ##### DoesNotExist : 없을 경우

   ```python
   # orm
   #get 쿼리 결과가 반드시 하나여야 한다.
   # 특정한 값이 여러개일 경우 오류. MultipleObjectsReturned,
   # DoesNotExist : 없을 경우
   User.objects.get(id=100)
   ```

   ```sql
   -- sql
   SELECT * FROM users_user WHERE id =100
   ```

4. 해당 user 레코드 수정

   > query.set 만 print(user.query)가능!!!!!!!!!!

   ```python
   # orm
   user = User.objects.get(id=100)
   user.last_name = '성'
   user.save()
   ```

   ```sql
   -- sql
   UPDATE users_user 
   SET last_name='최'
   WHERE id=100;
   ```

5. 해당 user 레코드 삭제

   ```python
   # orm
   user = User.objects.get(id=100).delete()
   ```

      ```sql
   -- sql
   DELETE FROM users_user WHERE id=101;
      ```

### 조건에 따른 쿼리문

1. 전체 인원 수

   ```python
   # orm
   User.objects.all().count()
   User.objects.count()
   # USer.objects.count().query() => 오류남. 인티져이기때문에. 쿼리셋이아닌.
   ```

      ```sql
   -- sql
   SELECT COUNT(* or id....) FROM users_user;
      ```

2. 나이가 30인 사람의 이름

   ```python
   # orm
   #Queryset으로 모든 오브젝트 리턴.
   User.objects.filter(age=30)
   
   #딕셔너리로 리턴.
   User.objects.filter(age=30).values('first_name')
    <QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': '은영'}]>
       
   #쿼리문 비교 print(User.objects.filter(age=30).values('first_name').query)                                                            
   SELECT "users_user"."first_name" FROM "users_user" WHERE "users_user"."age" = 30
   ```

      ```sql
   -- sql
   SELECT first_name FROM user_user 
   WHERE age=30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   > 대소관계
   >
   > `__gte` : >=
   >
   > `__gt` : >
   >
   > `__lte` : <=
   >
   > `__lt`: <

   ```
   # orm
   User.objects.filter(age__gte=30)
   User.objects.filter(age__gte=30).count()
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM user_user 
   WHERE age>=30;
   ```

4. 나이가 30이면서 성이 김씨인 사람의 인원 수

   > orm : (`iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith` and `iendswith`)

   ```django
   # orm
   #1.메서드체이닝(메서드를 점으로...)queryset
   User.objects.filter(age=30).filter(last_name='김').count()
   #2.
   User.objects.filter(age=30,last_name='김').count()
   
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM users_user 
   WHERE age=30 AND last_name = '김';
   ```

5. 지역번호가 02인 사람의 인원 수

   > https://docs.djangoproject.com/en/2.2/topics/db/queries/#escaping-percent-signs-and-underscores-in-like-statements

   ```python
   # orm
   User.objects.fliter(phone__startswith='02-').count()
   ```

      ```sql
   -- sql
   SELECT COUNT(*) FROM users_user 
   WHERE phone LIKE '02-%'; 
      ```

6. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   ```

      ```sql
   -- sql
   SELECT last_name FROM users_user
   WHERE 
      ```



### 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람 10명(내림차순)

   ```python
   # orm
   User.objects.order_by('-age')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user
   ORDER BY age DESC 
   LIMIT 10;
      ```

2. 잔액이 적은 사람 10명(오름차순)

   ```python
   # orm
   User.objects.order_by('balance')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user
   ORDER BY balance ASC(default)
   LIMIT 10;
      ```

3. 성, 이름 내림차순 순으로 5번째 있는 사람:star::star::star:

      ```python
   # orm
   User.objects.order_by('-last_name','-first_name')[4]
   ```
```
   
      ```sql
   -- sql
   SELECT * FROM users_user
   ORDER BY last_name DESC, first_name DESC
   LIMIT 1 OFFSET 4;
```



### 표현식

> 표현식을 위해서는 [aggregate]([https://docs.djangoproject.com/en/2.2/topics/db/aggregation/](https://docs.djangoproject.com/en/2.2/topics/db/aggregation/)) 를 알아야한다.
>
> ```bash
> # Shell Plus Django Imports
> from django.core.cache import cache
> from django.conf import settings
> from django.contrib.auth import get_user_model
> from django.db import transaction
> from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
> from django.utils import timezone
> from django.urls import reverse
> ```
>
> 

1. 전체 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   User.objects.aggregate(Avg('age'))
   
   
   In [5]: User.objects.aggregate(Avg('age'))                                                                                       
   Out[5]: {'age__avg': 28.23}
   
   ```

      ```sql
   -- sql
   SELECT ABE(age) FROM users_user;
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   from django.db.models import Avg
   User.objects.filter(last_name='김').aggregate(Avg('age'))
   
   User.objects.filter(last_name='김').aggregate(Avg('age'))                                                                
   Out[6]: {'age__avg': 28.782608695652176}
   ```

      ```sql
   -- sql
   SELECT ABE(age) FROM users_user
   WHERE last_name='김';
      ```

3. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   from django.db.models import Max
   User.objects.aggregate(Max('balance'))
   
   In [8]: User.objects.aggregate(Max('balance'))                                                                                   
   Out[8]: {'balance__max': 1000000}
   ```

      ```sql
   -- sql
   SELECT MAX(balance) FROM users_user;
      ```

4. 계좌 잔액 총액

      ```python
   # orm
   from django.db.models import Sum
User.objects.aggregate(Sum('balance'))
   
   
   In [10]: User.objects.aggregate(Sum('balance'))                                                                                  
   Out[10]: {'balance__sum': 14425040}
   
   ```
   
      ```sql
   -- sql
   SELECT SUM(balance) FROM users_user;
      ```



### Group by

> annotate는 개별 item에 추가 필드를 구성한다.
> 추후 1:N 관계에서 활용된다.
>
> annotate : 개별 아이템에 주석을 달다.

1. 지역별 인원 수

   ```python
   # orm
   User.objects.values('country')

   In [11]: User.objects.values('country')                                                                                          
   Out[11]: <QuerySet [{'country': '전라북도'}, {'country': '경상남도'}, {'country': '전라남도'}, {'country': '충청남도'}, {'country': '충청북도'}, {'country': '충청북도'}, {'country': '경기도'}, {'country': '충청북도'}, {'country': '제주특별자치도'}, {'country': '충청남도'}, {'country': '제주특별자치도'}, {'country': '충청남도'}, {'country': '전라북도'}, {'country': '전라남도'}, {'country': '경상북도'}, {'country': '경상남도'}, {'country': '충청남도'}, {'country': '충청북도'}, {'country': '충청남도'}, {'country': '경기도'}, '...(remaining elements truncated)...']>
       
   from django.db.models import Count
   User.objects.values('country').annotate(Count('country'))
   
   In [12]: User.objects.values('country').annotate(Count('country'))                                                               
   Out[12]: <QuerySet [{'country': '강원도', 'country__count': 14}, {'country': '경기도', 'country__count': 9}, {'country': '경상남 도', 'country__count': 9}, {'country': '경상북도', 'country__count': 15}, {'country': '전라남도', 'country__count': 10}, {'country': '전라북도', 'country__count': 11}, {'country': '제주특별자치도', 'country__count': 9}, {'country': '충청남도', 'country__count': 9}, {'country': '충청북도', 'country__count': 14}]>
   ```
   
   ```sql
   -- sql
   SELECT country, COUNT(country) FROM users_user
   GROUP BY country;
   ```

