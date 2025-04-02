<script setup>
import { ref, onMounted } from 'vue';
import apiService from '@/services/api';

const items = ref([]);
const isLoading = ref(true);
const error = ref(null);

async function fetchItems() {
  isLoading.value = true;
  error.value = null;
  try {
    const response = await apiService.getItems();
    items.value = response.data;
  } catch (err) {
    console.error("Error fetching items:", err);
    error.value = "Failed to load items.";
  } finally {
    isLoading.value = false;
  }
}

// Fetch items when the component is mounted
onMounted(fetchItems);
</script>

<template>
  <div>
    <h1>Home - Items</h1>
    <div v-if="isLoading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <ul v-else-if="items.length">
      <li v-for="item in items" :key="item.id">
        {{ item.name }} - {{ item.description }}
      </li>
    </ul>
    <div v-else>No items found.</div>
    <!-- Add forms/buttons to interact (create/update/delete) later -->
  </div>
</template>

<style scoped>
.error {
  color: red;
}
</style>
