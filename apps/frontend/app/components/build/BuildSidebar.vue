<template>
  <aside class="build-sidebar">
    <!-- Steps -->
    <nav class="build-sidebar-steps">
      <button
        v-for="s in steps"
        :key="s.id"
        class="build-sidebar-step"
        :class="stepClass(s.id)"
        @click="goTo(s.id)"
      >
        <span class="build-sidebar-step-index">
          {{ s.id }}
        </span>

        <span class="build-sidebar-step-label">
          {{ s.title }}
        </span>
      </button>
    </nav>
  </aside>
</template>

<script setup lang="ts">
import { useBuildProtocol } from '~/stores/buildProtocol'

const store = useBuildProtocol()

const steps = [
  { id: 1, title: 'Identity' },
  { id: 2, title: 'Project' },
  { id: 3, title: 'Visual' },
  { id: 4, title: 'Outputs' },
  { id: 5, title: 'Review' },
]

function goTo(id: number) {
  if (id <= store.step) store.goTo(id)
}

function stepClass(id: number) {
  if (id === store.step) return 'is-active'
  if (id < store.step) return 'is-done'
  return 'is-locked'
}
</script>
