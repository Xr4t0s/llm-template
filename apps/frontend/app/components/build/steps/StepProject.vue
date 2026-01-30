<template>
  <div class="space-y-8 w-full max-w-3xl">
    <!-- Header -->
    <div class="space-y-3">
      <h2 class="text-3xl font-bold text-white">
        Project Type
      </h2>
      <p class="text-white/60 leading-relaxed">
        Choose the category that best defines your project.
        This will influence structure, visuals, and documentation.
      </p>
    </div>

    <!-- Project type cards -->
    <div class="space-y-4">
      <label class="text-sm font-semibold text-white block">
        What type of project is this?
      </label>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <button
          v-for="t in types"
          :key="t.value"
		  @click="store.projectType === t.value
		  	? store.projectType = ''
			: store.projectType = t.value"
          class="group relative text-left"
        >
          <!-- Glow background -->
          <div
            v-if="store.projectType === t.value"
            class="absolute inset-0 bg-linear-to-br from-indigo-600/20 to-cyan-500/20 rounded-xl blur opacity-100 transition-opacity duration-300"
          />

          <!-- Card -->
          <div
            class="relative bg-white/5 backdrop-blur-xl border rounded-xl p-5 transition-all duration-300"
            :class="[
              store.projectType === t.value
                ? 'border-indigo-500/50 bg-white/10 shadow-lg shadow-indigo-500/20'
                : 'border-white/20 hover:bg-white/10 hover:border-white/30'
            ]"
          >
            <!-- Content -->
            <div class="space-y-2 mb-4">
              <h3 class="font-semibold text-white">
                {{ t.title }}
              </h3>
              <p class="text-xs text-white/60">
                {{ t.desc }}
              </p>
            </div>

            <!-- Selection indicator -->
            <div
              class="text-xs font-semibold px-3 py-1 rounded-full inline-flex items-center gap-2 transition-all"
              :class="
                store.projectType === t.value
                  ? 'bg-emerald-500/20 text-emerald-300'
                  : 'bg-white/10 text-white/40 group-hover:text-white/60'
              "
            >
              <span v-if="store.projectType === t.value" class="text-sm">✓</span>
              {{ store.projectType === t.value ? 'Selected' : 'Choose' }}
            </div>
          </div>
        </button>
      </div>
    </div>

    <!-- Primary goal section -->
    <div class="space-y-4">
      <label class="text-sm font-semibold text-white block">
        Primary goal
      </label>
      <p class="text-xs text-white/50 -mt-2">
        What is the main intention behind this project?
      </p>

      <div class="flex flex-wrap gap-2">
        <button
          v-for="g in goals"
          :key="g.value"
          @click="store.goal === g.value
		  	? store.goal = ''
			: store.goal = g.value"
          class="px-4 py-2 rounded-lg text-sm font-medium transition-all duration-300"
          :class="[
            store.goal === g.value
              ? 'bg-linear-to-r from-indigo-600 to-cyan-500 text-white shadow-lg shadow-indigo-500/30'
              : 'bg-white/5 border border-white/20 text-white/70 hover:bg-white/10 hover:border-white/30'
          ]"
        >
          {{ g.label }}
        </button>
      </div>
    </div>

    <!-- Summary cards -->
    <div class="grid grid-cols-2 gap-4 pt-4">
      <!-- Type summary -->
      <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-lg p-4 space-y-1">
        <p class="text-xs uppercase tracking-widest text-white/40 font-semibold">
          Selected Type
        </p>
        <p class="text-sm font-semibold text-white">
          {{ prettyProjectType }}
        </p>
      </div>

      <!-- Goal summary -->
      <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-lg p-4 space-y-1">
        <p class="text-xs uppercase tracking-widest text-white/40 font-semibold">
          Goal
        </p>
        <p class="text-sm font-semibold text-white">
          {{ prettyGoal }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'

const store = useBuildProtocol()

const types = [
  {
    value: 'meme' as const,
    title: 'Meme Project',
    desc: 'Community-first, viral, and expressive. Strong identity.',
  },
  {
    value: 'tool' as const,
    title: 'Tool / App',
    desc: 'Utility-driven solving a specific problem.',
  },
  {
    value: 'defi' as const,
    title: 'DeFi (simple)',
    desc: 'Protocol or financial primitive with clear mechanics.',
  },
]

const goals = [
  { value: 'community' as const, label: '👥 Community & culture' },
  { value: 'utility' as const, label: '⚡ Utility & adoption' },
  { value: 'experiment' as const, label: '🧪 Experiment / concept' },
  { value: 'launch' as const, label: '🚀 Launch-ready product' },
]

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
</script>