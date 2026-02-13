<script setup>
import {ref, onMounted} from "vue";
import {useRouter} from "vue-router";
import api from "@/api.js";

const error = ref('')
const links = ref([])
const router = useRouter()
const siteUrl = import.meta.env.DEV
  ? 'http://127.0.0.1:8000'
  : 'https://gosmoced.pythonanywhere.com';

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
    const response = await api.get('api/get-link/', {
      headers: {
        'Authorization' : `Bearer ${token}`
      }
    })
    // Добавляем поле showHistory каждому объекту, чтобы Vue мог его отслеживать
    links.value = response.data.map(link => ({
      ...link,
      showHistory: false
    }))
  } catch (err){
    error.value = 'Ошибка загрузки ссылок'
  }
}
const toggleHistory = (targetLink) => {
  links.value.forEach(link => {
    if (link.id === targetLink.id) {
      link.showHistory = !link.showHistory
    }
    else {
      link.showHistory = false
    }
  })
}


const copyLink = (title) => {
  const url = `${siteUrl}/link/${title}`
  navigator.clipboard.writeText(url)
    .then(() => {
       alert('Ссылка скопирована!')
    })
    .catch(err => {
      console.error('Failed to copy: ', err)
    })
}

const deleteLink =  async (id) => {
  const token = localStorage.getItem('access_token')

  try {
    await api.delete(`/api/delete-link/${id}/`, {
      headers: {
        'Authorization' : `Bearer ${token}`
      }
    })
    await fetchLinks()
  } catch (err) {
    error.value = 'Ошибка удаления'
  }
}

setTimeout(()=>{
  error.value = ''
},3000)
</script>

<template>
<section>
  <div v-if="links.length !== 0" class="view-link fade-in">
    <h1>Доступные ссылки</h1>

    <p><span>{{ error }}</span></p>

    <div v-for="link in links" :key="link.id" class="link-wrapper">
      <p class="link">
        Ссылка -
        <a :href="`${siteUrl}/link/${link.title}`" target="_blank">{{ link.title }}</a>
      </p>

      <div>
        <button @click="copyLink(link.title)" class="btn-copy">Copy</button>
        <button @click="toggleHistory(link)" class="btn-info">
        {{ link.showHistory ? 'Close' : 'Info' }}
        </button>
        <button @click="deleteLink(link.id)" class="btn-delete">X</button>
      </div>

    </div>
  </div>

  <div v-else>
    <h1>У вас пока нет ссылок</h1>
  </div>

  <div v-for="click in links">
    <div v-if="click.showHistory === true" class="info">
      <p>Info: {{click.title}}, <span class="click"> Click: {{ click.clicks }}</span></p>
      <p v-if="click.recent_clicks.length === 0 || !click.recent_clicks">
          На ссылку никто не нажимал
      </p>
      <div v-else v-for="info in click.recent_clicks" class="history-item">
        <p>IP:{{info.ip_address}}
          TIME: {{ new Date(info.created_at).toLocaleString('ru-RU') }}</p>
      </div>
    </div>
  </div>
</section>
</template>

<style scoped>
h1 {
  text-align: center;
  background: #0f172a;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow:
    1px 1px 1px rgba(255, 255, 255, 0.8),
    -1px -1px 1px rgba(0, 0, 0, 0.18);
  margin-bottom: 30px;
}
.view-link {
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
p {
  font-size: 18px;
  color: #707070;
}
p:not(.link) {
  margin-top: 30px;
}
p a {
  text-decoration: none;
}
.link-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
}
.fade-in {
  animation: fadeIn 0.8s ease-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.info{
  text-align: center;
  padding-bottom: 25px;
  padding-left: 10px;
  padding-right: 10px;
  max-width: 400px;
  width: 100%;
  margin: 0 auto;
  margin-top: 10px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
}
.info p {
  color: black;
}
.btn-info, .btn-delete, .btn-copy{
  color: white;
  padding: 5px 10px;
  border: none;
  border-radius: 5px;
  font-size: 14px;
  cursor: pointer;
  font-weight: bold;
  background: #0f172a;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.2);
  transition: all 0.3s ease;
}
.btn-delete{
  background: darkred;
  margin-left: 5px;
}
.btn-copy{
  margin-right: 5px;
}
.history-item {
  border-bottom: 1px solid rgba(112, 112, 112, 0.6);
  width: 98%;
  margin: 0 auto;
}
.history-item:last-child {
  border-bottom: none;
}
</style>