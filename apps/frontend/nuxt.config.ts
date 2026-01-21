// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app: {
    head: {
      title: 'Web3 Dashboard',
    },
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
