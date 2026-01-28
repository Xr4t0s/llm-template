<script setup lang="ts">
import { computed, watch } from 'vue'
import { useAuthStore } from '~/stores/auth'
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

definePageMeta({
  hideFooter: true
})

const authStore = useAuthStore()
const buildStore = useBuildProtocol()
const step = computed(() => buildStore.step)

watch(() => authStore.isConnected, (connected) => {
  if (!connected) {
    buildStore.reset()
    navigateTo('/')
  }
})
</script>

<template>
  <div class="relative w-full">
    <Transition name="fade" mode="out-in">
      <div
        v-if="!authStore.isConnected"
        key="wallet-required"
        class="min-h-[calc(100svh-6rem)] flex items-center justify-center px-6"
      >
        <div class="glass w-full max-w-[70vw] h-full rounded-2xl p-12 grid grid-cols-1 md:grid-cols-2 gap-16 items-center">
          <div class="flex justify-center items-center h-full">
            <img src="/images/wallet_required.webp" alt="wallet" class="h-auto w-auto scale-125">
          </div>

          <div class="flex flex-col space-y-6 items-center">
            <h1 class="text-3xl font-semibold">Connect your wallet</h1>
            <p class="text-(--text-soft) leading-relaxed max-w-xl">
              To access the build workspace, you need to connect a wallet.
              This allows us to secure your session, associate generated artifacts
              with your identity, and unlock advanced features.
            </p>
            <div class="pt-6">
              <button 
                @click="authStore.connect"
                :disabled="authStore.isLoading"
                class="bg-blue-500 hover:bg-blue-600 px-6 py-3 rounded-lg font-semibold disabled:opacity-50 transition-colors"
              >
                {{ authStore.isLoading ? 'Connecting...' : 'Connect Phantom' }}
              </button>
            </div>
          </div>
        </div>
      </div>

      <div v-else key="workspace" class="build-shell pt-20 pb-4">
        <div class="mx-auto w-full max-w-none px-4 sm:px-6 lg:px-10 xl:px-16">
          <div class="grid grid-cols-1 lg:grid-cols-[280px_1fr] gap-6 items-start">
            <aside class="lg:sticky lg:top-24 lg:h-[calc(100svh-6rem)]">
              <BuildSidebar />
            </aside>

            <main class="build-panel min-h-[calc(100svh-6rem)] flex flex-col">
              <BuildHeader />

              <div class="build-content flex-1 flex pt-6">
                <Transition name="fade-slide" mode="out-in">
                  <BuildSuccess v-if="buildStore.buildDone" key="success" />
                  <StepIdentity v-else-if="step === 1" key="step-1" />
                  <StepProject v-else-if="step === 2" key="step-2" />
                  <StepVisual v-else-if="step === 3" key="step-3" />
                  <StepOutputs v-else-if="step === 4" key="step-4" />
                  <StepReview v-else-if="step === 5" key="step-5" />
                </Transition>
              </div>

              <BuildFooter />
            </main>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

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