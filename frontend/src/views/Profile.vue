<script setup>
import {ref, onMounted} from "vue";
import {useRouter} from "vue-router";
import api from "@/api.js";

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
    const response = await api.get('/auth/users/me/', {
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
      const response = await api.patch('/auth/users/me/', {
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
      await api.post('/auth/users/set_username/', {
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
      setTimeout(()=>{
      error.value=''
      },3000)
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
  <div class="profile fade-in">
    <h1>User Dashboard</h1>
    <p><b>@{{login}}</b></p>
    <p><b>Email: </b>{{email}}</p>
    <button @click="exitProfile()" class="logout">Log Out</button>
  </div>

  <div class="update-form fade-in">
    <h2>Edit User Information</h2>
    <form @submit.prevent="updateProfile">
      <label for="login">Username:</label>
      <input type="text" id="login" v-model="newUsername">
      <label for="email">Email:</label>
      <input type="email" id="email" v-model="newEmail">
      <div v-if="PasswordVisible">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="Password">
      </div>
      <p class="message">{{message}}</p>
      <span>{{error}}</span>
      <button :disabled="isLoading">{{isLoading ? 'Saving...' : 'Update Information'}}</button>
    </form>
  </div>
</template>

<style scoped>
h1, h2 {
  text-align: center;
  background: #0f172a;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow:
    1px 1px 1px rgba(255, 255, 255, 0.8),
    -1px -1px 1px rgba(0, 0, 0, 0.18);
}
h2 {
  margin-top: 30px;
}
h1 {
  margin-bottom: 30px;
}
.update-form, .profile {
  max-width: 500px;
  margin: 0 auto;
  padding: 40px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
}
.profile {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;
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
  color: orangered;
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
@media (max-width: 426px){
  .profile{
    padding: 40px 15px;
  }
}
</style>