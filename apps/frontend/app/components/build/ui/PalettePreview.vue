<template>
  <div
    class="
      relative
      h-24
      w-full
      rounded-xl
      overflow-hidden
      border
      border-white/10
    "
  >
    <!-- Background -->
    <div
      class="absolute inset-0"
      :style="{ background: gradient }"
    />

    <!-- Fake UI blocks -->
    <div class="relative z-10 h-full p-3 flex flex-col justify-between">
      <!-- Header -->
      <div class="flex items-center gap-2">
        <div
          class="h-3 w-3 rounded-full"
          :style="{ background: colors[0] }"
        />
        <div class="h-2 w-16 rounded bg-white/40"></div>
      </div>

      <!-- Content -->
      <div class="space-y-1">
        <div class="h-2 w-3/4 rounded bg-white/30"></div>
        <div class="h-2 w-1/2 rounded bg-white/20"></div>
      </div>

      <!-- Accent -->
      <div class="h-2 w-10 rounded-full"
           :style="{ background: colors[1] }" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  colors: readonly string[]
}>()

const gradient = computed(() => {
  if (props.colors.length < 2) return props.colors[0]
  return `linear-gradient(135deg, ${props.colors.join(', ')})`
})
</script>
