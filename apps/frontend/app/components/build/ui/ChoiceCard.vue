<template>
  <button
    class="w-full text-left rounded-xl border transition-all"
    :class="active ? 'border-white/30 bg-white/10' : 'border-white/10 bg-white/5 hover:bg-white/7'"
    @click="$emit('click')"
  >
    <div class="p-4">
      <div class="text-sm font-semibold">{{ title }}</div>
      <div v-if="desc" class="mt-1 text-xs text-(--text-soft)">{{ desc }}</div>
    </div>
  </button>
</template>

<script setup lang="ts">
defineProps<{
  title: string
  desc?: string
  active?: boolean
}>()

defineEmits<{
  (e: 'click'): void
}>()
</script>
