<script setup>
import {ref, onMounted} from "vue";
import {useRouter} from "vue-router";
import axios from "axios";

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

setTimeout(()=>{
  error.value = ''
},3000)
</script>

<template>
  <div v-if="links.length !== 0" class="view-link fade-in">
    <h1>Доступные ссылки</h1>
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
  width: 50%;
  margin: 0 25%;
  padding: 40px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
}
.get-form{
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
button:not(.delete){
  color: white;
  padding: 10px 20px;
  margin-top: 20px;
  border: none;
  border-radius: 5px;
  font-size: 15px;
  cursor: pointer;
  font-weight: bold;
  background: #0f172a;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.2);
  transition: all 0.3s ease;
}
button:not(.delete):hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.3);
  background: #1e293b;
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
  text-decoration: none;
}
span {
  font-weight: bold;
  color: #e30000;
  display: block;
  opacity: 75%;
  margin-top: 10px;
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

@media (max-width: 768px) {
  .view-link{
    width: 90%;
    margin: 0 auto;
  }
}
</style>