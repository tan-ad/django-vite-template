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
  getItems() {
    return apiClient.get('/items/');
  },
  getItem(id) {
    return apiClient.get(`/items/${id}/`);
  },
  createItem(data) {
    return apiClient.post('/items/', data);
  },
  updateItem(id, data) {
    return apiClient.put(`/items/${id}/`, data);
  },
  deleteItem(id) {
    return apiClient.delete(`/items/${id}/`);
  }
  // Add other endpoints as needed
};
