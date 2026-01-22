<template>
  <section class="build-section">
    <!-- Title -->
    <header class="build-step-header">
      <h2 class="build-title">
        Identity & Lore
      </h2>
      <p class="build-subtitle">
        Define the origin story of your project. This narrative will guide
        the visual direction, tone, and documentation.
      </p>
    </header>

    <!-- Lore block -->
    <div class="build-lore">
      <label class="build-label">
        Project lore
      </label>

      <div class="build-textarea-wrapper">
        <textarea
          v-model="store.lore"
          rows="7"
          class="build-textarea"
          placeholder="Describe the idea, the intention, the universe behind your project..."
        />

        <div class="build-counter">
          {{ store.lore.length }} / 800
        </div>
      </div>

      <div class="build-helper">
        Tip: write it like an origin story, not a pitch deck.
      </div>
    </div>

    <!-- Options -->
    <div class="build-options-grid">
      <!-- Mascot -->
      <ToggleCard
        title="Mascot or main character"
        desc="A character can be reused across logos, memes, stickers, and social visuals."
        v-model="store.hasMascot"
      />

      <!-- Tone -->
      <div class="build-card build-tone">
        <div>
          <div class="build-label">
            Narrative tone
          </div>
          <div class="build-helper">
            Overall attitude of the project.
          </div>
        </div>

        <div class="build-tone-list">
          <button
            v-for="tone in tones"
            :key="tone"
            class="build-tone-pill"
            :class="{ 'build-tone-pill-active': store.tone === tone }"
            @click="store.tone = tone"
          >
            {{ tone }}
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useBuildProtocol } from '~/stores/buildProtocol'
import ToggleCard from '../ui/ToogleCard.vue'

const store = useBuildProtocol()

const tones = [
  'Serious',
  'Playful',
  'Meme',
  'Dark',
  'Experimental',
] as const
</script>
