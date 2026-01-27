<template>
<div class="relative w-full">
  <!-- ÉCRAN WALLET REQUIS -->
  <!-- ÉCRAN WALLET REQUIS -->
	<div
	v-if="!isConnected"
	class="
		min-h-[calc(100svh-6rem)]
		flex
		items-center
		justify-center
		px-6
	"
	>
	<div
		class="
		glass
		w-full
		max-w-[70vw]
		h-full
		rounded-2xl
		p-12
		grid
		grid-cols-1
		md:grid-cols-2
		gap-16
		items-center
		"
	>
		<!-- Visuel -->
		<div class="flex justify-center items-center h-full">
			<img
				src="/images/wallet_required.webp"
				alt="wallet"
				class="h-auto w-auto scale-125"
			>
		</div>

		<!-- Texte -->
		<div class="flex flex-col space-y-6 items-center">
		<h1 class="text-3xl font-semibold">
			Connect your wallet
		</h1>

		<p class="text-(--text-soft) leading-relaxed max-w-xl">
			To access the build workspace, you need to connect a wallet.
			This allows us to secure your session, associate generated artifacts
			with your identity, and unlock advanced features.
		</p>

		<div class="pt-6">
			<client-only>
			<appkit-button />
			</client-only>
		</div>
		</div>
	</div>
	</div>


  <!-- WORKSPACE NORMAL -->
  <div v-else class="build-shell pt-20 pb-4">
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
				min-h-[calc(100svh-6rem)]
				flex
				flex-col
			"
			>
			<!-- Header -->
			<BuildHeader />

			<!-- Step content (prend toute la hauteur restante) -->
			<div class="build-content flex-1 flex pt-6">
				<Transition name="fade-slide" mode="out-in">
				<BuildSuccess v-if="store.buildDone" key="success" />

				<StepIdentity v-else-if="step === 1" key="step-1" />
				<StepProject v-else-if="step === 2" key="step-2" />
				<StepVisual v-else-if="step === 3" key="step-3" />
				<StepOutputs v-else-if="step === 4" key="step-4" />
				<StepReview v-else-if="step === 5" key="step-5" />
				</Transition>
			</div>

			<!-- Footer -->
			<BuildFooter />
		</main>
      </div>
    </div>
  </div>
</div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useAppKitAccount } from "@reown/appkit/vue"
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
  middleware: ['auth-wallet'],
  hideFooter: true
})

const account = useAppKitAccount()
const isConnected = computed(() => !!account.value?.isConnected)

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
