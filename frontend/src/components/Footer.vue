<script setup>
import logo from '../assets/img_1.png';
</script>

<template>
  <footer>
    <div class="top">
      <div>
      <a href="*"><i class="fa-brands fa-instagram social-icon inst"></i></a>
      <a href="*"><i class="fa-brands fa-youtube social-icon yt"></i></a>
      <a href="*"><i class="fa-brands fa-telegram social-icon tg"></i></a>
    </div>
    <img :src="logo" alt="">
    </div>
    <p>Все права защищены</p>
  </footer>
</template>

<style scoped>
footer{
  margin-top: 20px;
}
.top {
  display: flex;
  justify-content: space-between;
  align-items: center;

}
img {
  width: 180px;
  height: auto;
}
a {
  margin-right: 20px;
}
.social-icon {
  font-size: 30px;
  margin-right: 15px;
  color: #707070;
  transition: all 0.3s;
}
.social-icon:hover {
  transform: translateY(-3px);
}
.inst:hover { color: #E1306C; }
.tg:hover    { color: #0088cc; }
.yt:hover    { color: #FF0000; }
p {
  text-align: center;
  width: 100%;
  color: gray;
  font-size: 16px;
  margin-bottom: 20px;
}

@media (max-width: 768px) {
  img {
    width: 120px;
    height: auto;
  }
}
@media (max-width: 768px) {
  .social-icon{
    font-size: 22px;
  }
}
</style>