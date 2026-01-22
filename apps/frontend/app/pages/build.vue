<template>
  <div class="build-shell pt-20 pb-4">
    <!-- Workspace container -->
    <div class="mx-auto w-full max-w-none px-4 sm:px-6 lg:px-10 xl:px-16">
      <div
        class="
          grid
          grid-cols-1
          lg:grid-cols-[280px_1fr]
          gap-6
          items-start
        "
      >
        <!-- Sidebar -->
        <aside
          class="
            lg:sticky
            lg:top-24
            lg:h-[calc(100svh-6rem)]
          "
        >
          <BuildSidebar />
        </aside>

        <!-- Main workspace -->
        <main
          class="
            build-panel
            space-y-8
            min-h-[calc(100svh-6rem)]
          "
        >
          <!-- Header -->
          <BuildHeader />

          <!-- Step content -->
          <div class="build-content">
            <Transition name="fade-slide" mode="out-in">
              <StepIdentity v-if="step === 1" key="step-1" />
              <StepProject v-else-if="step === 2" key="step-2" />
              <StepVisual v-else-if="step === 3" key="step-3" />
              <StepOutputs v-else-if="step === 4" key="step-4" />
              <StepReview v-else-if="step === 5" key="step-5" />
            </Transition>
          </div>

          <!-- Footer nav -->
          <BuildFooter />
        </main>
      </div>
    </div>
  </div>
</template>

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

const store = useBuildProtocol()
const step = computed(() => store.step)
</script>

<style scoped>
/* Smooth step transition */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.25s ease;
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
