import { fileURLToPath, URL } from 'node:url'
import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
// Use the function form to access mode and loadEnv
export default defineConfig(({ mode }) => {
  // Load environment variables based on the mode (development/production)
  // Vite loads .env files in the project root (frontend/) by default.
  // Prefixing with VITE_ exposes them to client-side code, but we only need it here for the proxy target.
  // Pass the environment variable via docker-compose for container setup.
  const env = loadEnv(mode, process.cwd(), ''); // Load all env vars

  const djangoServer = env.VITE_API_PROXY_TARGET || 'http://127.0.0.1:8000';
  console.log(`Vite proxying API requests to: ${djangoServer}`); // Log target for debugging

  return {
    plugins: [
      vue(),
    ],
    resolve: {
      alias: {
        // Use @ alias for cleaner imports in your Vue code
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    },

    // --- Server Configuration (Development) ---
    server: {
      // Make server accessible externally (needed for Docker)
      host: '0.0.0.0',
      port: 5173, // Default Vite port
      strictPort: true, // Exit if port is already in use

      // Proxy API requests to the Django backend server
      proxy: {
        '/api': { // Match requests starting with /api
          target: djangoServer, // Target read from env var or default
          changeOrigin: true, // Recommended for virtual hosted sites
          secure: false,      // Don't verify SSL cert if target is https (useful for some setups)
          // ws: true,           // Proxy websockets if needed
          // Optional: Rewrite path if Django URLs don't start with /api
          // rewrite: (path) => path.replace(/^\/api/, ''),
        },
        // You generally DON'T need to proxy /static/ or /media/ here
        // because Django serves the base HTML, and in dev mode,
        // django-vite template tags point directly to this Vite server (5173) for assets.
        // In production, Django serves the built static files itself.
      },

      // Optional: Configure HMR (Hot Module Replacement)
      // hmr: {
      //   host: 'localhost', // Or your specific local hostname if needed
      //   port: 5173,
      // }
    },

    // --- Build Configuration (Production) ---
    build: {
      // Output directory relative to `frontend/` root
      // Should match Django's DJANGO_VITE_ASSETS_PATH setting base
      outDir: '../backend/frontend_dist',
      // Generate manifest.json for django-vite
      manifest: true,
      // Generate sourcemaps for easier debugging in production (optional)
      sourcemap: true,
      rollupOptions: {
        // Ensure your JS entry point is correctly specified
        input: 'src/main.js',
        // Optional: Configure output chunking/naming if needed
        // output: { ... }
      },
      // Empty output directory before building
      emptyOutDir: true,
    },

    // --- Base URL ---
    // Must match Django's STATIC_URL
    base: '/static/',
  }
})
