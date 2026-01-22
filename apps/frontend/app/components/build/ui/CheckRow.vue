<template>
  <button
    type="button"
    class="w-full flex items-start gap-3 rounded-lg p-3 border border-white/10 bg-white/5 hover:bg-white/7 transition-all text-left"
    @click="$emit('update:modelValue', !modelValue)"
  >
    <div class="mt-0.5 h-4 w-4 rounded border border-white/20 flex items-center justify-center">
      <div v-if="modelValue" class="h-2.5 w-2.5 rounded bg-white/70"></div>
    </div>

    <div class="flex-1">
      <div class="text-sm font-medium">{{ label }}</div>
      <div v-if="desc" class="mt-1 text-xs text-(--text-soft)">{{ desc }}</div>
    </div>
  </button>
</template>

<script setup lang="ts">
defineProps<{
  label: string
  desc?: string
  modelValue: boolean
}>()

defineEmits<{
  (e: 'update:modelValue', v: boolean): void
}>()
</script>
