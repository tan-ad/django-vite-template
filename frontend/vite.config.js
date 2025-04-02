// frontend/vite.config.js
import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  // --- Important Settings for Django Integration ---
  base: '/static/', // Serve assets from Django's STATIC_URL
  build: {
    manifest: true, // Generate manifest.json
    outDir: '../backend/frontend_dist', // Output relative to project root
    rollupOptions: {
      // Overwrite default .html entry
      input: 'src/main.js',
    },
  },
  server: {
    port: 5173, // Default Vite port
    strictPort: true, // Don't try other ports if 5173 is busy
    // Proxy API requests to Django dev server
    proxy: {
      '/api': { // Adjust '/api' if your Django API URLs start differently
        target: 'http://127.0.0.1:8000', // Your Django server address
        changeOrigin: true,
        // Optional: rewrite path if needed, e.g., remove /api prefix
        // rewrite: (path) => path.replace(/^\/api/, ''),
      },
      // You might need to proxy static/media files as well if serving through Django dev server
      // '/static': 'http://127.0.0.1:8000',
      // '/media': 'http://127.0.0.1:8000',
    }
  }
  // --- End Important Settings ---
})
