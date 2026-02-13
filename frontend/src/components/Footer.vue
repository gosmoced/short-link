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
    <p class="logo">Short<span>Link</span></p>
    </div>
    <p class="rights">All rights reserved</p>
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
.logo{
  font-size: 40px;
  font-weight: bold;
  background: linear-gradient(to right, #182442, #004baf);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
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
.rights {
  text-align: center;
  width: 100%;
  color: gray;
  font-size: 16px;
  margin-bottom: 20px;
}

@media (max-width: 768px) {
  .logo {
    font-size: 30px;
  }
}
@media (max-width: 768px) {
  .social-icon{
    font-size: 22px;
    margin-right: 10px;
  }
}
</style>