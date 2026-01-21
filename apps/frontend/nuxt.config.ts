import tailwindcss from "@tailwindcss/vite";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app: {
    head: {
      title: 'Web3 Dashboard',
    },
  },
  css: ["~/assets/css/main.css"],
  vite: {
	plugins: [
		tailwindcss(),
	]
  },
  nitro: {
    devProxy: {
      '/api/v1': {
        target: 'http://backend:3001/api/v1',
        changeOrigin: true,
      },
    },
  },
})
