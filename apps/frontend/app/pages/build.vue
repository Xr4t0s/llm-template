<script setup lang="ts">
import { ref, watch } from 'vue'
import { useAuthStore } from '~/stores/auth'
import { useBuildProtocol } from '~/stores/buildProtocol'

import BuildWorkspace from '~/components/build/BuildWorkspace.vue'

definePageMeta({
  hideFooter: true,
})

const authStore = useAuthStore()
const buildStore = useBuildProtocol()

// State
const showWorkspace = ref(false)
const workspaceMode = ref<'create' | 'view'>('create')

// Watch for disconnection
watch(
  () => authStore.isConnected,
  (connected) => {
    if (!connected) {
      buildStore.reset()
      showWorkspace.value = false
      navigateTo('/')
    }
  }
)

// Actions
function startNewBuild() {
  buildStore.reset()
  workspaceMode.value = 'create'
  showWorkspace.value = true
}

function viewMyBuilds() {
  workspaceMode.value = 'view'
  showWorkspace.value = true
}

function backToHome() {
  showWorkspace.value = false
}
</script>

<template>
  <div class="relative w-full min-h-screen bg-gradient-to-br from-slate-950 via-purple-950 to-slate-950">
    <!-- Animated background elements -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <div class="absolute -top-40 -right-40 w-80 h-80 bg-indigo-600/10 rounded-full blur-3xl animate-pulse" />
      <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl animate-pulse delay-1000" />
    </div>

    <!-- Main Transition -->
    <Transition name="main-fade" mode="out-in">
      <!-- Wallet Required State -->
      <div
        v-if="!authStore.isConnected"
        key="wallet"
        class="relative z-10 min-h-screen flex items-center justify-center px-4 sm:px-6"
      >
        <div class="w-full max-w-4xl">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 items-center">
            <!-- Illustration -->
            <div class="flex justify-center items-center order-2 md:order-1">
              <div class="relative">
                <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/20 to-cyan-500/20 rounded-3xl blur-2xl" />
                <div class="relative bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8 flex items-center justify-center">
                  <img src="/images/wallet_required.webp" alt="wallet" class="w-64 h-64 object-cover">
                </div>
              </div>
            </div>

            <!-- Content -->
            <div class="space-y-8 order-1 md:order-2">
              <div class="space-y-4">
                <h1 class="text-4xl sm:text-5xl font-bold text-white leading-tight">
                  Connect your wallet
                </h1>
                <p class="text-lg text-white/60 leading-relaxed">
                  To access the build workspace, you need to connect a wallet.
                  This allows us to secure your session, associate generated artifacts
                  with your identity, and unlock advanced features.
                </p>
              </div>

              <!-- Features list -->
              <div class="space-y-3">
                <div class="flex items-center gap-3">
                  <div class="w-5 h-5 rounded-full bg-gradient-to-r from-indigo-400 to-cyan-400 flex items-center justify-center">
                    <svg class="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <span class="text-white/80">Secure session management</span>
                </div>
                <div class="flex items-center gap-3">
                  <div class="w-5 h-5 rounded-full bg-gradient-to-r from-indigo-400 to-cyan-400 flex items-center justify-center">
                    <svg class="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <span class="text-white/80">Own your generated artifacts</span>
                </div>
                <div class="flex items-center gap-3">
                  <div class="w-5 h-5 rounded-full bg-gradient-to-r from-indigo-400 to-cyan-400 flex items-center justify-center">
                    <svg class="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <span class="text-white/80">Access advanced features</span>
                </div>
              </div>

              <!-- Connect button -->
              <button
                @click="authStore.connect"
                :disabled="authStore.isLoading"
                class="w-full group relative px-8 py-4 rounded-xl font-semibold text-white overflow-hidden disabled:opacity-50 disabled:cursor-not-allowed transition-all"
              >
                <div class="absolute inset-0 bg-gradient-to-r from-indigo-600 to-cyan-500 opacity-100 group-hover:opacity-90 transition-opacity" />
                <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-500" />
                <span class="relative flex items-center justify-center gap-2">
                  <svg v-if="authStore.isLoading" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                  </svg>
                  <span v-if="!authStore.isLoading">
                    Connect Phantom
                    <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                    </svg>
                  </span>
                  <span v-else>Connecting…</span>
                </span>
              </button>

              <div class="text-center text-white/50 text-sm">
                Your wallet address is your identity. We never store keys.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Main Content -->
      <div v-else key="main" class="relative z-10">
        <Transition name="home-workspace" mode="out-in">
          <!-- Workspace -->
          <div v-if="showWorkspace" key="workspace">
            <BuildWorkspace :mode="workspaceMode" @back="backToHome" />
          </div>

          <!-- Welcome Home -->
          <div v-else key="home" class="min-h-screen flex flex-col items-center justify-center px-4 sm:px-6 py-20">
            <div class="w-full max-w-2xl text-center space-y-12">
              <!-- Welcome section -->
              <div class="space-y-6">
                <div class="text-8xl animate-bounce" style="animation-delay: 0s">⚡</div>
                <div class="space-y-4">
                  <h1 class="text-5xl sm:text-6xl font-bold text-white leading-tight opacity-0 animate-fade-in" style="animation-delay: 0.1s">
                    Welcome to <span class="bg-gradient-to-r from-indigo-400 via-cyan-400 to-emerald-400 bg-clip-text text-transparent">Build Studio</span>
                  </h1>
                  <p class="text-lg sm:text-xl text-white/60 leading-relaxed opacity-0 animate-fade-in" style="animation-delay: 0.2s">
                    Create extraordinary Web3 projects with AI assistance. From lore to launch, we handle the details.
                  </p>
                </div>
              </div>

              <!-- Action cards -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <button @click="startNewBuild" class="group relative opacity-0 animate-fade-in" style="animation-delay: 0.3s">
                  <div class="absolute inset-0 bg-gradient-to-br from-indigo-600/20 to-cyan-500/20 rounded-2xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
                  <div class="relative bg-white/5 backdrop-blur-xl border border-white/20 rounded-2xl p-8 space-y-4 group-hover:border-white/30 group-hover:bg-white/10 transition-all duration-300 transform group-hover:scale-105 group-hover:-translate-y-2">
                    <div class="w-16 h-16 rounded-xl bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 flex items-center justify-center text-4xl group-hover:scale-125 group-hover:rotate-12 transition-all duration-300">✨</div>
                    <div class="space-y-2 text-left">
                      <h2 class="text-xl font-bold text-white group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-indigo-400 group-hover:to-cyan-400 group-hover:bg-clip-text transition-all">Create Build</h2>
                      <p class="text-sm text-white/60 group-hover:text-white/80 transition-colors">Start a new project from scratch. Define your vision, identity, and let AI handle the rest.</p>
                    </div>
                    <div class="flex items-center gap-2 text-indigo-400 font-medium text-sm pt-2 group-hover:gap-4 group-hover:text-indigo-300 transition-all duration-300">
                      Start building
                      <svg class="w-5 h-5 group-hover:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                      </svg>
                    </div>
                  </div>
                </button>

                <button @click="viewMyBuilds" class="group relative opacity-0 animate-fade-in" style="animation-delay: 0.4s">
                  <div class="absolute inset-0 bg-gradient-to-br from-emerald-600/20 to-cyan-500/20 rounded-2xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
                  <div class="relative bg-white/5 backdrop-blur-xl border border-white/20 rounded-2xl p-8 space-y-4 group-hover:border-white/30 group-hover:bg-white/10 transition-all duration-300 transform group-hover:scale-105 group-hover:-translate-y-2">
                    <div class="w-16 h-16 rounded-xl bg-gradient-to-br from-emerald-500/20 to-cyan-500/20 flex items-center justify-center text-4xl group-hover:scale-125 group-hover:rotate-12 transition-all duration-300">📦</div>
                    <div class="space-y-2 text-left">
                      <h2 class="text-xl font-bold text-white group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-emerald-400 group-hover:to-cyan-400 group-hover:bg-clip-text transition-all">View Builds</h2>
                      <p class="text-sm text-white/60 group-hover:text-white/80 transition-colors">Browse your previous builds, download assets, and regenerate outputs.</p>
                    </div>
                    <div class="flex items-center gap-2 text-emerald-400 font-medium text-sm pt-2 group-hover:gap-4 group-hover:text-emerald-300 transition-all duration-300">
                      View projects
                      <svg class="w-5 h-5 group-hover:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                      </svg>
                    </div>
                  </div>
                </button>
              </div>

              <!-- Info section -->
              <div class="space-y-6 pt-8 border-t border-white/10 opacity-0 animate-fade-in" style="animation-delay: 0.5s">
                <div class="space-y-4">
                  <h3 class="text-lg font-semibold text-white">What you'll create:</h3>
                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-left">
                    <div class="flex items-start gap-3 p-3 rounded-lg bg-white/5 hover:bg-white/10 hover:border hover:border-white/20 transition-all group cursor-default hover:-translate-y-1">
                      <span class="text-xl group-hover:scale-125 transition-transform duration-300">🎨</span>
                      <div>
                        <p class="font-medium text-white">Visual Assets</p>
                        <p class="text-xs text-white/50">Logos, banners, PFPs, memes</p>
                      </div>
                    </div>
                    <div class="flex items-start gap-3 p-3 rounded-lg bg-white/5 hover:bg-white/10 hover:border hover:border-white/20 transition-all group cursor-default hover:-translate-y-1">
                      <span class="text-xl group-hover:scale-125 transition-transform duration-300">📝</span>
                      <div>
                        <p class="font-medium text-white">Documentation</p>
                        <p class="text-xs text-white/50">Guides, FAQ, roadmaps</p>
                      </div>
                    </div>
                    <div class="flex items-start gap-3 p-3 rounded-lg bg-white/5 hover:bg-white/10 hover:border hover:border-white/20 transition-all group cursor-default hover:-translate-y-1">
                      <span class="text-xl group-hover:scale-125 transition-transform duration-300">🎯</span>
                      <div>
                        <p class="font-medium text-white">Project Identity</p>
                        <p class="text-xs text-white/50">Tone, vision, direction</p>
                      </div>
                    </div>
                    <div class="flex items-start gap-3 p-3 rounded-lg bg-white/5 hover:bg-white/10 hover:border hover:border-white/20 transition-all group cursor-default hover:-translate-y-1">
                      <span class="text-xl group-hover:scale-125 transition-transform duration-300">⚡</span>
                      <div>
                        <p class="font-medium text-white">Launch Ready</p>
                        <p class="text-xs text-white/50">Production-ready outputs</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Footer -->
              <div class="text-center text-white/40 text-sm space-y-2 pt-4 opacity-0 animate-fade-in" style="animation-delay: 0.6s">
                <p>🔐 All your builds are securely associated with your wallet</p>
                <p class="text-xs">Connected as: <span class="font-mono text-white/60">{{ authStore.publicKey?.slice(0, 10) }}...{{ authStore.publicKey?.slice(-8) }}</span></p>
              </div>
            </div>
          </div>
        </Transition>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
/* Main transition */
.main-fade-enter-active,
.main-fade-leave-active {
  transition: opacity 0.4s ease;
}

.main-fade-enter-from,
.main-fade-leave-to {
  opacity: 0;
}

/* Home <-> Workspace transition */
.home-workspace-enter-active {
  transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.home-workspace-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.home-workspace-enter-from {
  opacity: 0;
  transform: scale(0.95) translateY(30px);
}

.home-workspace-leave-to {
  opacity: 0;
  transform: scale(0.90) translateY(-30px);
}

/* Fade in animation */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fadeInUp 0.6s ease-out forwards;
}

/* Smooth bounce */
@keyframes smoothBounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.animate-bounce {
  animation: smoothBounce 1s ease-in-out infinite;
}
</style>