import axios from 'axios';

const apiClient = axios.create({
  baseURL: '/api', // Uses the Vite proxy in dev, relative path works in prod
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
});

// Add interceptors for auth tokens or error handling if needed
// apiClient.interceptors.request.use(...)
// apiClient.interceptors.response.use(...)

export default {
  /**
   * Simple check to see if the API is responsive.
   * Assumes a '/api/ping/' endpoint exists on the backend.
   */
  checkApiStatus() {
    // Using GET for simplicity, could be POST if preferred
    return apiClient.get('/ping/');
  }
};
