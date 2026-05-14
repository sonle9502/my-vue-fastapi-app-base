<template>
  <div class="layout">

    <!-- SIDEBAR -->
    <Sidebar />

    <div class="main">

      <!-- TOPBAR -->
      <Topbar />

      <!-- CONTENT -->
      <div class="content">
        <router-view />
      </div>

    </div>

  </div>
</template>

<script setup>
import Sidebar from '../components/layout/Sidebar.vue'
import Topbar from '../components/layout/Topbar.vue'
</script>

<style scoped>
.layout {
  display: flex;
  height: 100vh;
  font-family: Arial;
}

.main {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.content {
  padding: 20px;
  background: #f3f4f6;
  flex: 1;
  overflow: auto;
}
</style>