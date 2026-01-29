<template>
  <div class="flex items-center gap-2 sm:gap-3">
    <!-- Not Connected State -->
    <button
      v-if="!authStore.isConnected"
      @click="authStore.connect"
      :disabled="authStore.isLoading"
      class="group relative px-6 sm:px-8 py-3 rounded-xl font-bold text-sm text-white overflow-hidden disabled:opacity-50 disabled:cursor-not-allowed transition-all"
    >
      <!-- Gradient background -->
      <div class="absolute inset-0 bg-linear-to-r from-indigo-600 via-indigo-500 to-cyan-500 opacity-100 group-hover:opacity-90 group-disabled:opacity-60 transition-opacity duration-300" />
      
      <!-- Shimmer effect -->
      <div class="absolute inset-0 bg-linear-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full group-disabled:translate-x-0 transition-transform duration-700" />
      
      <!-- Content -->
      <span class="relative flex items-center gap-2 justify-center">
        <svg
          v-if="authStore.isLoading"
          class="w-4 h-4 animate-spin"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
        </svg>
        <span v-else>
          <svg class="w-5 h-5 inline mr-2" fill="currentColor" viewBox="0 0 20 20">
            <path d="M18 9a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          Connect Wallet
        </span>
      </span>
    </button>

    <!-- Connected State -->
    <div v-else class="flex items-center gap-2 sm:gap-3">
      <!-- Address Display with Copy -->
      <div class="group relative">
        <!-- Background glow -->
        <div class="absolute -inset-1 bg-linear-to-r from-indigo-600/20 to-cyan-500/20 rounded-xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
        
        <!-- Card -->
        <button
          @click="copyAddress"
          class="relative flex items-center gap-3 px-4 sm:px-5 py-2.5 sm:py-3 rounded-xl bg-linear-to-br from-white/10 to-white/5 backdrop-blur-xl border border-white/10 group-hover:border-indigo-400/40 group-hover:bg-white/15 transition-all duration-300 cursor-pointer"
          :title="authStore.publicKey ? authStore.publicKey : undefined"
        >
          <!-- Online indicator -->
          <div class="flex items-center gap-2">
            <div class="relative">
              <span class="w-2 h-2 rounded-full bg-linear-to-r from-emerald-400 to-cyan-400 animate-pulse block" />
              <span class="absolute inset-0 w-2 h-2 rounded-full bg-emerald-400 animate-ping" style="animation-duration: 1.5s;" />
            </div>
            <span class="font-mono text-xs sm:text-sm text-white/80 group-hover:text-white/90 transition-colors font-semibold">
              {{ authStore.publicKey?.slice(0, 6) }}...{{ authStore.publicKey?.slice(-4) }}
            </span>
          </div>

          <!-- Copy icon -->
          <svg
            class="w-4 h-4 sm:w-5 sm:h-5 text-white/40 group-hover:text-indigo-300 transition-all duration-300 opacity-0 group-hover:opacity-100 group-hover:scale-110"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path d="M8 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM15 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z" />
            <path d="M3 4a1 1 0 00-1 1v10a1 1 0 001 1h1.05a2.5 2.5 0 014.9 0H10a1 1 0 001-1V5a1 1 0 00-1-1H3zM14 7a1 1 0 00-1 1v6.05A2.5 2.5 0 0115.95 16H17a1 1 0 001-1v-5a1 1 0 00-.293-.707l-2-2A1 1 0 0015 7h-1z" />
          </svg>
        </button>

        <!-- Tooltip on copy -->
        <Transition name="fade-tooltip">
          <div
            v-if="copied"
            class="absolute top-full left-1/2 -translate-x-1/2 mt-3 px-4 py-2 rounded-lg bg-linear-to-r from-emerald-500/30 to-cyan-500/20 border border-emerald-400/50 text-emerald-300 text-xs font-bold whitespace-nowrap shadow-lg shadow-emerald-500/20"
          >
            ✓ Address copied!
          </div>
        </Transition>
      </div>

      <!-- Disconnect Button -->
      <button
        @click="authStore.logout"
        class="group relative px-4 sm:px-5 py-2.5 sm:py-3 rounded-xl font-bold text-sm text-white/70 hover:text-white overflow-hidden transition-all duration-300"
      >
        <!-- Gradient border -->
        <div class="absolute inset-0 rounded-xl border-2 border-white/10 group-hover:border-red-500/40 transition-colors duration-300" />
        
        <!-- Hover background -->
        <div class="absolute inset-0 bg-linear-to-r from-red-500/0 to-pink-500/0 group-hover:from-red-500/10 group-hover:to-pink-500/10 rounded-xl opacity-0 group-hover:opacity-100 transition-all duration-300" />
        
        <!-- Content -->
        <span class="relative flex items-center gap-2 justify-center">
          <svg class="w-4 h-4 sm:w-5 sm:h-5 transition-transform group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
          </svg>
          <span class="hidden sm:inline">Disconnect</span>
        </span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '~/stores/auth'

const authStore = useAuthStore()
const copied = ref(false)

async function copyAddress() {
  if (!authStore.publicKey) return

  try {
    await navigator.clipboard.writeText(authStore.publicKey)
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2500)
  } catch (err) {
    console.error('Failed to copy:', err)
  }
}
</script>

<style scoped>
/* Fade transition for tooltip */
.fade-tooltip-enter-active,
.fade-tooltip-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.fade-tooltip-enter-from {
  opacity: 0;
  transform: translate(-50%, -8px);
}

.fade-tooltip-leave-to {
  opacity: 0;
  transform: translate(-50%, -8px);
}

/* Smooth transitions */
button {
  @apply transition-all duration-300;
}

/* Icon animations */
svg {
  @apply transition-all duration-300;
}
</style>