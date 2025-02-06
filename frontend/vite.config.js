import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/prorate': 'http://localhost:8000', // Proxy API requests to the FastAPI backend
    },
  },
});
