<script setup>
import axios from "axios";
import {ref} from "vue";
import {useRouter} from "vue-router";

const router = useRouter()

const username = ref('')
const email = ref('')
const password = ref('')
const error = ref('')

const handleRegister = async () => {
  try {
    await axios.post('http://127.0.0.1:8000/auth/users/', {'username':username.value, 'email':email.value, 'password':password.value})
    router.push('/login')
    alert('Вы успешно зарегистрированы')
  } catch (err) {
    console.error(err)

    if (err.response && err.response.data) {
      const serverData = err.response.data
      const errorMessages = []

      for (const key in serverData) {
        const errorText = serverData[key][0]
        errorMessages.push(`${key}: ${errorText}`)
      }

      error.value = errorMessages.join(' ')

    } else {
      error.value = 'Произошла ошибка'
    }
  }
}

</script>
<template>
  <div class="register-form">
    <h1>Регистрация на сайте</h1>
    <form @submit.prevent="handleRegister">
      <label for="username">Введите логин:</label>
      <input v-model="username" placeholder="Enter login" id="username">
      <label for="email">Введите почту:</label>
      <input v-model="email" type="email" placeholder="Enter email" id="email">
      <label for="password">Введите пароль:</label>
      <input v-model="password" type="password" placeholder="Enter password" id="password">
      <span class="error">{{error}}</span>
      <button>Зарегистрироваться</button>
    </form>
    <p>Уже зарегистрированы?<router-link to="/login"><a> Войти</a></router-link></p>
  </div>
</template>

<style scoped>
h1 {
  text-align: center;
}
.register-form {
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