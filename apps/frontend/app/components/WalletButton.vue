<template>
  <div class="flex items-center gap-3">
    <!-- Not Connected State -->
    <button
      v-if="!authStore.isConnected"
      @click="authStore.connect"
      :disabled="authStore.isLoading"
      class="group relative px-6 py-2.5 rounded-lg font-medium text-sm text-white overflow-hidden disabled:opacity-50 disabled:cursor-not-allowed transition-all"
    >
      <!-- Gradient background -->
      <div class="absolute inset-0 bg-gradient-to-r from-indigo-600 to-cyan-500 opacity-100 group-hover:opacity-90 group-disabled:opacity-70 transition-opacity" />
      <!-- Shimmer effect -->
      <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full group-disabled:translate-x-full transition-transform duration-500" />
      <!-- Content -->
      <span class="relative flex items-center gap-2">
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
          <svg class="w-4 h-4 inline mr-1" fill="currentColor" viewBox="0 0 20 20">
            <path d="M18 9a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          {{ authStore.isLoading ? 'Connecting...' : 'Connect Wallet' }}
        </span>
      </span>
    </button>

    <!-- Connected State -->
    <div v-else class="flex items-center gap-3">
      <!-- Address Display with Copy -->
      <div class="group relative">
        <!-- Background glow -->
        <div class="absolute inset-0 bg-gradient-to-r from-indigo-600/20 to-cyan-500/20 rounded-lg blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
        <!-- Card -->
        <button
          @click="copyAddress"
          class="relative flex items-center gap-2 px-4 py-2.5 rounded-lg bg-white/5 backdrop-blur-xl border border-white/20 group-hover:border-white/30 group-hover:bg-white/10 transition-all duration-300 cursor-pointer"
          :title="authStore.publicKey ? authStore.publicKey : undefined"
        >
          <!-- Online indicator -->
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-gradient-to-r from-green-400 to-emerald-500 animate-pulse" />
            <span class="font-mono text-xs text-white/80">
              {{ authStore.publicKey?.slice(0, 6) }}...{{ authStore.publicKey?.slice(-4) }}
            </span>
          </div>

          <!-- Copy icon -->
          <svg
            class="w-4 h-4 text-white/50 group-hover:text-white/80 transition-colors opacity-0 group-hover:opacity-100"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path d="M7 9a2 2 0 11-4 0 2 2 0 014 0z" />
            <path fill-rule="evenodd" d="M7.465 11.293a1 1 0 001.414 0l2.828-2.829a1 1 0 00-1.414-1.414L8 9.172V5a1 1 0 00-2 0v4.172L5.05 7.05a1 1 0 00-1.414 1.414l2.828 2.829z" clip-rule="evenodd" />
          </svg>
        </button>

        <!-- Tooltip on copy -->
        <Transition name="fade">
          <div
            v-if="copied"
            class="absolute top-full left-1/2 -translate-x-1/2 mt-2 px-3 py-1.5 rounded-lg bg-emerald-500/20 border border-emerald-500/30 text-emerald-300 text-xs font-medium whitespace-nowrap"
          >
            ✓ Copied!
          </div>
        </Transition>
      </div>

      <!-- Disconnect Button -->
      <button
        @click="authStore.logout"
        class="group relative px-4 py-2.5 rounded-lg font-medium text-sm text-white/80 overflow-hidden transition-all hover:text-white"
      >
        <!-- Border -->
        <div class="absolute inset-0 border border-white/20 rounded-lg group-hover:border-red-500/50 transition-colors" />
        <!-- Hover background -->
        <div class="absolute inset-0 bg-red-500/10 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity" />
        <!-- Content -->
        <span class="relative flex items-center gap-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
          </svg>
          Disconnect
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
    }, 2000)
  } catch (err) {
    console.error('Failed to copy:', err)
  }
}
</script>

<style scoped>
/* Fade transition for tooltip */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>