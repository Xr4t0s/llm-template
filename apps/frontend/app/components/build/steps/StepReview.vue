<template>
  <section class="space-y-10">
    <!-- Header -->
    <header class="space-y-2">
      <h2 class="text-2xl font-semibold tracking-tight">
        Review & Launch
      </h2>
      <p class="text-sm text-(--text-soft) max-w-xl">
        Review your project configuration before launching the build.
        This will generate all selected assets and documentation.
      </p>
    </header>

    <!-- Summary blocks -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <!-- Identity -->
      <div class="rounded-2xl border border-white/10 bg-white/5 p-4 space-y-3">
        <div class="text-xs uppercase tracking-wide text-(--text-soft)">
          Identity
        </div>

        <InfoPill
          label="Lore"
          :value="store.lore || '—'"
        />

        <div class="grid grid-cols-2 gap-2">
          <InfoPill
            label="Mascot"
            :value="store.hasMascot ? 'Yes' : 'No'"
          />
          <InfoPill
            label="Tone"
            :value="store.tone"
          />
        </div>
      </div>

      <!-- Project -->
      <div class="rounded-2xl border border-white/10 bg-white/5 p-4 space-y-3">
        <div class="text-xs uppercase tracking-wide text-(--text-soft)">
          Project
        </div>

        <div class="grid grid-cols-2 gap-2">
          <InfoPill
            label="Type"
            :value="prettyProjectType"
          />
          <InfoPill
            label="Goal"
            :value="prettyGoal"
          />
        </div>
      </div>

      <!-- Visual -->
      <div class="rounded-2xl border border-white/10 bg-white/5 p-4 space-y-3">
        <div class="text-xs uppercase tracking-wide text-(--text-soft)">
          Visual direction
        </div>

        <div class="grid grid-cols-2 gap-2">
          <InfoPill
            label="Vibe"
            :value="prettyVibe"
          />
          <InfoPill
            label="Palettes"
            :value="prettyPalettes"
          />
        </div>
      </div>

      <!-- Outputs -->
      <div class="rounded-2xl border border-white/10 bg-white/5 p-4 space-y-3">
        <div class="text-xs uppercase tracking-wide text-(--text-soft)">
          Outputs
        </div>

        <div class="flex flex-wrap gap-2">
          <span
            v-for="tag in selectedOutputs"
            :key="tag"
            class="px-2 py-1 rounded-full text-xs bg-white/10"
          >
            {{ tag }}
          </span>
          <span
            v-if="selectedOutputs.length === 0"
            class="text-xs text-(--text-soft)"
          >
            —
          </span>
        </div>
      </div>
    </div>

    <!-- Final action -->
    <div
      class="
        flex
        flex-col
        md:flex-row
        md:items-center
        md:justify-between
        gap-4
        pt-6
        border-t
        border-white/10
      "
    >
      <div class="text-xs text-(--text-soft) max-w-md">
        Once launched, the build process will generate the selected assets
        following the defined direction. You’ll be able to edit and regenerate
        outputs later.
      </div>

      <button
        class="
          px-6
          py-3
          rounded-xl
          text-sm
          font-semibold
          bg-white/15
          hover:bg-white/25
          transition-all
        "
        @click="build"
      >
        Launch build
      </button>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'
import InfoPill from '../ui/InfoPill.vue'

const store = useBuildProtocol()

/* ---------- prettifiers ---------- */

const prettyProjectType = computed(() => {
  if (store.projectType === 'meme') return 'Meme project'
  if (store.projectType === 'tool') return 'Tool / App'
  if (store.projectType === 'defi') return 'DeFi'
  return '—'
})

const prettyGoal = computed(() => {
  if (store.goal === 'community') return 'Community'
  if (store.goal === 'utility') return 'Utility'
  if (store.goal === 'experiment') return 'Experiment'
  if (store.goal === 'launch') return 'Launch-ready'
  return '—'
})

const prettyVibe = computed(() => {
  if (store.visualVibe === 'clean') return 'Clean / Minimal'
  if (store.visualVibe === 'bold') return 'Bold / Loud'
  if (store.visualVibe === 'dark') return 'Dark / Tech'
  if (store.visualVibe === 'meme') return 'Meme / Chaotic'
  if (store.visualVibe === 'future') return 'Futuristic'
  return '—'
})

const prettyPalettes = computed(() =>
  store.palettes.length ? store.palettes.join(', ') : '—'
)

const selectedOutputs = computed(() => {
  const map: Record<string, string> = {
    logo: 'Logos',
    banner: 'Banners',
    pfp: 'PFP',
    announcements: 'Announcements',
    memes: 'Memes',
    stickers: 'Stickers',
    documentation: 'Documentation',
    onepager: 'One-pager',
    roadmap: 'Roadmap',
    faq: 'FAQ',
  }

  return Object.entries(store.outputs)
    .filter(([, v]) => v)
    .map(([k]) => map[k] ?? k)
})

/* ---------- action ---------- */

function build() {
  const payload = { ...store.$state }
  console.log('BUILD PAYLOAD', payload)

  // Ici tu brancheras l’appel Nest plus tard
}
</script>
