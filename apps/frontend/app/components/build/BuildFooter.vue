<template>
  <div class="mt-auto pt-8 border-t border-white/10 space-y-6">
    <!-- Hint / Helper text -->
    <div class="flex items-center gap-3 px-4 py-3 rounded-lg bg-cyan-500/10 border border-cyan-500/20">
      <svg class="w-5 h-5 text-cyan-400 shrink-0" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
      </svg>
      <p class="text-sm text-cyan-300">
        {{ hint }}
      </p>
    </div>

    <!-- Actions -->
    <div class="flex gap-4">
      <!-- Back button -->
      <button
        @click="store.prev()"
        :disabled="store.step === 1"
        class="flex-1 group relative px-6 py-3 rounded-xl font-semibold text-white/70 overflow-hidden disabled:opacity-40 disabled:cursor-not-allowed transition-all"
      >
        <!-- Border and hover effect -->
        <div class="absolute inset-0 border border-white/20 rounded-xl group-hover:border-white/30 transition-colors" />
        <div class="absolute inset-0 bg-white/5 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity" />

        <!-- Content -->
        <span class="relative flex items-center justify-center gap-2">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
          Back
        </span>
      </button>

      <!-- Next / Launch button -->
      <button
        @click="onPrimary"
        :disabled="!store.canGoNext"
        class="flex-1 group relative px-6 py-3 rounded-xl font-semibold text-white overflow-hidden disabled:opacity-40 disabled:cursor-not-allowed transition-all"
      >
        <!-- Gradient background -->
        <div class="absolute inset-0 bg-linear-to-r from-indigo-600 to-cyan-500 opacity-100 group-hover:opacity-90 transition-opacity rounded-xl" />
        <!-- Shimmer effect -->
        <div class="absolute inset-0 bg-linear-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-500 rounded-xl" />

        <!-- Content -->
        <span class="relative flex items-center justify-center gap-2">
          <span class="text-lg">🚀</span>
          {{ primaryLabel }}
          <svg
            class="w-5 h-5 group-hover:translate-x-1 transition-transform"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
          </svg>
        </span>
      </button>
    </div>

    <!-- Step counter indicator -->
    <div class="text-center text-xs text-white/40 font-mono">
      Step {{ String(store.step).padStart(2, '0') }} of 05
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'

const store = useBuildProtocol()

const hints = [
  '💡 Write a short but meaningful lore for your project.',
  '🎯 Choose the category that fits your vision best.',
  '🎨 Limit palettes to 2-3 colors to keep consistency.',
  '📦 Select only the outputs you need right now.',
  '✅ Everything is ready. Time to launch the build!',
]

const hint = computed(() => hints[store.step - 1])

const primaryLabel = computed(() =>
  store.step === 5 ? '🚀 Launch build' : 'Continue'
)

function onPrimary() {
  if (!store.canGoNext) return
  store.step === 5 ? launch() : store.next()
}

function launch() {
  console.log('BUILD PAYLOAD', { ...store.$state })
  // Add actual launch logic here
}
</script>