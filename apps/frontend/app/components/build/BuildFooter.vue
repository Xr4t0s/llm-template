<template>
  <div class="build-footer">
    <!-- Back -->
    <button
      class="build-btn build-btn-secondary"
      :disabled="store.step === 1"
      :class="store.step === 1 ? 'opacity-40 cursor-not-allowed' : ''"
      @click="store.prev()"
    >
      Back
    </button>

    <!-- Hint -->
    <div class="build-footer-hint">
      {{ hint }}
    </div>

    <!-- Primary action -->
    <button
      class="build-btn build-btn-primary"
      :disabled="!store.canGoNext"
      :class="!store.canGoNext ? 'opacity-40 cursor-not-allowed' : ''"
      @click="onPrimary"
    >
      {{ primaryLabel }}
    </button>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'

const store = useBuildProtocol()

const hints = [
  'Write a short but meaningful lore.',
  'Choose the category that fits best.',
  'Limit palettes to keep consistency.',
  'Select only what you need now.',
  'Everything is ready. Launch the build.',
]

const hint = computed(() => hints[store.step - 1])

const primaryLabel = computed(() =>
  store.step === 5 ? 'Launch build' : 'Continue'
)

function onPrimary() {
  if (!store.canGoNext) return
  store.step === 5 ? launch() : store.next()
}

function launch() {
  console.log('BUILD PAYLOAD', { ...store.$state })
}
</script>
