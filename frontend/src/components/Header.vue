<script setup>
import logo from '../assets/img.png';
import {ref, onMounted, watch} from "vue";
import {useRoute} from "vue-router";

const route = useRoute()
const isAuth = ref(false)

const checkAuth = () => {
  const token = localStorage.getItem('access_token')
  isAuth.value = !!token
}

onMounted(() => {
  checkAuth()
})

watch(route, () => {
  checkAuth()
})
</script>

<template>
<header>
  <img :src="logo" alt="">
  <div>
    <router-link to="/"><a>Главная</a></router-link>
    <span v-if="isAuth">
      <router-link to="/profile"><a>Профиль</a></router-link>
      <router-link to="/link"><a>Ссылки</a></router-link>
    </span>
    <span v-else>
      <router-link to="/login"><a>Войти</a></router-link>
      <router-link to="/register"><a>Регистрация</a></router-link>
    </span>
  </div>

</header>
</template>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
a {
  color: #707070;
  border: none;
  font-size: 20px;
  text-decoration: none;
}
a:hover{
  color: #53a2da;
}
a:not(:last-child) {
  margin-right: 20px;
}
img {
  width: 130px;
  height: auto;
}
</style>