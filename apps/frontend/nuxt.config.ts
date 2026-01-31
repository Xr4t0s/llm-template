import tailwindcss from "@tailwindcss/vite";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  runtimeConfig: {
	public: {
		projectId: "dfbe3045d4172b6f8b4e332240c3e2a1"
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
	],
	server: {
      allowedHosts: [
        'localhost',
        '127.0.0.1',
        'xmcp.pro',
        'www.xmcp.pro',
      ]
    }
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
      isCustomElement: (tag: any) => tag === 'appkit-button',
    },
  },
})
