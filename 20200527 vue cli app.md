# 20200527 vue cli

- node : 환경이다.

```
npm install -g @vue/cli

vue create first_vuecli
default
npm -> yarn으로 대체 가능.
npm run serve
npm run build
```



- .vue file 구성.

  - <template>
        
    </template>

  - <script>
        
    </script>

  - <style>
        
    </style>



```
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

```

- App.vue

```html
<template>
  <div id="app">
    // 3. component를 쓴다.
    <MyComponent></MyComponent>
    <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
 // 1. import 꺼내온다.
import HelloWorld from "./components/HelloWorld.vue";
import MyComponent from "./components/MyComponent.vue";
export default {
  name: "App",
  components: {
    // 2. component에 등록한다.
    HelloWorld,
    MyComponent
  }
};
</script>

<style>
</style>
```

- component는 하나의 element만을 사용한다.

