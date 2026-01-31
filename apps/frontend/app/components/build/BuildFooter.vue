<template>
  <div class="mt-auto pt-8 border-t border-white/10 space-y-6">
    <!-- Hint / Helper text -->
    <div class="flex items-start gap-3 px-5 py-4 rounded-xl bg-linear-to-r from-cyan-500/15 to-emerald-500/10 border border-cyan-400/30">
      <svg class="w-5 h-5 text-cyan-400 shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
      </svg>
      <p class="text-sm text-cyan-300 leading-relaxed">
        <span class="font-semibold">{{ hint }}</span>
      </p>
    </div>

    <!-- Actions -->
    <div class="flex gap-3 sm:gap-4">
      <!-- Back button -->
      <button
        @click="store.prev()"
        :disabled="store.step === 1"
        class="group relative px-6 sm:px-8 py-3 sm:py-4 rounded-xl font-bold text-white/70 hover:text-white overflow-hidden disabled:opacity-40 disabled:cursor-not-allowed transition-all"
      >
        <!-- Border -->
        <div class="absolute inset-0 border-2 border-white/20 rounded-xl group-hover:border-white/40 transition-colors" />
        
        <!-- Hover background -->
        <div class="absolute inset-0 bg-white/5 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity" />

        <!-- Content -->
        <span class="relative flex items-center justify-center gap-2">
          <svg class="w-5 h-5 group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7" />
          </svg>
          <span class="hidden sm:inline">Back</span>
        </span>
      </button>

      <!-- Next / Launch button -->
      <button
        @click="onPrimary"
        :disabled="!store.canGoNext || isLoading"
        class="flex-1 group relative px-6 sm:px-8 py-3 sm:py-4 rounded-xl font-bold text-white text-base overflow-hidden disabled:opacity-50 disabled:cursor-not-allowed transition-all"
      >
        <!-- Gradient background -->
        <div class="absolute inset-0 bg-linear-to-r from-indigo-600 via-indigo-500 to-cyan-500 opacity-100 group-hover:opacity-90 group-disabled:opacity-70 transition-opacity rounded-xl" />
        
        <!-- Shimmer effect -->
        <div class="absolute inset-0 bg-linear-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full group-disabled:translate-x-0 transition-transform duration-700 rounded-xl" />

        <!-- Content -->
        <span class="relative flex items-center justify-center gap-3">
          <svg v-if="isLoading" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
          </svg>
          <span v-else class="text-lg">🚀</span>
          
          <span>
            {{ isLoading ? 'Launching...' : primaryLabel }}
          </span>
          
          <svg
            v-if="!isLoading"
            class="w-5 h-5 group-hover:translate-x-1 transition-transform"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 7l5 5m0 0l-5 5m5-5H6" />
          </svg>
        </span>
      </button>
    </div>

    <!-- Step counter indicator -->
    <div class="text-center text-xs text-white/40 font-mono tracking-widest uppercase">
      Step {{ String(store.step).padStart(2, '0') }} of 05
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'
import { useAuthStore } from '~/stores/auth'

const store = useBuildProtocol()
const authStore = useAuthStore()
const isLoading = ref(false)

const hints = [
  '💡 Write a short but meaningful lore for your project.',
  '🎯 Choose the category that fits your vision best.',
  '🎨 Select 2-3 colors to keep consistency.',
  '📦 Choose the outputs you need.',
  '✅ Everything looks good. Time to launch!',
]

const hint = computed(() => hints[store.step - 1])

const primaryLabel = computed(() =>
  store.step === 5 ? 'Launch Build' : 'Continue'
)

async function onPrimary() {
  if (!store.canGoNext) return
  
  if (store.step === 5) {
    await launchBuild()
  } else {
    store.next()
  }
}

async function launchBuild() {
  if (isLoading.value) return
  
  isLoading.value = true

  try {
    const payload = {
      lore: store.lore,
      hasMascot: store.hasMascot,
      tone: store.tone,
      projectType: store.projectType,
      goal: store.goal,
      visualVibe: store.visualVibe,
      palettes: store.palettes,
      outputs: store.outputs,
    }

    const res = await fetch('/api/v1/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${authStore.token}`,
      },
      body: JSON.stringify(payload),
    })

    if (!res.ok) {
      const error = await res.json()
      throw new Error(error.message || 'Build failed')
    }

    const data = await res.json()
    
    // Mark build as done
    store.buildDone = true
    
    // Optional: Navigate to results
    // navigateTo(`/build/results/${data.buildId}`)
    
  } catch (err) {
    console.error('Build error:', err)
    
    // TODO: Show error toast notification
    // toast.error(`Build failed: ${err.message}`)
    
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
/* Smooth transitions */
button {
  @apply transition-all duration-300;
}

/* Icon animations */
svg {
  @apply transition-all duration-300;
}
</style>