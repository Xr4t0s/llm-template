<template>
  <button
    class="
      w-full
      text-left
      rounded-2xl
      border
      p-4
      transition-all
      space-y-3
    "
    :class="
      selected
        ? 'border-white/30 bg-white/10'
        : 'border-white/10 bg-white/5 hover:bg-white/7'
    "
    @click="$emit('toggle')"
  >
    <!-- Preview -->
    <PalettePreview :colors="palette.chips" />

    <!-- Info -->
    <div class="space-y-1">
      <div class="text-sm font-semibold">
        {{ palette.name }}
      </div>
      <div v-if="palette.subtitle" class="text-xs text-(--text-soft)">
        {{ palette.subtitle }}
      </div>
    </div>

    <!-- Status -->
    <div
      class="text-xs font-medium"
      :class="selected ? 'text-white' : 'text-(--text-soft)'"
    >
      {{ selected ? 'Selected' : 'Select palette' }}
    </div>
  </button>
</template>

<script setup lang="ts">
import PalettePreview from './PalettePreview.vue'

defineProps<{
  palette: {
    id: string
    name: string
    subtitle?: string
    chips: readonly string[]
  }
  selected?: boolean
}>()

defineEmits<{
  (e: 'toggle'): void
}>()
</script>
