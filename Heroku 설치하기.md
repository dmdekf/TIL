1. DEBUG

   우리 실제 서버를 돌렸을 때, 에러 메시지를 띄웠던 DEBUG 기능을 꺼야한다.

   이 기능이 켜져있는 상태에서 배포하면,

   누군가가 들어와서 뚜둘려줄지도 모른다,,

   ```python
   # settings.py
   # SECURITY WARNING: don't run with debug turned on in production!
   DEBUG = True
   ```

   를

   ```python
   # SECURITY WARNING: don't run with debug turned on in production!
   # DEBUG = True
   DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )
   ```

   로 바꿔주자.

2. SECRET_KEY

   CRSF 보안 등을 위해 사용되는 큰 숫자의 랜덤값이다.

   이게 털리면 서버가 비밀리에 간직해야되는 정보의 암호화가 무용지물이 된다.

   ```python
   # settings.py
   # SECURITY WARNING: keep the secret key used in production secret!
   SECRET_KEY = '(p7p0#$^HHFGHHdggtherververvewkjbnp3290vdvfd)w'
   ```

   를

   ```python
   # settings.py
   # SECURITY WARNING: keep the secret key used in production secret!
   # SECRET_KEY = '(p7p0#$^HHFGHHdggtherververvewkjbnp3290vdvfd)w'
   # SECURITY WARNING: keep the secret key used in production secret!
   import os
   SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '(p7p0#$^HHFGHHdggtherververvewkjbnp3290vdvfd)w')
   ```

   로 바꿔주자.

 

## Heroku 설치하기

