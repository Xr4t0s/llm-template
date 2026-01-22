<template>
  <div class="rounded-xl border border-white/10 bg-white/5 p-4">
    <div class="flex items-start justify-between gap-4">
      <div>
        <div class="text-sm font-semibold">{{ title }}</div>
        <div v-if="desc" class="mt-1 text-xs text-(--text-soft)">{{ desc }}</div>
      </div>

      <button
        class="px-3 py-2 rounded-lg bg-white/10 hover:bg-white/15 transition-all text-xs font-semibold"
        @click="$emit('update:modelValue', !modelValue)"
      >
        {{ modelValue ? 'YES' : 'NO' }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  title: string
  desc?: string
  modelValue: boolean
}>()

defineEmits<{
  (e: 'update:modelValue', v: boolean): void
}>()
</script>
