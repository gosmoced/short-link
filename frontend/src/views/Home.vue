<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from "@/api.js";

const router = useRouter()
const isAuth = ref(false)
const url = ref('')
const title = ref('')
const error = ref('')

onMounted(() => {
  const token = localStorage.getItem('access_token')
  isAuth.value = !!token
})

const CreateLink = async () => {
  const token = localStorage.getItem('access_token')
  try {
    await api.post('/api/create/', {
      url : url.value,
      title: title.value
    }, {headers: {
      'Authorization': `Bearer ${token}`
      }} )
    title.value = ''
    url.value = ''
  }catch(err){
    error.value = 'Ошибка создания'
    setTimeout(()=> {
      error.value = ''
    }, 3000)
  }
}

</script>

<template>
  <div class="home-container">

    <div v-if="isAuth" class="get-form fade-in">
    <h1>Создание ссылок</h1>
    <form @submit.prevent="CreateLink">
      <label for="title">Название:</label>
      <input v-model="title" id="title">
      <label for="url">URL:</label>
      <input v-model="url" type="url" id="url">
      <span class="error">{{ error }}</span>
      <button class="btn-save">Сохранить</button>
    </form>
    </div>

    <div v-else class="hero-section fade-in">
      <h1 class="hero-title">Управляйте своими ссылками<br>как профессионал</h1>
      <p class="hero-text text-3d">
        Делайте длинные и сложные ссылки короткими, понятными и запоминающимися.
        Идеально для соцсетей, резюме и бизнеса.
      </p>

      <div class="hero-buttons">
        <router-link to="/register" class="cta-btn">Начать бесплатно</router-link>
        <router-link to="/login" class="secondary-btn">У меня есть аккаунт</router-link>
      </div>

      <div class="features">
        <div class="feature f-1">
          <i class="fa-solid fa-bolt"></i>
          <span>Мгновенно</span>
        </div>
        <div class="feature f-2">
          <i class="fa-solid fa-lock"></i>
          <span>Безопасно</span>
        </div>
        <div class="feature f-3">
          <i class="fa-solid fa-chart-simple"></i>
          <span>Удобно</span>
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
.home-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 65vh; /* Чтобы было по центру экрана */
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
.get-form {
  max-width: 500px;
  width: 100%;
  margin: 0 auto;
  padding: 40px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
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
.btn-save{
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
.btn-save:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.3);
  background: #1e293b;
}
.error {
  font-weight: bold;
  color: #e30000;
  display: block;
  opacity: 75%;
  margin-top: 10px;
}

/* --- СТИЛЬ ДЛЯ ГОСТЕЙ (Hero Section) --- */

.hero-section {
  text-align: center;
  max-width: 800px;
}
.hero-title {
  font-size: 3rem;
  line-height: 1.2;
  margin-bottom: 20px;
  background: linear-gradient(to right, #0f172a, #004baf);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.hero-text {
  font-size: 1.2rem;
  color: #64748b;
  margin-bottom: 40px;
  line-height: 1.6;
}
.hero-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
  margin-bottom: 50px;
}
.cta-btn {
  background: #004baf;
  color: white;
  padding: 15px 30px;
  border-radius: 30px;
  text-decoration: none;
  font-weight: bold;
  font-size: 1.1rem;
  box-shadow: 0 10px 20px rgba(49, 118, 248, 0.7);
  transition: 0.3s;
}
.cta-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 25px rgba(49, 118, 248);
}
.secondary-btn {
  background: white;
  color: #333;
  padding: 15px 30px;
  border-radius: 30px;
  text-decoration: none;
  font-weight: bold;
  border: 1px solid #ddd;
  transition: 0.3s;
}
.secondary-btn:hover {
  background: #f8fafc;
}
.features {
  display: flex;
  justify-content: center;
  gap: 40px;
  color: #64748b;
}
.feature {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  font-weight: bold;
}
.feature i {
  font-size: 26px;
}
.f-1 {
  color: #182442;
}
.f-2 {
  color: #1b3878;
}
.f-3 {
  color: #004baf;
}


.fade-in {
  animation: fadeIn 0.8s ease-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
@media (max-width: 768px) {
  .hero-title { font-size: 2rem; }
  .hero-buttons { flex-direction: column; }
}


</style>