<template>
  <div class="sidebar">
    <h2 class="logo">ADMIN</h2>

    <ul>
      <li :class="{ active: isActive('/') }" @click="go('/')">
        Dashboard
      </li>

      <li :class="{ active: isActive('/users') }" @click="go('/users')">
        Users
      </li>

      <li :class="{ active: isActive('/products') }" @click="go('/products')">
        Products
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const go = (path) => router.push(path)
const isActive = (path) => route.path === path
</script>

<style scoped>
.sidebar {
  width: 220px;
  background: #111827;
  color: white;
  padding: 20px;
}

.logo {
  margin-bottom: 20px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px;
  cursor: pointer;
  border-radius: 6px;
}

li:hover {
  background: #374151;
}

.active {
  background: #2563eb;
}
</style>