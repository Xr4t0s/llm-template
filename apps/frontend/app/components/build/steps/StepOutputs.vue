<template>
  <div class="space-y-8 w-full max-w-3xl">
    <!-- Header -->
    <div class="space-y-3">
      <h2 class="text-3xl font-bold text-white">
        Outputs
      </h2>
      <p class="text-white/60 leading-relaxed">
        Select what you want to generate now. You can always add more later.
        Focus on what's needed for the next step of your project.
      </p>
    </div>

    <!-- Visual assets section -->
    <div class="space-y-4">
      <div>
        <h3 class="text-sm font-semibold text-white mb-1">
          📐 Visual assets
        </h3>
        <p class="text-xs text-white/50">
          Identity and communication visuals
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <CheckboxCard
          label="Logos"
          desc="3–5 variants, light & dark, SVG / PNG"
          v-model="store.outputs.logo"
        />
        <CheckboxCard
          label="Profile pictures (PFP)"
          desc="Square avatars aligned with the DA"
          v-model="store.outputs.pfp"
        />
        <CheckboxCard
          label="Banners"
          desc="Twitter / X headers with tagline"
          v-model="store.outputs.banner"
        />
        <CheckboxCard
          label="Announcement cards"
          desc="Launch, milestones, partnerships"
          v-model="store.outputs.announcements"
        />
        <CheckboxCard
          label="Memes"
          desc="Templates for viral content"
          v-model="store.outputs.memes"
        />
        <CheckboxCard
          label="Stickers"
          desc="Telegram sticker pack"
          v-model="store.outputs.stickers"
        />
      </div>
    </div>

    <!-- Content & documentation section -->
    <div class="space-y-4">
      <div>
        <h3 class="text-sm font-semibold text-white mb-1">
          📝 Content & documentation
        </h3>
        <p class="text-xs text-white/50">
          Textual assets and structured explanations
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <CheckboxCard
          label="Documentation"
          desc="Structured, GitBook-ready docs"
          v-model="store.outputs.documentation"
        />
        <CheckboxCard
          label="One-pager"
          desc="Short overview of the project"
          v-model="store.outputs.onepager"
        />
        <CheckboxCard
          label="Roadmap"
          desc="Phases, milestones, future plans"
          v-model="store.outputs.roadmap"
        />
        <CheckboxCard
          label="FAQ"
          desc="Common questions and disclaimers"
          v-model="store.outputs.faq"
        />
      </div>
    </div>

    <!-- Summary card -->
    <div class="bg-gradient-to-r from-cyan-500/10 to-indigo-500/10 backdrop-blur-xl border border-cyan-500/20 rounded-xl p-5 space-y-3">
      <div class="flex items-center gap-2 text-white">
        <svg class="w-5 h-5 text-cyan-400" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2z" clip-rule="evenodd" />
        </svg>
        <span class="font-semibold text-sm">
          {{ selectedCount }} output{{ selectedCount !== 1 ? 's' : '' }} selected
        </span>
      </div>
      <p class="text-xs text-white/60">
        This selection will define the scope of your build. More outputs = more time to generate.
      </p>
    </div>

    <!-- Validation hint -->
    <div v-if="selectedCount === 0" class="flex items-center gap-3 px-4 py-3 rounded-lg bg-orange-500/10 border border-orange-500/20">
      <svg class="w-5 h-5 text-orange-400 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
      <p class="text-sm text-orange-300">
        Select at least one output to continue
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'
import CheckboxCard from '../ui/CheckRow.vue'

const store = useBuildProtocol()

const selectedCount = computed(() =>
  Object.values(store.outputs).filter(Boolean).length
)
</script>