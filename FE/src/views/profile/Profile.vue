<template>
  <div class="container mt-4" v-if="!store.loading && store.profile">
    <div class="card shadow p-4">

      <h3 class="mb-4">User Profile</h3>

      <div class="text-center mb-4">
        <img
          :src="store.profile.avatar_url || defaultAvatar"
          class="rounded-circle"
          width="120"
          height="120"
        />
      </div>

      <input class="form-control mb-2" v-model="store.profile.username" disabled />
      <input class="form-control mb-2" v-model="store.profile.email" disabled />

      <input class="form-control mb-2" v-model="store.profile.full_name" placeholder="Full name" />
      <input class="form-control mb-2" v-model="store.profile.phone" placeholder="Phone" />
      <input class="form-control mb-3" v-model="store.profile.avatar_url" placeholder="Avatar URL" />

      <button class="btn btn-primary" @click="store.updateProfile">
        Save Changes
      </button>

      <p v-if="store.message" class="mt-3 text-success">
        {{ store.message }}
      </p>

    </div>
  </div>

  <div v-else class="text-center mt-5">
    Loading...
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useProfileStore } from "@/stores/profileStore";

const store = useProfileStore();
const defaultAvatar = "https://i.pravatar.cc/150";

onMounted(() => {
  store.fetchProfile();
});
</script>