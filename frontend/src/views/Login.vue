<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const username = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const handleLogin = async () => {
  try{
    const response = await axios.post('http://127.0.0.1:8000/auth/jwt/create/', {username : username.value, password : password.value})
    localStorage.setItem('access_token', response.data.access)
    router.push('/')
  } catch (err){
    console.error(err)
    error.value = 'Неверный логин или пароль'
  }
}
</script>

<template>
<div class="login-form">
  <h1>Авторизация</h1>
  <form @submit.prevent="handleLogin">
    <label for="username">Введите логин:</label>
    <input v-model="username" type="text" placeholder="Enter login" required id="username">
    <label for="password">Введите пароль:</label>
    <input v-model="password" type="password" placeholder="Enter password" required id="password">
    <span v-if='error' class="error">{{error}}</span>
    <button type="submit">Войти</button>
    <p>Нет аккаунта?<router-link to="/register"><a> Зарегистрироваться</a></router-link></p>
  </form>
</div>
</template>

<style scoped>
h1 {
  text-align: center;
}
.login-form {
  width: 50%;
  margin: 0 25%;
}
label{
  display: inline-block;
  font-size: 18px;
  margin-top: 20px;
  color: #555555;
}
input {
  width: 100%;
  padding: 10px 10px;
  border-radius: 5px;
  margin-top: 10px;
  border: 2px solid #b5b4b4;
}
button{
  color: white;
  background: orangered;
  padding: 10px 20px;
  margin-top: 20px;
  border: none;
  border-radius: 5px;
  font-size: 15px;
  cursor: pointer;
}
button:hover {
  background: #ff7941;
}
p {
  color: #555555;
  margin-top: 10px;
}
a {
  text-decoration: none;
  color: orangered;
}
span {
  font-weight: bold;
  color: #e30000;
  display: block;
  opacity: 75%;
}
</style>