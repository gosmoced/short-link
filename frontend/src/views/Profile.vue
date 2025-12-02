<script setup>
import {ref, onMounted} from "vue";
import axios from "axios";
import {useRouter} from "vue-router";

const router = useRouter()
const email = ref('')
const login = ref('')
const error = ref('')
const message = ref('')
const newUsername = ref('')
const newEmail = ref('')
const Password = ref('')
const PasswordVisible = ref(false)
const isLoading = ref(false)

const getToken = () => localStorage.getItem('access_token')

onMounted(async () => {
  const token = getToken()
  if(!token) {
    router.push('/login')
    return
  }
  try {
    const response = await axios.get('http://127.0.0.1:8000/auth/users/me/', {
      headers: {
        'Authorization' : `Bearer ${token}`
      }
    })
    login.value = response.data.username
    email.value = response.data.email
    newUsername.value = response.data.username
    newEmail.value = response.data.email

  } catch (err) {
    console.log(err)
    error.value = 'Не удалось загрузить профиль'
  }
})
const updateProfile = async () => {
  error.value = ''
  const token = getToken()

  if(login.value === newUsername.value && email.value === newEmail.value) {
    message.value = 'Нет изменений'
    setTimeout(() => {
      message.value = ''
    }, 3000)
    return
  }

  isLoading.value = true

  try {
    if(newEmail.value !== email.value){
      const response = await axios.patch('http://127.0.0.1:8000/auth/users/me/', {
      email: newEmail.value},
         {
      headers: {
        'Authorization': `Bearer ${token}`},
         })
      email.value = response.data.email}

    if(login.value !== newUsername.value){
      if(!Password.value){
        PasswordVisible.value = true
        error.value = 'Для смены логина требуется ввести пароль.'
        return
      }
      await axios.post('http://127.0.0.1:8000/auth/users/set_username/', {
          new_username: newUsername.value,
          current_password: Password.value},
            {headers: {
              'Authorization' : `Bearer ${token}`
              }})
      login.value = newUsername.value
      Password.value = ''
    }
    message.value = 'Данные успешно обновлены'
    PasswordVisible.value = false
    setTimeout(() => {
      message.value = ''
    }, 3000)

  } catch (err){
    console.error(err)
    if (err.response && err.response.data) {
      const serverData = err.response.data
      const errorMessages = []

      for (const key in serverData) {
        const errorText = serverData[key][0]
        errorMessages.push(`${key}: ${errorText}`)
      }

      error.value = errorMessages.join(' ')
    }
  } finally {
    isLoading.value = false
  }
}
const exitProfile = () => {
  localStorage.removeItem('access_token')
  router.push('/login')
}

</script>

<template>
  <div class="profile">
    <h1>Кабинет пользователя</h1>
    <p><b>@{{login}}</b></p>
    <p><b>Email: </b>{{email}}</p>
    <button @click="exitProfile()" class="logout">Выйти из аккаунта</button>
  </div>

  <div class="update-form">
    <h2>Изменить данные пользователя</h2>
    <form @submit.prevent="updateProfile">
      <label for="login">Имя пользователя:</label>
      <input type="text" id="login" v-model="newUsername">
      <label for="email">Почта:</label>
      <input type="email" id="email" v-model="newEmail">
      <div v-if="PasswordVisible">
        <label for="password">Пароль:</label>
        <input type="password" id="password" v-model="Password">
      </div>
      <p class="message">{{message}}</p>
      <span>{{error}}</span>
      <button :disabled="isLoading">{{isLoading ? 'Сохраняем...' : 'Обновить данные'}}</button>
    </form>
  </div>
</template>

<style scoped>
h1 {
  margin-bottom: 30px;
}
h1, h2 {
  text-align: center;
}
.update-form, .profile {
  width: 50%;
  margin: 0 25%;
}
.profile {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 40px;
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