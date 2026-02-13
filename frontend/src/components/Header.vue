<script setup>
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
  <div>
    <p class="logo">ShortLink</p>
  </div>
  <div class="nav">
    <router-link to="/">Home</router-link>
    <span v-if="isAuth">
      <router-link to="/profile">Profile</router-link>
      <router-link to="/link">Links</router-link>
    </span>
    <span v-else>
      <router-link to="/login">Login</router-link>
      <router-link to="/register">Sign up</router-link>
    </span>
  </div>
</header>
</template>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 30px 0;
}
a {
  display: inline-block;
  color: #707070;
  border: none;
  font-size: 20px;
  text-decoration: none;
  transition: all 0.3s ease;
  margin-left: 15px;
}
a:hover{
  color: #0f172a;
  transform: scale(1.1)
}

.logo{
  font-size: 40px;
  font-weight: bold;
  background: linear-gradient(to right, #182442, #004baf);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
@media (max-width: 768px) {
  .logo {
    font-size: 30px;
  }
}
</style>