<template>
  <div class="flex flex-wrap gap-2">
    <button
      v-for="opt in options"
      :key="opt"
      class="text-xs px-2 py-1 rounded-full transition-all"
      :class="modelValue === opt ? 'bg-white/15 text-white' : 'bg-white/5 hover:bg-white/10 text-(--text-soft)'"
      @click="$emit('update:modelValue', opt)"
    >
      {{ opt }}
    </button>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  options: string[]
  modelValue: string
}>()

defineEmits<{
  (e: 'update:modelValue', v: string): void
}>()
</script>
