<template>
  <div class="topbar">
    <div>Dashboard</div>

    <button class="logout" @click="logout">
      Logout
    </button>
  </div>
</template>

<script setup>
import { useAuthStore } from '../../stores/auth'

const auth = useAuthStore()

const logout = () => {
  auth.logout()
}
</script>

<style scoped>
.topbar {
  height: 60px;
  background: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  border-bottom: 1px solid #eee;
}

.logout {
  background: #ef4444;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
}
</style>