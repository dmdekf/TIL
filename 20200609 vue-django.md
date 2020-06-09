# 20200609 vue-django

- ajax요청(비동기요청)

![image-20200609101257196](C:\Users\peach\AppData\Roaming\Typora\typora-user-images\image-20200609101257196.png)

- cors : 교차 출처 리소스 공유

> 모든 사람이 읽어야 한다. 
>
> 브라우저가 친절하다.  브라우저가 막는다.
>
> 비동기 요청에 한해서는 다른곳에서의 요청은 받아주지 않는다.
>
> 응답의 헤더에 `Access-Control-Allow-Origin header`가 없을 경우.

![image-20200609101426281](C:\Users\peach\AppData\Roaming\Typora\typora-user-images\image-20200609101426281.png)

- cors 설치

  ```
  $ pip install django-cors-headers
  
  INSTALLED_APPS = [
      ...
      'corsheaders',
      ...
  ]
  
  MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
      ...
      'corsheaders.middleware.CorsMiddleware',
      'django.middleware.common.CommonMiddleware',
      ...
  ]
  
  
  ```

## vue add router

- API(application interface)

![image-20200609103613118](assets/image-20200609103613118.png)



![image-20200609102557120](assets/image-20200609102557120.png)

npm i axios



- login/signup



![image-20200609105407683](assets/image-20200609105407683.png)

- cookie

```
npm install --save vue-cookies
```



![image-20200609110202244](assets/image-20200609110202244.png)



![image-20200609114223231](assets/image-20200609114223231.png)

----

# Zoom

django-rest-auth



- 

```
vue create [project]
vue add router
npm i axios
npm install --save vue-cookies

npm run serve
```

---

# 오후

![image-20200609140706281](assets/image-20200609140706281.png)

- cookie를 공유하기 위해 데이터를 올려주었다. 
- 나의 선택지는...?

- 네비게이션 가드

### 프로젝트

- 맞춰해야 할 것을 정한다. - 규약..
  - API!!!! 가장 맞춰야 할 구간 : request, response 형태.
- 같이 일을 시작한다.











# tips

aws route 53으로 사서 시작하기.

