import axios from 'axios';

// Vite автоматически выберет нужный адрес
// import.meta.env.DEV — это true, когда ты запускаешь npm run dev
// import.meta.env.PROD — это true, когда сайт собран (build)

const api = axios.create({
  baseURL: import.meta.env.DEV
    ? 'http://127.0.0.1:8000'  // Адрес для домашней разработки
    : 'https://gosmoced.pythonanywhere.com', // Адрес для интернета
});

export default api;