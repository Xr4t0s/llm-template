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
  <div class="relative w-full min-h-screen bg-black overflow-hidden">
    <!-- Animated background -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <!-- Animated gradient orbs -->
      <div class="absolute top-1/4 -right-40 w-96 h-96 bg-indigo-600/25 rounded-full blur-3xl animate-float" />
      <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-cyan-500/20 rounded-full blur-3xl animate-float-delayed" />
      <div class="absolute top-1/2 left-1/3 w-72 h-72 bg-emerald-500/15 rounded-full blur-3xl animate-pulse" style="animation-duration: 8s;" />
      
      <!-- Grid background -->
      <svg class="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <pattern id="grid-build" width="50" height="50" patternUnits="userSpaceOnUse">
            <path d="M 50 0 L 0 0 0 50" fill="none" stroke="rgba(139, 92, 246, 0.1)" stroke-width="1"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid-build)" />
      </svg>
    </div>

    <!-- Main Transition -->
    <Transition name="main-fade" mode="out-in">
      <!-- Wallet Required State -->
      <div
        v-if="!authStore.isConnected && false"
        key="wallet"
        class="relative z-10 min-h-screen flex items-center justify-center p-4 sm:px-6"
      >
        <div class="w-full max-w-5xl">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-16 items-center">

            <!-- Left: Visual -->
            <div class="relative h-96 hidden lg:block order-2 lg:order-1">
              <div class="absolute inset-0 bg-linear-to-br from-indigo-600/40 via-cyan-600/30 to-emerald-600/20 rounded-4xl blur-3xl" />
              <div class="absolute inset-6 border border-white/10 rounded-3xl backdrop-blur-md bg-white/5 flex flex-col items-center justify-center overflow-hidden p-8 space-y-6">
                <div class="text-8xl animate-bounce">🔐</div>
                <div class="text-center space-y-2">
                  <p class="text-white font-bold text-xl">Secure Entry</p>
                  <p class="text-white/60 text-sm">Connect with your wallet to begin</p>
                </div>
              </div>
            </div>

            <!-- Right: Content -->
            <div class="space-y-10 order-1 lg:order-2">
              <div class="space-y-6">
                <div class="inline-block">
                  <span class="text-sm font-mono text-transparent bg-clip-text bg-linear-to-r from-indigo-400 to-cyan-400 tracking-widest uppercase">
                    🔑 Wallet Connection
                  </span>
                </div>
                <h1 class="text-5xl sm:text-6xl lg:text-7xl font-thin leading-tight text-white">
                  Connect your
                  <br />
                  <span class="bg-linear-to-r from-indigo-400 via-cyan-400 to-emerald-400 bg-clip-text text-transparent">
                    wallet
                  </span>
                </h1>
                <p class="text-xl text-white/70 leading-relaxed font-light max-w-lg">
                  Secure your session and own your generated artifacts. Your wallet address is your identity.
                </p>
              </div>

              <!-- Features list -->
              <div class="space-y-4">
                <div class="flex items-start gap-4 p-4 rounded-xl hover:bg-white/5 transition-all group">
                  <div class="w-6 h-6 rounded-full bg-linear-to-r from-indigo-400 to-cyan-400 flex items-center justify-center shrink-0 mt-0.5 group-hover:scale-110 transition-transform">
                    <svg class="w-3.5 h-3.5 text-black" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <div class="space-y-1 flex-1">
                    <p class="font-semibold text-white group-hover:text-indigo-200 transition-colors">Secure Session Management</p>
                    <p class="text-sm text-white/50">Your session is protected and associated with your wallet</p>
                  </div>
                </div>

                <div class="flex items-start gap-4 p-4 rounded-xl hover:bg-white/5 transition-all group">
                  <div class="w-6 h-6 rounded-full bg-linear-to-r from-cyan-400 to-emerald-400 flex items-center justify-center shrink-0 mt-0.5 group-hover:scale-110 transition-transform">
                    <svg class="w-3.5 h-3.5 text-black" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <div class="space-y-1 flex-1">
                    <p class="font-semibold text-white group-hover:text-cyan-200 transition-colors">Own Your Artifacts</p>
                    <p class="text-sm text-white/50">All generated assets are securely associated with your identity</p>
                  </div>
                </div>

                <div class="flex items-start gap-4 p-4 rounded-xl hover:bg-white/5 transition-all group">
                  <div class="w-6 h-6 rounded-full bg-linear-to-r from-emerald-400 to-indigo-400 flex items-center justify-center shrink-0 mt-0.5 group-hover:scale-110 transition-transform">
                    <svg class="w-3.5 h-3.5 text-black" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                    </svg>
                  </div>
                  <div class="space-y-1 flex-1">
                    <p class="font-semibold text-white group-hover:text-emerald-200 transition-colors">Access Premium Features</p>
                    <p class="text-sm text-white/50">Unlock advanced building capabilities and storage options</p>
                  </div>
                </div>
              </div>

              <!-- Connect button -->
              <button
                @click="authStore.connect"
                :disabled="authStore.isLoading"
                class="w-full group relative px-8 py-5 rounded-xl font-bold text-white text-lg overflow-hidden disabled:opacity-50 disabled:cursor-not-allowed transition-all"
              >
                <!-- Gradient background -->
                <div class="absolute inset-0 bg-linear-to-r from-indigo-600 via-indigo-500 to-cyan-500 opacity-100 group-hover:opacity-90 transition-opacity duration-300" />
                <!-- Shimmer -->
                <div class="absolute inset-0 bg-linear-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-700" />
                <!-- Text -->
                <span class="relative flex items-center justify-center gap-3">
                  <svg v-if="authStore.isLoading" class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                  </svg>
                  <span v-if="!authStore.isLoading">
                    Connect Phantom Wallet
                  </span>
                  <span v-else>Connecting…</span>
                </span>
              </button>

              <div class="text-center text-white/50 text-sm">
                🛡️ We never store your private keys or secret phrases
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
            <div class="w-full max-w-4xl text-center space-y-16">
              <!-- Welcome section -->
              <div class="space-y-8">
                <div class="text-9xl animate-bounce" style="animation-delay: 0s">✨</div>
                <div class="space-y-6">
                  <h1 class="text-6xl sm:text-7xl lg:text-8xl font-thin leading-tight text-white opacity-0 animate-fade-in" style="animation-delay: 0.1s">
                    Welcome to
                    <br />
                    <span class="bg-linear-to-r from-indigo-400 via-cyan-400 to-emerald-400 bg-clip-text text-transparent animate-gradient">
                      Build Studio
                    </span>
                  </h1>
                  <p class="text-xl sm:text-2xl text-white/60 leading-relaxed font-light opacity-0 animate-fade-in" style="animation-delay: 0.2s">
                    Orchestrate AI to create extraordinary Web3 projects. From vision to launch, handled end-to-end.
                  </p>
                </div>
              </div>

              <!-- Action cards -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 sm:gap-8">
                <!-- Create Build Card -->
                <button @click="startNewBuild" class="group relative opacity-0 animate-fade-in h-full" style="animation-delay: 0.3s">
                  <!-- Glow effect -->
                  <div class="absolute -inset-2 bg-linear-to-br from-indigo-600/30 to-cyan-500/20 rounded-3xl blur-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
                  
                  <!-- Card -->
                  <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-10 sm:p-12 space-y-6 group-hover:border-indigo-400/40 transition-all duration-300 transform group-hover:scale-105 group-hover:-translate-y-3 h-full flex flex-col">
                    <!-- Icon -->
                    <div class="w-20 h-20 rounded-2xl bg-linear-to-br from-indigo-500/30 to-cyan-500/20 flex items-center justify-center text-5xl group-hover:scale-125 group-hover:rotate-12 transition-all duration-300 border border-indigo-400/30">
                      ✨
                    </div>
                    
                    <!-- Content -->
                    <div class="space-y-3 flex-1 text-left">
                      <h2 class="text-3xl font-thin text-white group-hover:text-transparent group-hover:bg-linear-to-r group-hover:from-indigo-400 group-hover:to-cyan-400 group-hover:bg-clip-text transition-all duration-300">
                        Create Build
                      </h2>
                      <p class="text-base text-white/60 group-hover:text-white/80 transition-colors leading-relaxed">
                        Start a new project from scratch. Define your vision, set the tone, and let AI orchestration handle the execution.
                      </p>
                    </div>
                    
                    <!-- CTA -->
                    <div class="flex items-center gap-3 text-indigo-300 font-bold text-base pt-4 group-hover:gap-6 group-hover:text-indigo-200 transition-all duration-300">
                      Start building
                      <svg class="w-6 h-6 group-hover:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                      </svg>
                    </div>
                  </div>
                </button>

                <!-- View Builds Card -->
                <button @click="viewMyBuilds" class="group relative opacity-0 animate-fade-in h-full" style="animation-delay: 0.4s">
                  <!-- Glow effect -->
                  <div class="absolute -inset-2 bg-linear-to-br from-emerald-600/30 to-cyan-500/20 rounded-3xl blur-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
                  
                  <!-- Card -->
                  <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-10 sm:p-12 space-y-6 group-hover:border-emerald-400/40 transition-all duration-300 transform group-hover:scale-105 group-hover:-translate-y-3 h-full flex flex-col">
                    <!-- Icon -->
                    <div class="w-20 h-20 rounded-2xl bg-linear-to-br from-emerald-500/30 to-cyan-500/20 flex items-center justify-center text-5xl group-hover:scale-125 group-hover:rotate-12 transition-all duration-300 border border-emerald-400/30">
                      📦
                    </div>
                    
                    <!-- Content -->
                    <div class="space-y-3 flex-1 text-left">
                      <h2 class="text-3xl font-thin text-white group-hover:text-transparent group-hover:bg-linear-to-r group-hover:from-emerald-400 group-hover:to-cyan-400 group-hover:bg-clip-text transition-all duration-300">
                        View Builds
                      </h2>
                      <p class="text-base text-white/60 group-hover:text-white/80 transition-colors leading-relaxed">
                        Browse your previous projects, download assets, regenerate outputs, and track your creation history.
                      </p>
                    </div>
                    
                    <!-- CTA -->
                    <div class="flex items-center gap-3 text-emerald-300 font-bold text-base pt-4 group-hover:gap-6 group-hover:text-emerald-200 transition-all duration-300">
                      View projects
                      <svg class="w-6 h-6 group-hover:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                      </svg>
                    </div>
                  </div>
                </button>
              </div>

              <!-- Info section -->
              <div class="space-y-8 pt-12 border-t border-white/10 opacity-0 animate-fade-in" style="animation-delay: 0.5s">
                <div class="space-y-6">
                  <h3 class="text-2xl font-bold text-white">What you'll create:</h3>
                  <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
                    <!-- Visual Assets -->
                    <div class="flex flex-col items-center gap-3 p-6 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/0 hover:border-white/20 transition-all group cursor-default hover:-translate-y-2">
                      <span class="text-4xl group-hover:scale-125 transition-transform duration-300">🎨</span>
                      <div class="text-center space-y-1">
                        <p class="font-bold text-white text-sm">Visual Assets</p>
                        <p class="text-xs text-white/50">Logos, banners, PFPs</p>
                      </div>
                    </div>

                    <!-- Documentation -->
                    <div class="flex flex-col items-center gap-3 p-6 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/0 hover:border-white/20 transition-all group cursor-default hover:-translate-y-2">
                      <span class="text-4xl group-hover:scale-125 transition-transform duration-300">📝</span>
                      <div class="text-center space-y-1">
                        <p class="font-bold text-white text-sm">Documentation</p>
                        <p class="text-xs text-white/50">Guides, FAQ, roadmaps</p>
                      </div>
                    </div>

                    <!-- Project Identity -->
                    <div class="flex flex-col items-center gap-3 p-6 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/0 hover:border-white/20 transition-all group cursor-default hover:-translate-y-2">
                      <span class="text-4xl group-hover:scale-125 transition-transform duration-300">🎯</span>
                      <div class="text-center space-y-1">
                        <p class="font-bold text-white text-sm">Project Identity</p>
                        <p class="text-xs text-white/50">Tone, vision, direction</p>
                      </div>
                    </div>

                    <!-- Launch Ready -->
                    <div class="flex flex-col items-center gap-3 p-6 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/0 hover:border-white/20 transition-all group cursor-default hover:-translate-y-2">
                      <span class="text-4xl group-hover:scale-125 transition-transform duration-300">⚡</span>
                      <div class="text-center space-y-1">
                        <p class="font-bold text-white text-sm">Launch Ready</p>
                        <p class="text-xs text-white/50">Production-ready outputs</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Footer -->
              <div class="text-center text-white/50 text-sm space-y-3 pt-8 opacity-0 animate-fade-in" style="animation-delay: 0.6s">
                <div class="flex items-center justify-center gap-2">
                  <span>🔐</span>
                  <p>All builds securely owned by your wallet</p>
                </div>
                <div class="font-mono text-white/40 text-xs">
                  Connected: <span class="text-white/60">{{ authStore.publicKey?.slice(0, 12) }}...{{ authStore.publicKey?.slice(-10) }}</span>
                </div>
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
  transition: all 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
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

/* Custom animations */
@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-30px);
  }
}

@keyframes float-delayed {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(30px);
  }
}

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

@keyframes gradient {
  0%, 100% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
}

@keyframes smoothBounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-15px); }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}

.animate-float-delayed {
  animation: float-delayed 8s ease-in-out infinite;
}

.animate-fade-in {
  animation: fadeInUp 0.8s ease-out forwards;
  opacity: 0;
}

.animate-bounce {
  animation: smoothBounce 1.2s ease-in-out infinite;
}

.animate-gradient {
  background-size: 200% 200%;
  animation: gradient 3s ease infinite;
}
</style>