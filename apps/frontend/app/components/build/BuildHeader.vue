<template>
  <div class="space-y-6">
    <!-- Title section -->
    <div class="space-y-3">
      <div class="flex items-baseline gap-3">
        <h1 class="text-5xl font-bold text-white">
          Build
        </h1>
        <span class="text-lg text-white/40 font-mono">
          {{ String(store.step).padStart(2, '0') }} / {{ String(totalSteps).padStart(2, '0') }}
        </span>
      </div>
      <p class="text-lg text-white/60">
        {{ currentStep!.subtitle }}
      </p>
    </div>

    <!-- Progress Section -->
    <div class="space-y-2">
      <div class="flex items-center justify-between text-sm">
        <span class="text-white/50 uppercase tracking-wider font-medium">Progress</span>
        <span class="text-white font-mono font-semibold">{{ Math.round(progress) }}%</span>
      </div>

      <!-- Main progress bar with glow -->
      <div class="relative h-2 bg-white/10 rounded-full overflow-hidden border border-white/20">
        <div
          class="h-full bg-gradient-to-r from-indigo-500 via-cyan-400 to-emerald-400 rounded-full transition-all duration-500 ease-out shadow-lg shadow-indigo-500/50"
          :style="{ width: `${progress}%` }"
        />
        <div
          class="absolute inset-0 bg-gradient-to-r from-indigo-400 via-cyan-300 to-emerald-300 opacity-0 blur-lg transition-opacity duration-500"
          :style="{ width: `${progress}%`, opacity: Math.min(progress / 100 * 0.3, 0.3) }"
        />
      </div>
    </div>

    <!-- Step dots indicator -->
    <div class="flex gap-2 pt-4">
      <button
        v-for="s in steps"
        :key="s.id"
        @click="goTo(s.id)"
        :disabled="s.id > store.step"
        class="group relative"
        :title="s.subtitle"
      >
        <div
          class="w-3 h-3 rounded-full transition-all duration-300"
          :class="[
            s.id === store.step && 'bg-gradient-to-r from-indigo-400 to-cyan-400 shadow-lg shadow-indigo-500/50 scale-125',
            s.id < store.step && 'bg-emerald-500 hover:bg-emerald-400',
            s.id > store.step && 'bg-white/20 cursor-not-allowed',
          ]"
        />
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'

const store = useBuildProtocol()

const steps = [
  { id: 1, subtitle: 'Define the identity and lore' },
  { id: 2, subtitle: 'Choose the project type' },
  { id: 3, subtitle: 'Lock the visual direction' },
  { id: 4, subtitle: 'Select outputs to generate' },
  { id: 5, subtitle: 'Review and launch the build' },
]

const currentStep = computed(
  () => steps.find(s => s.id === store.step) ?? steps[0]
)

const totalSteps = steps.length

const progress = computed(() => ((store.step - 1) / (totalSteps - 1)) * 100)

function goTo(id: number) {
  if (id <= store.step) store.goTo(id)
}
</script>