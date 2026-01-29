<template>
  <div class="space-y-8 w-full max-w-3xl">
    <!-- Header -->
    <div class="space-y-3">
      <h2 class="text-3xl font-bold text-white">
        Review & Launch
      </h2>
      <p class="text-white/60 leading-relaxed">
        Review your project configuration before launching the build.
        This will generate all selected assets and documentation.
      </p>
    </div>

    <!-- Summary grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <!-- Identity block -->
      <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-5 space-y-4">
        <p class="text-xs uppercase tracking-widest text-white/40 font-semibold">
          🎭 Identity
        </p>

        <div class="space-y-3">
          <!-- Lore preview -->
          <div class="bg-white/5 rounded-lg p-3 space-y-1 max-h-32 overflow-y-auto">
            <p class="text-xs text-white/50 font-semibold">Lore</p>
            <p class="text-xs text-white/70 leading-relaxed font-mono">
              {{ store.lore || '—' }}
            </p>
          </div>

          <!-- Grid info -->
          <div class="grid grid-cols-2 gap-2">
            <div class="text-center p-2 rounded-lg bg-white/10 border border-white/10">
              <p class="text-xs text-white/50 mb-1">Mascot</p>
              <p class="text-sm font-semibold text-white">
                {{ store.hasMascot ? '✓' : '—' }}
              </p>
            </div>
            <div class="text-center p-2 rounded-lg bg-white/10 border border-white/10">
              <p class="text-xs text-white/50 mb-1">Tone</p>
              <p class="text-sm font-semibold text-white">{{ store.tone }}</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Project block -->
      <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-5 space-y-4">
        <p class="text-xs uppercase tracking-widest text-white/40 font-semibold">
          🎯 Project
        </p>

        <div class="grid grid-cols-2 gap-3">
          <div class="text-center p-3 rounded-lg bg-white/10 border border-white/10">
            <p class="text-xs text-white/50 mb-2">Type</p>
            <p class="text-sm font-semibold text-white">
              {{ prettyProjectType }}
            </p>
          </div>
          <div class="text-center p-3 rounded-lg bg-white/10 border border-white/10">
            <p class="text-xs text-white/50 mb-2">Goal</p>
            <p class="text-sm font-semibold text-white">{{ prettyGoal }}</p>
          </div>
        </div>
      </div>

      <!-- Visual block -->
      <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-5 space-y-4">
        <p class="text-xs uppercase tracking-widest text-white/40 font-semibold">
          🎨 Visual Direction
        </p>

        <div class="grid grid-cols-2 gap-3">
          <div class="text-center p-3 rounded-lg bg-white/10 border border-white/10">
            <p class="text-xs text-white/50 mb-2">Vibe</p>
            <p class="text-xs font-semibold text-white">
              {{ prettyVibe }}
            </p>
          </div>
          <div class="text-center p-3 rounded-lg bg-white/10 border border-white/10">
            <p class="text-xs text-white/50 mb-2">Palettes</p>
            <p class="text-xs font-semibold text-white">
              {{ store.palettes.length > 0 ? store.palettes.join(' + ') : '—' }}
            </p>
          </div>
        </div>
      </div>

      <!-- Outputs block -->
      <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-5 space-y-4">
        <p class="text-xs uppercase tracking-widest text-white/40 font-semibold">
          📦 Outputs
        </p>

        <div class="flex flex-wrap gap-2">
          <span
            v-for="tag in selectedOutputs"
            :key="tag"
            class="px-2.5 py-1.5 rounded-lg bg-linear-to-r from-indigo-500/20 to-cyan-500/20 border border-indigo-500/30 text-xs font-medium text-indigo-300"
          >
            {{ tag }}
          </span>
          <span
            v-if="selectedOutputs.length === 0"
            class="text-xs text-white/50 italic"
          >
            No outputs selected
          </span>
        </div>
      </div>
    </div>

    <!-- Launch section -->
    <div class="space-y-4 pt-6 border-t border-white/10">
      <div class="flex items-start gap-3 p-4 rounded-lg bg-cyan-500/10 border border-cyan-500/20">
        <svg class="w-5 h-5 text-cyan-400 shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
        </svg>
        <div>
          <p class="text-sm text-cyan-300 font-medium mb-1">Ready to launch?</p>
          <p class="text-xs text-cyan-300/70">
            Once launched, the build process will generate all selected assets following the defined direction.
            You can edit and regenerate outputs later.
          </p>
        </div>
      </div>

      <button
        @click="launchBuild"
        :disabled="selectedOutputs.length === 0"
        class="w-full group relative px-8 py-4 rounded-xl font-semibold text-white overflow-hidden disabled:opacity-50 disabled:cursor-not-allowed transition-all"
      >
        <!-- Gradient background -->
        <div class="absolute inset-0 bg-linear-to-r from-indigo-600 to-cyan-500 opacity-100 group-hover:opacity-90 group-disabled:opacity-70 transition-opacity" />
        <!-- Shimmer effect -->
        <div class="absolute inset-0 bg-linear-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full group-disabled:translate-x-full transition-transform duration-500" />
        <!-- Content -->
        <span class="relative flex items-center justify-center gap-2">
          <span class="text-lg">🚀</span>
          Launch build
        </span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'
import { useAuthStore } from '~/stores/auth'

const store = useBuildProtocol()
const authStore = useAuthStore()

const prettyProjectType = computed(() => {
  const map: Record<string, string> = {
    meme: 'Meme project',
    tool: 'Tool / App',
    defi: 'DeFi',
  }
  return map[store.projectType] || '—'
})

const prettyGoal = computed(() => {
  const map: Record<string, string> = {
    community: 'Community',
    utility: 'Utility',
    experiment: 'Experiment',
    launch: 'Launch-ready',
  }
  return map[store.goal] || '—'
})

const prettyVibe = computed(() => {
  const map: Record<string, string> = {
    clean: 'Clean',
    bold: 'Bold',
    dark: 'Dark',
    meme: 'Meme',
    future: 'Future',
  }
  return map[store.visualVibe] || '—'
})

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

async function launchBuild() {
  if (selectedOutputs.value.length === 0) return

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

  try {
    const res = await fetch('/api/v1/generate/doc', {
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

    store.buildDone = true
  } catch (err) {
    console.error('Build error:', err)
    // Handle error - maybe show toast notification
  }
}
</script>