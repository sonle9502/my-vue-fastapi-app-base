<template>
  <div>
    <div v-if="authStore.user">

      <p>
        Username: {{ authStore.user.username }}
      </p>

      <p>
        Email: {{ authStore.user.email }}
      </p>

      <p>Roles:</p>

      <ul>
        <li
          v-for="role in authStore.user.roles"
          :key="role"
        >
          {{ role }}
        </li>
      </ul>

    </div>
    <button @click="profile">Profile</button>
    <button @click="logout">Logout</button>
  </div>
</template>

<script setup>
import { useAuthStore } from "@/stores/authStore";

const authStore = useAuthStore();

const logout = async () => {
  await authStore.logout();
};

const profile = () => {
  // Navigate to profile page
  window.location.href = "/profile";
};
</script>