1. [https://www.heroku.com](https://www.heroku.com/)

   여기서 회원가입을 진행하자.

2. https://devcenter.heroku.com/articles/getting-started-with-python

   그리고 이 주소에서 배포를 연습할 수 있다.

   먼저 setup만 해주자.

   본인에게 해당되는 운영체제를 선택해 설치하자.

   ![2019-03-05 2 15 28](https://user-images.githubusercontent.com/37871541/53782549-22304380-3f51-11e9-82a8-23912aa11063.png)

 

## Github repository에 저장하기

앞 강의를 들었으면, github 아이디는 있을 거라 생각하고 진행하겠다.

1. 먼저 repository 부터 만들어보자.

2. 그럼 업로드하기 위해서, `.gitignore` 파일을 만들어야되는데,

   이 파일은 `manage.py` 파일이 있는 폴더에 만들어야 한다.

   이 부분이 생각이 안나면,

   [[[Django\] Week 2.5_2 Git 실습](https://egg-money.tistory.com/97)](https://egg-money.tistory.com/97?category=811218)

   이 부분을 참고하자.

3. `.gitignore` 파일 안에 이렇게 넣어주자.

   ```python
   # .gitignore
   ### Django ###
   *.log
   *.pot
   *.pyc
   __pycache__/
   local_settings.py
   db.sqlite3
   media
   ```

4. 여기까지 했으면, github 에 push까지 진행해보자.

   ```shell
   $ git init
   $ git add .
   $ git status
   $ git commit -m "first commit"
   $ git remote add origin https://github.com/wansook0316/heroku_upload.git
   $ git push -u origin master 
   ```

 

## Heroku에 올리기 위한 작업

### Procfile 작성

하, 이파일 설명하기가 너무 힘들다.

일단은 그냥 만들어야 하는 파일이라고 생각하자.

이것도 역시 `manage.py` 가 있는 위치에 만들자.

```
web: gunicorn secondproject.wsgi --log-file -
```

중간에 secondproject 는 프로젝트 이름이다.

 

### Unicorn 설치하기

```shell
$ pip install gunicorn
```

 

### Database 설정하기

앞서 개발에서는 sqlite가 기본으로 설정되어 있었지만 heroku에서는 사용할 수 없다.

그 이유는 복잡한데, heroku가 postgresql 를 기본 옵션으로 하고 있기 때문이라고만 생각하고 넘어가자.

그전에 무언가 설치해줘야한다.

```shell
$ pip install dj-database-url
$ pip install psycopg2-binary
```

 

그 다음에, `settings.py` 맨하단에 아래 내용을 붙여넣기 하자.

```python
# settings.py
# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
```

 

### Static file 을 위한 설정하기

```shell
$ pip install whitenoise
```

설치한 후에 `settings.py` 로 가서 MIDDLEWEAR 설정에서

SecurityMiddleware 위에 WhiteNoiseMiddleware 를 추가하자.

```python
# settings.py
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

이 만큼을 **추가** 하는 거다.

 

### 파이썬 관련 라이브러리를 서버에 설치하기

앞에서 pip install 을 통해 여러가지를 설치했는데,

이 설치한 내용을 호스팅할 서버에서도 설치해줘야한다.

그렇기 떄문에 이 리스트를 업로드 해줘야 한다.

```shell
$ pip freeze > requirements.txt
```

 

### heroku에게 python 버전을 알려주자

우리가 만든 프로젝트의 python 버전을 heroku 에게 알려줘야 충돌을 줄일 수 있다.

`runtime.txt` 라는 파일을 만들고 안에 python 버전을 적어주자.

파이썬 버전을 알려주는 명령어는,

```shell
$ python --version
```

이다.

그리고 최상위 폴더에 `runtime.txt` 를 만들어주자.

```
# runtime.txt

python-3.7.1
```

해당 부분은 내 파이썬 버전을 입력해준다.

 

마지막으로 다시 github에 푸시해주자.

```shell
$ git init
$ git add .
$ git status
$ git commit -m "heroku edited"
$ git remote add origin https://github.com/wansook0316/heroku_upload.git 이 부분은 없어도된다.
$ git push -u origin master 
```

 

 

## Heroku 만들기

여기까지 잘했다면 이제 Heroku를 만들어보자.

```shell
$ heroku login
```

그러면 이런 창이 뜬다.

![2019-03-05 5 27 42](https://user-images.githubusercontent.com/37871541/53791138-fcfcfe80-3f6b-11e9-9c6c-297c0c1388c2.png)

 

일단 로그인 해준다.

로그인후 뜨는 창을 보면, 이런창이 뜰텐데,

결국 이 사이트에 들어와서 내가 GUI 기반으로 앱을 만들 수 있는 거다.

![2019-03-05 5 31 47](https://user-images.githubusercontent.com/37871541/53791353-8f050700-3f6c-11e9-8273-adc39520f579.png)

우리는 기존에 내가 만든 앱을 바로 올리고 싶은 거니까

터미널 창에서 해보자.

 

이제 다음 명령어를 쳐보자.

```shell
$ heroku create 
$ heroku create 저장소이름
```

 

그러면 앱이 생성되고, (이건 GUI 기반으로도 할 수 있다.)

 

모든 사항을 수정한 것이 github 에 올라간것이 확인되면,

```shell
$ git push heroku master
```

 

이 때, 만약 앱을 삭제해 버렸다면,

```shell
$ heroku git:remote -a 헤로쿠 앱 이름
```

 

이렇게 써주면 잘 푸시 된다.

 

이렇게 하고

[헤로쿠 홈페이지](https://egg-money.tistory.com/heroku.com)

들어가면,

![2019-03-05 9 54 51](https://user-images.githubusercontent.com/37871541/53806803-4f044b00-3f91-11e9-8153-2b9722844abb.png)

잘 뜬다! 이러면 웹을 올린 거다!

 

그런데 이건 푸시만 한거고, heroku 에는 migrate 가 안되어 있으니,

```shell
$ heroku run python manage.py migrate
```

 

자, 이제 내가 올린 페이지를 열어보자

```shell
$ heroku open
```

 



 

푸시를 하면서 예전에 만들었던 DB, superuser 다 없어졌으니까,

```shell
$ heoku run python manage.py createsuperuser
```

 



출처: https://egg-money.tistory.com/115 [완숙의 에그머니]