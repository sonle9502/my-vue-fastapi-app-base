<template>
  <div class="layout">
    
    <!-- HEADER -->
    <header class="header">
      <h3>My System</h3>

      <button class="btn btn-danger btn-sm" @click="logout">
        Logout
      </button>
    </header>

    <!-- CONTENT -->
    <main class="content">
      <router-view />
    </main>

  </div>
</template>

<script setup>
import { useAuthStore } from '../stores/auth'

const auth = useAuthStore()

const logout = () => {
  auth.logout()
}
</script>

<style scoped>
.header {
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  background: #1f2937;
  color: white;
}
</style>