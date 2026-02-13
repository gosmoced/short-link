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

.wrapper {
  max-width: 70%;
  margin: 0 auto;
  display: grid;
  grid-template-rows: auto 1fr auto;
  min-height: 100dvh;
}
@media (max-width: 525px){
  .wrapper{
    max-width: 90%;
  }
}
</style>
