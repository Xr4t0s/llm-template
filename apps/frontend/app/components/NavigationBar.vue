<template>
  <nav class="fixed top-0 w-full z-50">
    <!-- Backdrop blur background -->
    <div class="absolute inset-0 bg-linear-to-b from-black/80 via-black/60 to-black/0 backdrop-blur-xl border-b border-white/10" />
    
    <!-- Animated glow underline -->
    <div 
      class="absolute bottom-0 left-0 right-0 h-px bg-linear-to-r from-transparent via-indigo-500/30 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"
      style="box-shadow: 0 0 20px rgba(139, 92, 246, 0.3)"
    />

    <div class="relative max-w-7xl mx-auto px-6 py-4 sm:py-5">
      <div class="flex items-center justify-between">
        
        <!-- Logo -->
        <NuxtLink
          to="/"
          class="flex items-center gap-3 group relative z-10"
        >
          <!-- Logo box with glow -->
          <div class="relative">
            <div class="absolute inset-0 bg-linear-to-br from-indigo-500 via-indigo-400 to-cyan-400 rounded-xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" style="filter: blur(8px)" />
            <div class="relative w-10 h-10 rounded-xl bg-linear-to-br from-indigo-500 to-cyan-400 flex items-center justify-center shadow-lg shadow-indigo-500/40 group-hover:shadow-2xl group-hover:shadow-indigo-500/60 transition-all duration-300">
              <span class="text-white font-black text-lg">⚡</span>
            </div>
          </div>
          
          <!-- Logo text with gradient on hover -->
          <span class="text-white font-black text-xl tracking-tight group-hover:text-transparent group-hover:bg-linear-to-r group-hover:from-indigo-300 group-hover:via-cyan-300 group-hover:to-emerald-300 group-hover:bg-clip-text transition-all duration-300">
            Studio
          </span>
        </NuxtLink>

        <!-- Desktop Navigation Links -->
        <div class="hidden lg:flex items-center gap-1">
          <NuxtLink
            v-for="link in links"
            :key="link.to"
            :to="link.to"
            class="relative px-4 py-2 text-white/60 hover:text-white/90 font-semibold text-sm transition-colors duration-300 group"
            :active-class="'text-white'"
          >
            <!-- Background hover effect -->
            <div class="absolute inset-0 rounded-lg bg-white/0 group-hover:bg-white/5 transition-colors duration-300" />
            
            <!-- Text -->
            <span class="relative">{{ link.label }}</span>
            
            <!-- Underline animation on hover -->
            <span class="absolute bottom-1 left-4 right-4 h-0.5 bg-linear-to-r from-indigo-400/0 via-indigo-400 to-cyan-400/0 scale-x-0 group-hover:scale-x-100 transition-transform duration-300 origin-center" />
          </NuxtLink>
        </div>

        <!-- Right side: Wallet + Mobile menu -->
        <div class="flex items-center gap-3 sm:gap-4 relative z-10">
          <!-- Wallet Button -->
          <div class="hidden sm:block">
            <WalletButton />
          </div>

		  
          <!-- Mobile wallet button -->
          <div class="sm:hidden">
            <WalletButton />
          </div>
          <!-- Mobile menu button -->
          <button
            class="lg:hidden group relative w-11 h-11 flex items-center justify-center rounded-lg bg-white/10 hover:bg-white/15 border border-white/10 hover:border-white/20 transition-all duration-300"
            @click="mobileMenuOpen = !mobileMenuOpen"
            :aria-label="mobileMenuOpen ? 'Close menu' : 'Open menu'"
          >
            <!-- Glow on hover -->
            <div class="absolute inset-0 rounded-lg bg-linear-to-br from-indigo-500/0 to-cyan-500/0 group-hover:from-indigo-500/10 group-hover:to-cyan-500/10 transition-colors duration-300" />
            
            <svg class="w-5 h-5 text-white relative transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M4 6h16M4 12h16M4 18h16" />
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>

        </div>
      </div>

      <!-- Mobile Navigation Menu -->
      <Transition
        enter-active-class="transition duration-400 ease-out"
        enter-from-class="opacity-0 scale-95 -translate-y-4"
        enter-to-class="opacity-100 scale-100 translate-y-0"
        leave-active-class="transition duration-300 ease-in"
        leave-from-class="opacity-100 scale-100 translate-y-0"
        leave-to-class="opacity-0 scale-95 -translate-y-4"
      >
        <div
          v-if="mobileMenuOpen"
          class="lg:hidden absolute top-full left-4 right-4 mt-3 rounded-2xl bg-linear-to-br from-white/15 via-white/10 to-white/5 backdrop-blur-2xl border border-white/20 shadow-2xl shadow-black/50 p-4 space-y-2 origin-top"
        >
          <!-- Navigation links -->
          <NuxtLink
            v-for="link in links"
            :key="link.to"
            :to="link.to"
            class="block px-4 py-3 text-white/70 hover:text-white hover:bg-white/10 rounded-lg transition-all duration-300 font-semibold text-sm group"
            @click="mobileMenuOpen = false"
          >
            <span class="flex items-center gap-2">
              {{ link.label }}
              <span class="text-xs text-white/30 group-hover:text-white/60 transition-colors">→</span>
            </span>
          </NuxtLink>

          <!-- Divider -->
          <div class="h-px bg-linear-to-r from-white/0 via-white/10 to-white/0 my-2" />

          <!-- Additional mobile-specific actions could go here -->
          <div class="px-4 py-3 text-xs text-white/40 text-center">
            Build Web3 with intention
          </div>
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

<style scoped>
/* Smooth transitions for all elements */
* {
  @apply transition-all duration-300;
}

/* Logo glow animation on interaction */
@keyframes logoGlow {
  0%, 100% {
    box-shadow: 0 0 20px rgba(139, 92, 246, 0.4);
  }
  50% {
    box-shadow: 0 0 40px rgba(139, 92, 246, 0.6);
  }
}

/* Navbar entrance animation */
@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

nav {
  animation: slideDown 0.6s ease-out;
}


/* Prevent layout shift on mobile */
@media (max-width: 1024px) {
  nav {
    padding-bottom: max(1rem, env(safe-area-inset-bottom));
  }
}
</style>