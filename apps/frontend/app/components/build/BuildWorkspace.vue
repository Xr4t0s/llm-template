<script setup lang="ts">
import { computed } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'

import BuildSidebar from '~/components/build/BuildSidebar.vue'
import BuildHeader from '~/components/build/BuildHeader.vue'
import BuildFooter from '~/components/build/BuildFooter.vue'

import StepIdentity from '~/components/build/steps/StepIdentity.vue'
import StepProject from '~/components/build/steps/StepProject.vue'
import StepVisual from '~/components/build/steps/StepVisual.vue'
import StepOutputs from '~/components/build/steps/StepOutputs.vue'
import StepReview from '~/components/build/steps/StepReview.vue'
import BuildSuccess from '~/components/build/steps/Success.vue'

interface Props {
  mode: 'create' | 'view'
}

defineProps<Props>()
defineEmits<{
  back: []
}>()

const buildStore = useBuildProtocol()
const step = computed(() => buildStore.step)
</script>

<template>
  <div class="relative w-full min-h-screen pt-4 pb-4">
    <div class="mx-auto w-full max-w-7xl px-4 sm:px-6 lg:px-8">
      <!-- Back button for view mode -->
      <div v-if="mode === 'view'" class="mb-6">
        <button
          @click="$emit('back')"
          class="flex items-center gap-2 text-white/60 hover:text-white/80 transition-colors font-medium text-sm"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
          Back to home
        </button>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-[280px_1fr] gap-6 items-start">
        <!-- Sidebar -->
        <aside v-if="mode === 'create'" class="lg:sticky lg:top-0 lg:h-[calc(100vh-120px)]">
          <BuildSidebar />
        </aside>

        <!-- Main Content -->
        <main class="min-h-[calc(100vh-120px)] flex flex-col">
          <!-- Header (only for create mode) -->
		  <div v-if="mode === 'create'" class="mb-6">
        	<button
          	  @click="$emit('back')"
          	  class="flex items-center gap-2 text-white/60 hover:text-white/80 transition-colors font-medium text-sm"
        	>
          	<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          	</svg>
          	  Back to home
        	</button>
      	  </div>
          <BuildHeader v-if="mode === 'create'" />

          <!-- Step Content -->
          <div class="flex-1 flex flex-col" :class="{ 'pt-6': mode === 'create' }">
            <Transition
              name="fade-slide"
              mode="out-in"
            >
              <!-- Create mode: show steps -->
              <template v-if="mode === 'create'">
                <BuildSuccess
                  v-if="buildStore.buildDone"
                  key="success"
                />
                <StepIdentity
                  v-else-if="step === 1"
                  key="step-1"
                />
                <StepProject
                  v-else-if="step === 2"
                  key="step-2"
                />
                <StepVisual
                  v-else-if="step === 3"
                  key="step-3"
                />
                <StepOutputs
                  v-else-if="step === 4"
                  key="step-4"
                />
                <StepReview
                  v-else-if="step === 5"
                  key="step-5"
                />
              </template>

              <!-- View mode: show builds list (placeholder) -->
              <div
                v-else
                key="view-builds"
                class="w-full max-w-3xl space-y-8"
              >
                <!-- Header -->
                <div class="space-y-3">
                  <h2 class="text-3xl font-bold text-white">
                    Your Builds
                  </h2>
                  <p class="text-white/60">
                    Browse and manage all your generated projects
                  </p>
                </div>

                <!-- Empty state -->
                <div class="text-center py-20 space-y-6">
                  <div class="text-6xl">📦</div>
                  <div class="space-y-2">
                    <p class="text-xl font-semibold text-white">
                      No builds yet
                    </p>
                    <p class="text-white/60">
                      Create your first build to see it here
                    </p>
                  </div>
                  <button
                    @click="$emit('back')"
                    class="inline-block group relative px-8 py-3 rounded-xl font-semibold text-white overflow-hidden"
                  >
                    <!-- Gradient background -->
                    <div class="absolute inset-0 bg-linear-to-r from-indigo-600 to-cyan-500 opacity-100 group-hover:opacity-90 transition-opacity" />
                    <!-- Text -->
                    <span class="relative flex items-center gap-2">
                      Create your first build
                      <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                      </svg>
                    </span>
                  </button>
                </div>
              </div>
            </Transition>
          </div>

          <!-- Footer (only for create mode) -->
          <BuildFooter v-if="mode === 'create'" />
        </main>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Fade + Slide transition for steps */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(12px) scale(0.98);
}

.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-8px) scale(0.98);
}
</style>