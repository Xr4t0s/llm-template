<template>
  <footer class="relative z-10 w-full  sm:mt-40 border-t border-white/10">
    <!-- Background gradient -->
    <div class="absolute inset-0 bg-gradient-to-b from-transparent via-indigo-950/5 to-black pointer-events-none" />

    <div class="relative max-w-7xl mx-auto px-6 sm:px-8 py-16 sm:py-20">
      <div class="space-y-12 sm:space-y-16">
        <!-- Main footer content -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 sm:gap-12">
          
          <!-- Brand section -->
          <div class="space-y-6 sm:col-span-2 lg:col-span-1">
            <!-- Logo -->
            <NuxtLink
              to="/"
              class="flex items-center gap-3 group w-fit"
            >
              <div class="relative">
                <div class="absolute inset-0 bg-gradient-to-br from-indigo-500 to-cyan-400 rounded-lg blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
                <div class="relative w-10 h-10 rounded-lg bg-gradient-to-br from-indigo-500 to-cyan-400 flex items-center justify-center">
                  <span class="text-white font-black text-lg">⚡</span>
                </div>
              </div>
              <span class="text-white font-black text-lg tracking-tight group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-indigo-300 group-hover:to-cyan-300 group-hover:bg-clip-text transition-all duration-300">
                Studio
              </span>
            </NuxtLink>
            
            <!-- Tagline -->
            <p class="text-sm text-white/60 leading-relaxed font-light max-w-xs">
              Build Web3 products with intention. Orchestrate AI. Ship with clarity.
            </p>
          </div>

          <!-- Product Links -->
          <div class="space-y-4">
            <h3 class="text-sm font-bold text-white uppercase tracking-wider">Product</h3>
            <ul class="space-y-3">
              <li>
                <NuxtLink
                  to="/build"
                  class="text-sm text-white/60 hover:text-white transition-colors duration-300 font-light"
                >
                  Build Studio
                </NuxtLink>
              </li>
              <li>
                <NuxtLink
                  to="/docs"
                  class="text-sm text-white/60 hover:text-white transition-colors duration-300 font-light"
                >
                  Documentation
                </NuxtLink>
              </li>
              <li>
                <a
                  href="#"
                  class="text-sm text-white/60 hover:text-white transition-colors duration-300 font-light"
                >
                  Roadmap
                </a>
              </li>
              <li>
                <a
                  href="#"
                  class="text-sm text-white/60 hover:text-white transition-colors duration-300 font-light"
                >
                  Pricing
                </a>
              </li>
            </ul>
          </div>

          <!-- Company Links -->
          <div class="space-y-4">
            <h3 class="text-sm font-bold text-white uppercase tracking-wider">Company</h3>
            <ul class="space-y-3">
              <li>
                <NuxtLink
                  to="/about"
                  class="text-sm text-white/60 hover:text-white transition-colors duration-300 font-light"
                >
                  About
                </NuxtLink>
              </li>
              <li>
                <a
                  href="#"
                  class="text-sm text-white/60 hover:text-white transition-colors duration-300 font-light"
                >
                  Blog
                </a>
              </li>
              <li>
                <a
                  href="#"
                  class="text-sm text-white/60 hover:text-white transition-colors duration-300 font-light"
                >
                  Careers
                </a>
              </li>
              <li>
                <a
                  href="#"
                  class="text-sm text-white/60 hover:text-white transition-colors duration-300 font-light"
                >
                  Contact
                </a>
              </li>
            </ul>
          </div>

          <!-- Legal Links -->
          <div class="space-y-4">
            <h3 class="text-sm font-bold text-white uppercase tracking-wider">Legal</h3>
            <ul class="space-y-3">
              <li>
                <a
                  href="#"
                  class="text-sm text-white/60 hover:text-white transition-colors duration-300 font-light"
                >
                  Privacy
                </a>
              </li>
              <li>
                <a
                  href="#"
                  class="text-sm text-white/60 hover:text-white transition-colors duration-300 font-light"
                >
                  Terms
                </a>
              </li>
              <li>
                <a
                  href="#"
                  class="text-sm text-white/60 hover:text-white transition-colors duration-300 font-light"
                >
                  Cookies
                </a>
              </li>
              <li>
                <a
                  href="#"
                  class="text-sm text-white/60 hover:text-white transition-colors duration-300 font-light"
                >
                  Security
                </a>
              </li>
            </ul>
          </div>
        </div>

        <!-- Divider -->
        <div class="h-px bg-gradient-to-r from-white/0 via-white/10 to-white/0" />

        <!-- Bottom section -->
        <div class="flex flex-col sm:flex-row items-center justify-between gap-6">
          <!-- Copyright -->
          <div class="text-xs text-white/40 font-light">
            © {{ year }} LLM Studio. Built with intention.
          </div>

          <!-- Social icons -->
          <div class="flex items-center gap-6">
            <a
              v-for="social in socials"
              :key="social.name"
              :href="social.href"
              target="_blank"
              rel="noopener noreferrer"
              :aria-label="social.name"
              class="group relative w-10 h-10 flex items-center justify-center rounded-lg bg-white/5 border border-white/10 hover:border-white/30 hover:bg-white/10 transition-all duration-300"
            >
              <!-- Hover glow -->
              <div class="absolute inset-0 rounded-lg bg-gradient-to-br opacity-0 group-hover:opacity-20 transition-opacity duration-300" :style="{ backgroundImage: `linear-gradient(135deg, ${social.color} 0%, rgba(0,0,0,0) 100%)` }" />
              
              <!-- Icon -->
              <svg class="w-5 h-5 text-white/70 group-hover:text-white transition-colors relative z-10" fill="currentColor" viewBox="0 0 24 24">
                <component :is="`svg`" v-bind="social.iconProps" />
              </svg>

              <!-- Tooltip -->
              <div class="absolute bottom-full mb-2 px-2 py-1 rounded text-xs font-medium text-white bg-black border border-white/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300 whitespace-nowrap pointer-events-none">
                {{ social.name }}
              </div>
            </a>
          </div>

          <!-- Status -->
          <div class="flex items-center gap-2 text-xs text-white/40">
            <div class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            <span>All systems operational</span>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const year = new Date().getFullYear()

