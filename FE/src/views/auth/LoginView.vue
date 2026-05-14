<script setup>
import { useAuthStore } from "@/stores/authStore";

const auth = useAuthStore();

const login = async () => {
  await auth.loginWithKeycloak();
};
</script>

<template>
  <button @click="login">
    Login with Keycloak
  </button>
</template>