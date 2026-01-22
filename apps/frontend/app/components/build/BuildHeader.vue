<template>
  <header class="build-header">
    <!-- Top line -->
    <div class="build-header-top">
      <div>
        <h1 class="build-title">
          Build
        </h1>
        <p class="build-subtitle">
          {{ currentStep!.subtitle }}
        </p>
      </div>

      <!-- Step indicator (desktop) -->
      <div class="build-header-steps">
        <span>Step {{ store.step }}</span>
        <span>/</span>
        <span>{{ totalSteps }}</span>
      </div>
    </div>

    <!-- Progress bar -->
    <div class="build-progress">
      <div
        class="build-progress-bar"
        :style="{ width: progress + '%' }"
      />
    </div>
  </header>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'

const store = useBuildProtocol()

const steps = [
  { id: 1, subtitle: 'Define the identity and lore' },
  { id: 2, subtitle: 'Choose the project type' },
  { id: 3, subtitle: 'Lock the visual direction' },
  { id: 4, subtitle: 'Select outputs to generate' },
  { id: 5, subtitle: 'Review and launch the build' },
]

const currentStep = computed(
  () => steps.find(s => s.id === store.step) ?? steps[0]
)

const totalSteps = steps.length
const progress = computed(
  () => ((store.step - 1) / (totalSteps - 1)) * 100
)
</script>
