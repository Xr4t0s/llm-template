import tailwindcss from "@tailwindcss/vite";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  runtimeConfig: {
	public: {
		projectId: "d61d68cb1a573a4678dc4bcad697bd68"
	}
  },
  app: {
	pageTransition: {
      name: 'page',
      mode: 'out-in'
    },
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
  modules: [
	'@pinia/nuxt',
	'nuxt-icon',
  ],
  vue: {
    compilerOptions: {
      isCustomElement: (tag) => tag === 'appkit-button',
    },
  },
})
