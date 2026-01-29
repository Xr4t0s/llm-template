<template>
  <div class="relative w-full min-h-screen bg-black overflow-hidden flex flex-col">
    <!-- Animated background -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <!-- Animated gradient orbs -->
      <div class="absolute top-1/4 -right-40 w-96 h-96 bg-indigo-600/25 rounded-full blur-3xl animate-float" />
      <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-cyan-500/20 rounded-full blur-3xl animate-float-delayed" />
      <div class="absolute top-2/3 left-1/4 w-80 h-80 bg-emerald-500/15 rounded-full blur-3xl animate-pulse" style="animation-duration: 8s;" />
      
      <!-- Grid background -->
      <svg class="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <pattern id="grid-layout" width="50" height="50" patternUnits="userSpaceOnUse">
            <path d="M 50 0 L 0 0 0 50" fill="none" stroke="rgba(139, 92, 246, 0.1)" stroke-width="1"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid-layout)" />
      </svg>

      <!-- Gradient overlays for depth -->
      <div class="absolute inset-0 bg-linear-to-b from-black/0 via-transparent to-black/40" />
      <div class="absolute inset-0 bg-linear-to-r from-indigo-950/10 via-transparent to-cyan-950/10 opacity-50" />
    </div>

    <!-- Navigation -->
    <NavigationBar />

    <!-- Main Content (Grows to fill available space) -->
    <main class="relative z-10 pt-20 sm:pt-24 flex-1">
      <slot />
    </main>

    <!-- Footer -->
    <Footer />

    <!-- Scroll indicator (appears on scroll) -->
    <div 
      class="fixed bottom-8 left-1/2 transform -translate-x-1/2 z-40 transition-opacity duration-500"
      :class="{ 'opacity-0 pointer-events-none': hasScrolled }"
    >
      <div class="flex flex-col items-center gap-3">
        <span class="text-white/50 text-xs font-light tracking-widest uppercase">Scroll</span>
        <div class="animate-bounce">
          <svg class="w-5 h-5 text-white/40" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
          </svg>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Footer from '~/components/FooterBar.vue'
import { ref, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const hasScrolled = ref(false)

// Handle scroll detection for scroll indicator
const handleScroll = () => {
  hasScrolled.value = window.scrollY > 100
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
/* Custom animations */
@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-30px);
  }
}

@keyframes float-delayed {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(30px);
  }
}

@keyframes smoothBounce {
  0%, 100% { 
    transform: translateY(0); 
  }
  50% { 
    transform: translateY(-8px); 
  }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

.animate-float-delayed {
  animation: float-delayed 8s ease-in-out infinite;
}

.animate-bounce {
  animation: smoothBounce 2s ease-in-out infinite;
}

/* Smooth scroll behavior */
html {
  scroll-behavior: smooth;
}

/* Flex layout setup */
#__nuxt {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

/* Remove scrollbar for cleaner look (optional - uncomment to use) */
/* 
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: rgba(139, 92, 246, 0.3);
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(139, 92, 246, 0.5);
}
*/
</style>