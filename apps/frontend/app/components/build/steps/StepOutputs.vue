<template>
  <section class="space-y-10">
    <!-- Header -->
    <header class="space-y-2">
      <h2 class="text-2xl font-semibold tracking-tight">
        Outputs
      </h2>
      <p class="text-sm text-(--text-soft) max-w-xl">
        Select what you want to generate now. You can always add more later.
        Focus on what’s needed for the next step of your project.
      </p>
    </header>

    <!-- Visual outputs -->
    <div class="space-y-4">
      <div>
        <div class="text-sm font-semibold">
          Visual assets
        </div>
        <div class="text-xs text-(--text-soft)">
          Identity and communication visuals.
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <CheckRow
          label="Logos"
          desc="3–5 variants, light & dark, SVG / PNG"
          v-model="store.outputs.logo"
        />
        <CheckRow
          label="Profile pictures (PFP)"
          desc="Square avatars aligned with the DA"
          v-model="store.outputs.pfp"
        />
        <CheckRow
          label="Banners"
          desc="Twitter / X headers with tagline"
          v-model="store.outputs.banner"
        />
        <CheckRow
          label="Announcement cards"
          desc="Launch, milestones, partnerships"
          v-model="store.outputs.announcements"
        />
        <CheckRow
          label="Memes"
          desc="Templates for viral content"
          v-model="store.outputs.memes"
        />
        <CheckRow
          label="Stickers"
          desc="Telegram sticker pack"
          v-model="store.outputs.stickers"
        />
      </div>
    </div>

    <!-- Content outputs -->
    <div class="space-y-4">
      <div>
        <div class="text-sm font-semibold">
          Content & documentation
        </div>
        <div class="text-xs text-(--text-soft)">
          Textual assets and structured explanations.
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
        <CheckRow
          label="Documentation"
          desc="Structured, GitBook-ready documentation"
          v-model="store.outputs.documentation"
        />
        <CheckRow
          label="One-pager"
          desc="Short overview of the project"
          v-model="store.outputs.onepager"
        />
        <CheckRow
          label="Roadmap"
          desc="Phases, milestones, future plans"
          v-model="store.outputs.roadmap"
        />
        <CheckRow
          label="FAQ"
          desc="Common questions and disclaimers"
          v-model="store.outputs.faq"
        />
      </div>
    </div>

    <!-- Summary -->
    <div
      class="
        rounded-2xl
        border
        border-white/10
        bg-white/5
        p-4
        text-xs
        text-(--text-soft)
      "
    >
      {{ selectedCount }} output{{ selectedCount > 1 ? 's' : '' }} selected.
      This will define the scope of the build.
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'
import CheckRow from '../ui/CheckRow.vue'

const store = useBuildProtocol()

const selectedCount = computed(() =>
  Object.values(store.outputs).filter(Boolean).length
)
</script>
