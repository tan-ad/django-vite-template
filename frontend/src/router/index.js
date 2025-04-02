import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue' // Example: Assuming you have a HomeView component

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (About.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('../views/AboutView.vue') // Example: Lazy-loaded AboutView
  }
  // Add more routes here
]

const router = createRouter({
  // Use createWebHistory for standard SPA routing (uses browser history API)
  // Requires server configuration (like your Django catch-all route) to work correctly on page refresh/direct access.
    history: createWebHistory(),
    routes // short for `routes: routes`
})

export default router
