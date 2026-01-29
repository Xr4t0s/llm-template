<template>
  <div class="space-y-8 w-full max-w-3xl">
    <!-- Header -->
    <div class="space-y-3">
      <h2 class="text-3xl font-bold text-white">
        Visual Direction
      </h2>
      <p class="text-white/60 leading-relaxed">
        Lock the artistic direction of your project. Consistency matters more
        than creativity at this stage.
      </p>
    </div>

    <!-- Visual vibe selection -->
    <div class="space-y-4">
      <label class="text-sm font-semibold text-white block">
        Visual vibe
      </label>
      <p class="text-xs text-white/50 -mt-2">
        Overall aesthetic and mood
      </p>

      <div class="flex flex-wrap gap-2">
        <button
          v-for="v in vibes"
          :key="v.value"
          @click="store.visualVibe = v.value"
          class="px-4 py-2 rounded-lg text-sm font-medium transition-all duration-300"
          :class="[
            store.visualVibe === v.value
              ? 'bg-linear-to-r from-indigo-600 to-cyan-500 text-white shadow-lg shadow-indigo-500/30'
              : 'bg-white/5 border border-white/20 text-white/70 hover:bg-white/10 hover:border-white/30'
          ]"
        >
          {{ v.label }}
        </button>
      </div>
    </div>

    <!-- Palette selection -->
    <div class="space-y-4">
      <div>
        <label class="text-sm font-semibold text-white block mb-2">
          Color palettes
        </label>
        <p class="text-xs text-white/50">
          Choose up to <strong>2 palettes</strong> to keep visual consistency
        </p>
      </div>

      <div class="space-y-3">
        <button
          v-for="p in palettes"
          :key="p.id"
          @click="togglePalette(p.id)"
          :disabled="store.palettes.length >= maxPalettes && !store.palettes.includes(p.id)"
          class="group relative w-full text-left transition-all"
        >
          <!-- Glow effect -->
          <div
            v-if="store.palettes.includes(p.id)"
            class="absolute inset-0 bg-linear-to-r from-emerald-600/20 to-cyan-500/20 rounded-xl blur opacity-100 transition-opacity duration-300"
          />

          <!-- Card -->
          <div
            class="relative bg-white/5 backdrop-blur-xl border rounded-xl p-4 transition-all duration-300"
            :class="[
              store.palettes.includes(p.id)
                ? 'border-emerald-500/50 bg-white/10 shadow-lg shadow-emerald-500/20'
                : 'border-white/20 hover:bg-white/10 hover:border-white/30',
              store.palettes.length >= maxPalettes && !store.palettes.includes(p.id) && 'opacity-50 cursor-not-allowed'
            ]"
          >
            <div class="flex items-center gap-4">
              <!-- Palette preview -->
              <div class="flex gap-2">
                <div
                  v-for="(color, idx) in p.chips"
                  :key="idx"
                  class="w-8 h-8 rounded-lg border border-white/20 shadow-lg"
                  :style="{ backgroundColor: color }"
                  :title="color"
                />
              </div>

              <!-- Content -->
              <div class="flex-1 min-w-0">
                <h3 class="font-semibold text-white text-sm">
                  {{ p.name }}
                </h3>
                <p class="text-xs text-white/60">
                  {{ p.subtitle }}
                </p>
              </div>

              <!-- Selection checkbox -->
              <div
                class="shrink-0 w-6 h-6 rounded-lg border-2 flex items-center justify-center transition-all"
                :class="
                  store.palettes.includes(p.id)
                    ? 'border-emerald-500 bg-emerald-500'
                    : 'border-white/20 group-hover:border-white/40'
                "
              >
                <svg v-if="store.palettes.includes(p.id)" class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
              </div>
            </div>
          </div>
        </button>
      </div>

      <!-- Selected counter -->
      <div class="text-xs text-white/50 font-mono text-center pt-2">
        {{ store.palettes.length }} / {{ maxPalettes }} selected
      </div>
    </div>

    <!-- Summary -->
    <div class="grid grid-cols-2 gap-4 pt-4">
      <!-- Vibe summary -->
      <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-lg p-4 space-y-1">
        <p class="text-xs uppercase tracking-widest text-white/40 font-semibold">
          Vibe
        </p>
        <p class="text-sm font-semibold text-white">
          {{ prettyVibe }}
        </p>
      </div>

      <!-- Palettes summary -->
      <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-lg p-4 space-y-1">
        <p class="text-xs uppercase tracking-widest text-white/40 font-semibold">
          Palettes
        </p>
        <p class="text-sm font-semibold text-white">
          {{ store.palettes.length > 0 ? store.palettes.join(', ') : '—' }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'

const store = useBuildProtocol()
const maxPalettes = 2

const vibes = [
  { value: 'clean' as const, label: '✨ Clean / Minimal' },
  { value: 'bold' as const, label: '💥 Bold / Loud' },
  { value: 'dark' as const, label: '🌙 Dark / Tech' },
  { value: 'meme' as const, label: '🎨 Meme / Chaotic' },
  { value: 'future' as const, label: '🔮 Futuristic' },
]

const palettes = [
  {
    id: 'indigo',
    name: 'Indigo / Neon',
    subtitle: 'Tech-forward, modern, clean',
    chips: ['#6366F1', '#22D3EE', '#0B1020', '#E5E7EB'],
  },
  {
    id: 'amber',
    name: 'Amber / Ink',
    subtitle: 'Premium, contrast, editorial',
    chips: ['#FBBF24', '#0B0F19', '#1F2937', '#E5E7EB'],
  },
  {
    id: 'rose',
    name: 'Rose / Night',
    subtitle: 'Expressive, bold, culture',
    chips: ['#FB7185', '#0F172A', '#334155', '#F1F5F9'],
  },
  {
    id: 'lime',
    name: 'Lime / Graphite',
    subtitle: 'Experimental, playful',
    chips: ['#A3E635', '#111827', '#374151', '#F9FAFB'],
  },
]

const prettyVibe = computed(() => {
  const map: Record<string, string> = {
    clean: 'Clean / Minimal',
    bold: 'Bold / Loud',
    dark: 'Dark / Tech',
    meme: 'Meme / Chaotic',
    future: 'Futuristic',
  }
  return map[store.visualVibe] || '—'
})

function togglePalette(id: string) {
  const idx = store.palettes.indexOf(id)
  if (idx >= 0) {
    store.palettes.splice(idx, 1)
  } else if (store.palettes.length < maxPalettes) {
    store.palettes.push(id)
  }
}
</script>