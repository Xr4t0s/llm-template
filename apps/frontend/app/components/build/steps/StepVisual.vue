<template>
  <section class="space-y-10">
    <!-- Header -->
    <header class="space-y-2">
      <h2 class="text-2xl font-semibold tracking-tight">
        Visual Direction
      </h2>
      <p class="text-sm text-(--text-soft) max-w-xl">
        Lock the artistic direction of your project. Consistency matters more
        than creativity at this stage.
      </p>
    </header>

    <!-- Visual vibe -->
    <div class="space-y-4">
      <div>
        <div class="text-sm font-semibold">
          Visual vibe
        </div>
        <div class="text-xs text-(--text-soft)">
          Overall aesthetic and mood.
        </div>
      </div>

      <div class="flex flex-wrap gap-2">
        <button
          v-for="v in vibes"
          :key="v.value"
          class="
            px-3
            py-1.5
            rounded-full
            text-xs
            transition-all
          "
          :class="
            store.visualVibe === v.value
              ? 'bg-white/20 text-white'
              : 'bg-white/5 hover:bg-white/10 text-(--text-soft)'
          "
          @click="store.visualVibe = v.value"
        >
          {{ v.label }}
        </button>
      </div>
    </div>

    <!-- Palette selection -->
    <div class="space-y-4">
      <div>
        <div class="text-sm font-semibold">
          Color palettes
        </div>
        <div class="text-xs text-(--text-soft)">
          Choose up to <strong>2</strong> palettes to keep visual consistency.
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <PaletteCard
          v-for="p in palettes"
          :key="p.id"
          :palette="p"
          :selected="store.palettes.includes(p.id)"
          :class="
            store.palettes.length >= maxPalettes &&
            !store.palettes.includes(p.id)
              ? 'opacity-40 cursor-not-allowed'
              : ''
          "
          @toggle="toggle(p.id)"
        />
      </div>

      <!-- Selected summary -->
      <div class="text-xs text-(--text-soft)">
        Selected palettes: {{ store.palettes.length }} / {{ maxPalettes }}
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useBuildProtocol } from '~/stores/buildProtocol'
import PaletteCard from '../ui/PaletteCard.vue'

const store = useBuildProtocol()
const maxPalettes = 2

const vibes = [
  { value: 'clean', label: 'Clean / Minimal' },
  { value: 'bold', label: 'Bold / Loud' },
  { value: 'dark', label: 'Dark / Tech' },
  { value: 'meme', label: 'Meme / Chaotic' },
  { value: 'future', label: 'Futuristic' },
] as const

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
] as const

function toggle(id: string) {
  const i = store.palettes.indexOf(id)

  if (i >= 0) {
    store.palettes.splice(i, 1)
    return
  }

  if (store.palettes.length >= maxPalettes) return

  store.palettes.push(id)
}
</script>
