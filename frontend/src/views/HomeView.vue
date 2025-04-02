<script setup>
import { ref, onMounted } from 'vue';
import apiService from '@/services/api'; // Ensure path is correct

const apiStatus = ref('checking'); // 'checking', 'ok', 'error'
const apiMessage = ref('');
const errorMessage = ref('');

async function checkApi() {
  apiStatus.value = 'checking';
  apiMessage.value = '';
  errorMessage.value = '';
  try {
    const response = await apiService.checkApiStatus();
    // Assuming the backend sends { "message": "API is responsive." }
    apiMessage.value = response.data?.message || 'Successfully connected to API.';
    apiStatus.value = 'ok';
    console.log('API Status Check Response:', response.data);
  } catch (err) {
    console.error("Error checking API status:", err);
    apiStatus.value = 'error';
    if (err.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      errorMessage.value = `API Error ${err.response.status}: ${err.response.data?.detail || err.message}`;
    } else if (err.request) {
      // The request was made but no response was received
      errorMessage.value = 'No response received from API. Is the backend running?';
    } else {
      // Something happened in setting up the request that triggered an Error
      errorMessage.value = `Request failed: ${err.message}`;
    }
  }
}

// Check API status when the component is mounted
onMounted(checkApi);
</script>

<template>
  <div class="home-view">
    <h1>Django + Vite + Vue Template</h1>
    <p>
      This page demonstrates the basic integration between the Django backend and the Vue frontend.
    </p>

    <div class="status-card">
      <h2>API Connection Status</h2>
      <div v-if="apiStatus === 'checking'" class="status status-checking">
        <p>Checking API connection...</p>
        <div class="spinner"></div>
      </div>
      <div v-else-if="apiStatus === 'ok'" class="status status-ok">
        <p>✅ Connection Successful!</p>
        <p v-if="apiMessage" class="api-message"><em>Backend says: "{{ apiMessage }}"</em></p>
      </div>
      <div v-else-if="apiStatus === 'error'" class="status status-error">
        <p>❌ Connection Failed</p>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
        <p><small>Check the browser console and backend logs for more details.</small></p>
      </div>
       <button @click="checkApi" :disabled="apiStatus === 'checking'">
        Re-check Status
      </button>
    </div>

    <div class="next-steps">
      <h2>Next Steps</h2>
      <ul>
        <li>Explore the project structure (<code>backend/</code> and <code>frontend/</code> directories).</li>
        <li>Modify this component (<code>frontend/src/views/HomeView.vue</code>) to build your UI.</li>
        <li>Add more API endpoints in Django (<code>backend/api/views.py</code> and <code>urls.py</code>).</li>
        <li>Create Django models (<code>backend/api/models.py</code>) and serializers (<code>backend/api/serializers.py</code>).</li>
        <li>Fetch data from your new endpoints in your Vue components using the <code>frontend/src/services/api.js</code> service.</li>
        <li>Configure authentication, database, etc. in <code>backend/settings.py</code> and <code>backend/.env</code>.</li>
         <li>Review the Docker setup (`docker-compose.yml`, `Dockerfile`s) for development and plan for production deployment.</li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.home-view {
  max-width: 800px;
  margin: 2rem auto;
  padding: 1rem;
  font-family: sans-serif;
  line-height: 1.6;
}

h1, h2 {
  border-bottom: 1px solid #eee;
  padding-bottom: 0.5rem;
  margin-bottom: 1rem;
}

.status-card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  text-align: center;
}

.status-card h2{
  color: #333
}

.status {
  padding: 1rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}

.status-checking {
  background-color: #eef;
  border-left: 5px solid #66f;
  color: #339;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.status-ok {
  background-color: #efe;
  border-left: 5px solid #3c3;
  color: #060;
}

.status-error {
  background-color: #fee;
  border-left: 5px solid #c33;
  color: #900;
}

.api-message, .error-message {
  margin-top: 0.5rem;
  font-size: 0.9em;
}

.error-message {
  font-weight: bold;
}

button {
  padding: 0.5rem 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
  background-color: #fff;
  transition: background-color 0.2s ease;
  color: #333
}

button:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

button:not(:disabled):hover {
  background-color: #f0f0f0;
}

.next-steps ul {
  list-style: disc;
  padding-left: 2rem;
}

.next-steps li {
  margin-bottom: 0.5rem;
}

/* Simple Spinner */
.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border-left-color: #66f;
  animation: spin 1s ease infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

code {
  background-color: #504f4f;
  padding: 0.2em 0.4em;
  border-radius: 3px;
  font-family: monospace;
}
</style>
