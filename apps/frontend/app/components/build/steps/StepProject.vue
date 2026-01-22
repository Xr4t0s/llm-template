<template>
  <section class="space-y-10">
    <!-- Header -->
    <header class="space-y-2">
      <h2 class="text-2xl font-semibold tracking-tight">
        Project Type
      </h2>
      <p class="text-sm text-(--text-soft) max-w-xl">
        Choose the category that best defines the nature of your project.
        This will influence structure, visuals, and documentation.
      </p>
    </header>

    <!-- Project type cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <button
        v-for="t in types"
        :key="t.value"
        class="
          group
          relative
          rounded-2xl
          border
          transition-all
          text-left
          overflow-hidden
        "
        :class="
          store.projectType === t.value
            ? 'border-white/30 bg-white/10'
            : 'border-white/10 bg-white/5 hover:bg-white/7'
        "
        @click="store.projectType = t.value"
      >
        <!-- Glow -->
        <div
          v-if="store.projectType === t.value"
          class="
            pointer-events-none
            absolute
            inset-0
            opacity-30
            bg-linear-to-br
            from-white/20
            to-transparent
          "
        />

        <div class="relative p-5 space-y-3">
          <div class="text-sm font-semibold">
            {{ t.title }}
          </div>

          <div class="text-xs text-(--text-soft)">
            {{ t.desc }}
          </div>

          <!-- Selected indicator -->
          <div
            class="
              pt-2
              text-xs
              font-medium
              transition-opacity
            "
            :class="
              store.projectType === t.value
                ? 'opacity-100 text-white'
                : 'opacity-0 group-hover:opacity-100 text-(--text-soft)'
            "
          >
            {{ store.projectType === t.value ? 'Selected' : 'Choose this' }}
          </div>
        </div>
      </button>
    </div>

    <!-- Intent / Goal -->
    <div class="space-y-4">
      <div>
        <div class="text-sm font-semibold">
          Primary goal
        </div>
        <div class="text-xs text-(--text-soft)">
          What is the main intention behind this project?
        </div>
      </div>

      <div class="flex flex-wrap gap-2">
        <button
          v-for="g in goals"
          :key="g.value"
          class="
            px-3
            py-1.5
            rounded-full
            text-xs
            transition-all
          "
          :class="
            store.goal === g.value
              ? 'bg-white/20 text-white'
              : 'bg-white/5 hover:bg-white/10 text-(--text-soft)'
          "
          @click="store.goal = g.value"
        >
          {{ g.label }}
        </button>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useBuildProtocol } from '~/stores/buildProtocol'

const store = useBuildProtocol()

const types = [
  {
    value: 'meme',
    title: 'Meme Project',
    desc: 'Community-first, viral, expressive. Strong identity and memes.',
  },
  {
    value: 'tool',
    title: 'Tool / App',
    desc: 'Utility-driven project solving a specific problem.',
  },
  {
    value: 'defi',
    title: 'DeFi (simple)',
    desc: 'Protocol or financial primitive with clear mechanics.',
  },
] as const

const goals = [
  { value: 'community', label: 'Community & culture' },
  { value: 'utility', label: 'Utility & adoption' },
  { value: 'experiment', label: 'Experiment / concept' },
  { value: 'launch', label: 'Launch-ready product' },
] as const
</script>
