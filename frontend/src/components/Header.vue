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
    <router-link to="/">Главная</router-link>
    <span v-if="isAuth">
      <router-link to="/profile">Профиль</router-link>
      <router-link to="/link">Ссылки</router-link>
    </span>
    <span v-else>
      <router-link to="/login">Войти</router-link>
      <router-link to="/register">Регистрация</router-link>
    </span>
  </div>

</header>
</template>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
a {
  display: inline-block;
  color: #707070;
  border: none;
  font-size: 20px;
  text-decoration: none;
  transition: all 0.3s ease;
  margin-left: 20px;
}
a:hover{
  color: #0f172a;
  transform: scale(1.1)
}

img {
  width: 90px;
  height: auto;
}
@media (max-width: 768px) {
  img {
    width: 60px;
    height: auto;
  }
}
</style>