<template>
  <div class="rounded-xl border border-white/10 bg-white/5 p-3">
    <div class="text-xs text-(--text-soft)">{{ label }}</div>
    <div class="mt-1 text-sm font-semibold whitespace-pre-wrap">{{ value }}</div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  label: string
  value: string
}>()
</script>
