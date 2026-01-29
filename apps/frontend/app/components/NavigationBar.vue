<template>
  <nav class="fixed top-0 w-full z-50">
    <!-- Backdrop blur background -->
    <div class="absolute inset-0 bg-black/40 backdrop-blur-md border-b border-white/10" />

    <div class="relative max-w-7xl mx-auto px-6 py-4">
      <div class="flex items-center justify-between">
        
        <!-- Logo -->
        <NuxtLink
          to="/"
          class="flex items-center gap-2 group"
        >
          <div class="w-10 h-10 rounded-lg bg-linear-to-br from-indigo-500 to-cyan-400 flex items-center justify-center shadow-lg shadow-indigo-500/50 group-hover:shadow-xl group-hover:shadow-indigo-500/70 transition-all">
            <span class="text-white font-bold text-lg">⚡</span>
          </div>
          <span class="text-white font-bold text-xl group-hover:text-transparent group-hover:bg-linear-to-r group-hover:from-indigo-400 group-hover:to-cyan-400 group-hover:bg-clip-text transition-all">
			MCP
          </span>
        </NuxtLink>

        <!-- Desktop Navigation Links -->
        <div class="hidden md:flex items-center gap-2">
          <NuxtLink
            v-for="link in links"
            :key="link.to"
            :to="link.to"
            class="relative px-4 py-2 text-white/70 hover:text-white font-medium text-sm transition-colors duration-300 group"
            :active-class="'text-white'"
          >
            {{ link.label }}
            <!-- Underline animation on active -->
            <span class="absolute bottom-0 left-0 w-0 h-0.5 bg-linear-to-r from-indigo-400 to-cyan-400 group-hover:w-full transition-all duration-300" />
          </NuxtLink>
        </div>

        <!-- Wallet Button -->
        <div class="flex items-center gap-4">
          <WalletButton />
          
          <!-- Mobile menu button -->
          <button
            class="md:hidden w-10 h-10 flex items-center justify-center rounded-lg bg-white/10 hover:bg-white/20 transition text-white"
            @click="mobileMenuOpen = !mobileMenuOpen"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Navigation Menu -->
      <Transition
        enter-active-class="transition duration-300"
        enter-from-class="opacity-0 -translate-y-4"
        enter-to-class="opacity-100 translate-y-0"
        leave-active-class="transition duration-300"
        leave-from-class="opacity-100 translate-y-0"
        leave-to-class="opacity-0 -translate-y-4"
      >
        <div
          v-if="mobileMenuOpen"
          class="md:hidden absolute top-full left-0 right-0 mt-2 mx-4 rounded-xl bg-black/80 backdrop-blur-xl border border-white/20 p-4 space-y-2"
        >
          <NuxtLink
            v-for="link in links"
            :key="link.to"
            :to="link.to"
            class="block px-4 py-3 text-white/70 hover:text-white hover:bg-white/10 rounded-lg transition-colors font-medium"
            @click="mobileMenuOpen = false"
          >
            {{ link.label }}
          </NuxtLink>
        </div>
      </Transition>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface NavLink {
  to: string
  label: string
}

const mobileMenuOpen = ref(false)

const links: NavLink[] = [
  { to: '/', label: 'Home' },
  { to: '/build', label: 'Build' },
  { to: '/docs', label: 'Docs' },
  { to: '/about', label: 'About' },
]
</script>