<script setup>
import {ref, onMounted} from "vue";
import {useRouter} from "vue-router";
import axios from "axios";

const url = ref('')
const title = ref('')
const error = ref('')
const links = ref([])
const router = useRouter()

onMounted(() => {
  const token = localStorage.getItem('access_token')
  if (!token) {
    router.push('/login')
    return
  }
  fetchLinks()
})

const fetchLinks = async () => {
  const token = localStorage.getItem('access_token')
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/get-link/', {
      headers: {
        'Authorization' : `Bearer ${token}`
      }
    })
    links.value = response.data
  } catch (err){
    error.value = ''
  }
}

const CreateLink = async () => {
  const token = localStorage.getItem('access_token')
  try {
    await axios.post('http://127.0.0.1:8000/api/create/', {
      url : url.value,
      title: title.value
    }, {headers: {
      'Authorization': `Bearer ${token}`
      }} )
    await fetchLinks()
    title.value = ''
    url.value = ''
  }catch(err){
    error.value = 'Ошибка создания'
  }
}

const deleteLink =  async (id) => {
  const token = localStorage.getItem('access_token')

  try {
    await axios.delete(`http://127.0.0.1:8000/api/delete-link/${id}/`, {
      headers: {
        'Authorization' : `Bearer ${token}`
      }
    })
    await fetchLinks()
  } catch (err) {
    error.value = 'Ошибка удаления'
  }
}

</script>


<template>
  <div>
    <h1>Создание ссылок</h1>
    <form @submit.prevent="CreateLink" class="get-form">
      <label for="title">Название:</label>
      <input v-model="title" id="title">
      <label for="url">URL:</label>
      <input v-model="url" type="url" id="url">
      <span class="error">{{ error }}</span>
      <button>Сохранить</button>
    </form>
  </div>
  <div v-if="links.length !== 0" class="view-link">
    <h2>Доступные ссылки</h2>
    <div v-for="link in links" :key="link.id" class="link-wrapper">
      <p class="link">Ссылка - <a :href='link.url'>/link/{{ link.title }}</a></p>
      <button @click="deleteLink(link.id)" class="delete">❌</button>
    </div>
  </div>
  <div v-else>
    <h1>У вас пока нет ссылок</h1>
  </div>
</template>

<style scoped>
h1, h2 {
  text-align: center;
}
h2 {
  margin-bottom: 20px;
}
.get-form, .view-link {
  width: 50%;
  margin: 0 25%;
}
.get-form {
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
button:not(.delete){
  color: white;
  background: orangered;
  padding: 10px 20px;
  margin-top: 20px;
  border: none;
  border-radius: 5px;
  font-size: 15px;
  cursor: pointer;
}
button:not(.delete):hover {
  background: #ff7941;
}
.delete{
  background: none;
  border: none;
  cursor: pointer;
}
p {
  font-size: 18px;
  color: #707070;
}
p:not(.link) {
  margin-top: 30px;
}
p a {
  color: orangered;
  text-decoration: none;
}
span {
  font-weight: bold;
  color: #e30000;
  display: block;
  opacity: 75%;
}
.link-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
}
</style>