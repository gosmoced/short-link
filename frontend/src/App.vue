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
  background-color: #fcfdfc
}
.wrapper {
  width: 70%;
  margin: 0 auto;
  display: grid;
  min-height: 100vh;
  grid-template-rows: auto 1fr auto;
}
@media (max-width: 768px) {
  .wrapper {
    width: 95%;
    margin: 0 auto;
  }
}

</style>
