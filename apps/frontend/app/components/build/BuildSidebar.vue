<template>
  <div class="space-y-4">
    <!-- Title -->
    <div class="px-4 py-3 space-y-1">
      <p class="text-xs uppercase tracking-widest text-white/40 font-semibold">Build Steps</p>
    </div>

    <!-- Steps navigation -->
    <nav class="space-y-2">
      <button
        v-for="s in steps"
        :key="s.id"
        @click="goTo(s.id)"
        :disabled="s.id > store.step"
        class="w-full group relative"
      >
        <!-- Background glow for active -->
        <div
          v-if="s.id === store.step"
          class="absolute inset-0 bg-linear-to-r from-indigo-600/20 to-cyan-500/20 rounded-xl blur transition-opacity duration-300"
        />

        <!-- Card -->
        <div
          class="relative px-4 py-3 rounded-xl border transition-all duration-300 flex items-center gap-3"
          :class="[
            s.id === store.step && 'bg-white/10 border-indigo-500/50 text-white shadow-lg shadow-indigo-500/20',
            s.id < store.step && 'bg-white/5 border-white/10 text-white/70 hover:bg-white/10 hover:border-white/20 cursor-pointer',
            s.id > store.step && 'bg-white/5 border-white/10 text-white/40 cursor-not-allowed opacity-60',
          ]"
        >
          <!-- Step indicator circle -->
          <div
            class="relative w-8 h-8 rounded-lg flex items-center justify-center font-semibold text-sm transition-all duration-300"
            :class="[
              s.id === store.step && 'bg-linear-to-br from-indigo-500 to-cyan-400 text-white shadow-lg shadow-indigo-500/50',
              s.id < store.step && 'bg-emerald-500/30 text-emerald-300 border border-emerald-500/50',
              s.id > store.step && 'bg-white/10 text-white/40 border border-white/10',
            ]"
          >
            <span v-if="s.id < store.step" class="text-lg">✓</span>
            <span v-else>{{ s.id }}</span>
          </div>

          <!-- Step info -->
          <div class="flex-1 text-left space-y-0.5 min-w-0">
            <p class="font-semibold text-sm truncate">
              {{ s.title }}
            </p>
            <p
              v-if="s.id === store.step"
              class="text-xs text-white/60 truncate"
            >
              {{ s.label }}
            </p>
          </div>

          <!-- Arrow for active/completed -->
          <div
            v-if="s.id <= store.step"
            class="flex-shrink-0 w-4 h-4 opacity-0 group-hover:opacity-100 transition-opacity text-white/40"
          >
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </div>
        </div>
      </button>
    </nav>

    <!-- Current step indicator -->
    <div class="px-4 py-3 mt-6 pt-6 border-t border-white/10 space-y-2">
      <p class="text-xs uppercase tracking-widest text-white/40 font-semibold">Current Step</p>
      <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-lg p-3 space-y-1">
        <p class="text-sm font-semibold text-white">
          {{ currentStep!.title }}
        </p>
        <p class="text-xs text-white/50">
          {{ currentStep!.label }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'

const store = useBuildProtocol()

const steps = [
  { id: 1, title: 'Identity', label: 'Project lore and tone' },
  { id: 2, title: 'Project', label: 'Type and category' },
  { id: 3, title: 'Visual', label: 'Colors and vibe' },
  { id: 4, title: 'Outputs', label: 'Generation config' },
  { id: 5, title: 'Review', label: 'Final check & launch' },
]

const currentStep = computed(
  () => steps.find(s => s.id === store.step) ?? steps[0]
)

function goTo(id: number) {
  if (id <= store.step) store.goTo(id)
}
</script>