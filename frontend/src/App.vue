<script setup>
// Import RouterLink if you want navigation links here
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <!-- Example Navigation -->
    <nav>
      <RouterLink to="/">Home</RouterLink> |
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </header>

  <main>
     <!-- Components matched by the route will be rendered here -->
    <RouterView />
  </main>

</template>

<style scoped>
 /* Add some basic styling */
  header {
    line-height: 1.5;
    max-height: 100vh;
    margin-bottom: 2rem;
  }
  nav {
    width: 100%;
    font-size: 12px;
    text-align: center;
    margin-top: 1rem;
  }
  nav a.router-link-exact-active {
    color: var(--color-text);
  }
  nav a.router-link-exact-active:hover {
    background-color: transparent;
  }
  nav a {
    display: inline-block;
    padding: 0 1rem;
    border-left: 1px solid var(--color-border);
  }
  nav a:first-of-type {
    border: 0;
  }
  main {
    padding: 1rem;
  }
</style>
