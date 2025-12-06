<script setup>
import { RouterView } from 'vue-router'
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
</script>

<template>
  <div class="wrapper">
  <Header />
  <main>
    <RouterView />
  </main>
  <Footer />
  </div>
</template>

<style>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  margin: 0;
  /* Мягкий, "воздушный" градиент */
  background-color: #e0e5ec;
  background-image:
    radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%),
    radial-gradient(at 50% 0%, hsla(225,39%,30%,1) 0, transparent 50%),
    radial-gradient(at 100% 0%, hsla(339,49%,30%,1) 0, transparent 50%);
  /* Заменим на более светлый вариант для "Light Theme": */
  background:
    radial-gradient(at 10% 10%, rgb(255, 233, 244) 0px, transparent 50%),
    radial-gradient(at 90% 10%, rgb(227, 246, 255) 0px, transparent 50%),
    radial-gradient(at 90% 90%, rgb(200, 240, 230) 0px, transparent 50%),
    radial-gradient(at 10% 90%, rgb(235, 235, 255) 0px, transparent 50%);
  background-size: 100% 100%;
  background-attachment: fixed;
}
.wrapper {
  width: 70%;
  margin: 0 auto;
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100dvh;
}
@media (max-width: 768px) {
  .wrapper {
    width: 95%;
    margin: 0 auto;
  }
}
</style>
