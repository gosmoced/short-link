<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import api from "@/api.js";

const username = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

const handleLogin = async () => {
  try{
    const response = await api.post('/auth/jwt/create/', {username : username.value, password : password.value})
    localStorage.setItem('access_token', response.data.access)
    router.push('/')
  } catch (err){
    console.error(err)
    error.value = 'Неверный логин или пароль'
    setTimeout(()=>{
    error.value = ''
    },3000)
  }
}

</script>

<template>
<div class="login-form glass-card fade-in">
  <h1 class="title-gradient">Login</h1>
  <form @submit.prevent="handleLogin">
    <label for="username">Enter username:</label>
    <input v-model="username" type="text" placeholder="Enter login" required id="username">
    <label for="password">Enter password:</label>
    <input v-model="password" type="password" placeholder="Enter password" required id="password">
    <span v-if='error' class="error">{{error}}</span>
    <button type="submit">Sign in</button>
    <p>Don’t have an account?<router-link to="/register"><a> Sign Up</a></router-link></p>
  </form>
</div>
</template>

<style scoped>
.login-form {
  max-width: 500px;
  margin: 0 auto;
  padding: 40px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
}
h1 {
  text-align: center;
  background: #0f172a;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow:
    1px 1px 1px rgba(255, 255, 255, 0.8),
    -1px -1px 1px rgba(0, 0, 0, 0.18);
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
  margin-top: 10px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid #e2e8f0;
  font-size: 1rem;
  color: #334155;
  outline: none;
  transition: all 0.3s ease;
}
input:focus {
  border-color: #94a3b8;
  box-shadow: 0 0 0 4px rgba(226, 232, 240, 0.6);
  background: #ffffff;
}
button{
  color: white;
  padding: 10px 20px;
  margin-top: 20px;
  border: none;
  border-radius: 5px;
  font-size: 15px;
  cursor: pointer;
  font-weight: bold;
  background: linear-gradient(to right, #182442, #004baf);
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.2);
  transition: all 0.3s ease;
}
button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.3);
}
p {
  color: #555555;
  margin-top: 10px;
}
a {
  text-decoration: none;
}
span {
  font-weight: bold;
  color: #e30000;
  display: block;
  opacity: 75%;
  margin-top: 10px;
}

.fade-in {
  animation: fadeIn 0.8s ease-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

</style>