const socials = [
  {
    name: 'Twitter',
    href: 'https://twitter.com',
    color: '#1DA1F2',
    iconProps: {
      viewBox: '0 0 24 24',
      d: 'M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2s9 5 20 5a9.5 9.5 0 00-9-5.5c4.75 2.25 7-7 7-7'
    }
  },
  {
    name: 'GitHub',
    href: 'https://github.com',
    color: '#ffffff',
    iconProps: {
      viewBox: '0 0 24 24',
      d: 'M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'
    }
  },
  {
    name: 'Discord',
    href: 'https://discord.gg',
    color: '#5865F2',
    iconProps: {
      viewBox: '0 0 24 24',
      d: 'M20.317 4.3671a19.8062 19.8062 0 00-4.8850-1.5152.0741.0741 0 00-.0785.0371c-.211.3753-.4447.8648-.6083 1.2524-.9815-.1514-1.9519-.1514-2.9139 0-.1636-.3876-.3957-.8771-.6078-1.2524a.077.077 0 00-.0785-.037 19.7930 19.7930 0 00-4.8856 1.515.0699.0699 0 00-.0321.0277C1.75 8.068 1.1236 11.7512 2.0897 15.3467a.082.082 0 00.0313.0456 19.9484 19.9484 0 005.9325 3.0011.0801.0801 0 00.0842-.0291c.4616-.6304.8731-1.2952 1.226-1.9707a.074.074 0 00-.0407-.1025c-.6656-.2485-1.2995-.5792-1.9023-.9652a.077.077 0 01-.0076-.1277c.1277-.0955.2555-.1952.3779-.2965a.0743.0743 0 01.0765-.0105c3.9921 1.8218 8.3625 1.8218 12.3228 0a.0742.0742 0 01.0765.0095c.1232.1013.2492.2011.3805.2966a.0755.0755 0 01-.0071.1288c-.6954.3860-1.4382.7134-2.0486.9652a.0749.0749 0 00-.0391.1025c.3744.7655.7879 1.5403 1.2620 1.9713a.0800.0800 0 00.0842.0291 19.9993 19.9993 0 005.9365-3.0011.0822.0822 0 00.0313-.0456c1.11-3.6786.4657-7.2154-1.9154-10.0363a.0622.0622 0 00-.032-.0277zM8.02 12.6321c-.735 0-1.3335-.6755-1.3335-1.506 0-.8316.5982-1.506 1.3335-1.506.7365 0 1.3458.6755 1.3335 1.506 0 .8316-.5982 1.506-1.3335 1.506zm7.9776 0c-.7365 0-1.3335-.6755-1.3335-1.506 0-.8316.5982-1.506 1.3335-1.506.7365 0 1.3458.6755 1.3335 1.506 0 .8316-.597 1.506-1.3335 1.506z'
    }
  }
]
</script>

<style scoped>
/* Smooth transitions */
* {
  @apply transition-all duration-300;
}

/* SVG path animation */
svg path {
  @apply transition-all duration-300;
}
</style>