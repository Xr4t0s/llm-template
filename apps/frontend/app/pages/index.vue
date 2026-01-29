<template>
  <div class="relative overflow-hidden bg-black">
    <!-- ============================================
         HERO SECTION
        ============================================ -->
    <section class="relative min-h-[calc(100vh-80px)] flex items-center justify-center pt-20 pb-20 overflow-hidden">
      <!-- Animated background elements -->
      <div class="absolute inset-0 overflow-hidden">
        <!-- Animated gradient orbs -->
        <div class="absolute top-1/4 -right-40 w-96 h-96 bg-indigo-600/30 rounded-full blur-3xl animate-float" />
        <div class="absolute -bottom-32 -left-40 w-96 h-96 bg-cyan-500/25 rounded-full blur-3xl animate-float-delayed" />
        <div class="absolute top-1/2 left-1/2 w-72 h-72 bg-emerald-500/20 rounded-full blur-3xl animate-pulse" style="animation-duration: 8s;" />
        
        <!-- Grid background -->
        <svg class="absolute inset-0 w-full h-full opacity-20" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <pattern id="grid-hero" width="50" height="50" patternUnits="userSpaceOnUse">
              <path d="M 50 0 L 0 0 0 50" fill="none" stroke="rgba(139, 92, 246, 0.1)" stroke-width="1"/>
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#grid-hero)" />
        </svg>
      </div>

      <!-- Content -->
      <div class="max-w-6xl mx-auto px-6 w-full relative z-10">
        <div class="max-w-4xl space-y-10 mx-auto lg:mx-0 lg:max-w-3xl">

          <!-- Accent label -->
          <div class="inline-block animate-fade-in" style="animation-delay: 0s;">
            <span class="text-sm font-mono text-transparent bg-clip-text bg-linear-to-r from-indigo-400 to-cyan-400 tracking-widest uppercase">
              ✨ The future of building
            </span>
          </div>

          <!-- Main Heading -->
          <div class="space-y-6 animate-fade-in" style="animation-delay: 0.1s;">
            <h1 class="text-6xl sm:text-7xl lg:text-8xl font-black leading-tight text-white">
              Build products
              <br />
              <span class="bg-linear-to-r from-indigo-400 via-cyan-400 to-emerald-400 bg-clip-text text-transparent animate-gradient">
                with intention
              </span>
            </h1>
          </div>

          <!-- Subheading -->
          <p class="text-lg sm:text-xl text-white/70 max-w-2xl leading-relaxed animate-fade-in font-light" style="animation-delay: 0.2s;">
            A Web3-native workspace to orchestrate LLMs using custom MCP services. Manage state, maintain context, and ship real artifacts—
            <span class="text-white font-semibold bg-linear-to-r from-indigo-200 to-cyan-200 bg-clip-text text-transparent">from idea to production.</span>
          </p>

          <!-- CTA Buttons -->
          <div class="flex flex-col sm:flex-row items-start gap-4 pt-4 animate-fade-in" style="animation-delay: 0.3s;">
            <NuxtLink
              to="/build"
              class="group relative px-8 py-4 rounded-xl font-bold text-white overflow-hidden w-full sm:w-auto text-center sm:text-left"
            >
              <!-- Gradient background -->
              <div class="absolute inset-0 bg-linear-to-r from-indigo-600 via-indigo-500 to-cyan-500 opacity-100 group-hover:opacity-90 transition-opacity duration-300" />
              <!-- Animated border -->
              <div class="absolute inset-0 rounded-xl opacity-0 group-hover:opacity-100 border border-white/20 transition-opacity duration-300" />
              <!-- Shimmer effect -->
              <div class="absolute inset-0 bg-linear-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-700" />
              <!-- Text -->
              <span class="relative flex items-center gap-3 justify-center sm:justify-start">
                Start building
                <svg class="w-5 h-5 group-hover:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </span>
            </NuxtLink>

            <NuxtLink
              to="/docs"
              class="group relative px-8 py-4 rounded-xl font-bold text-white border-2 border-white/30 hover:border-white/60 transition-all duration-300 backdrop-blur-sm w-full sm:w-auto text-center sm:text-left hover:bg-white/5"
            >
              <span class="relative flex items-center gap-3 justify-center sm:justify-start">
                Read the docs
                <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7" />
                </svg>
              </span>
            </NuxtLink>
          </div>

          <!-- Stats row -->
          <div class="flex flex-wrap gap-8 pt-8 animate-fade-in border-t border-white/10 pt-8" style="animation-delay: 0.4s;">
            <div class="space-y-2">
              <div class="text-3xl font-bold text-transparent bg-clip-text bg-linear-to-r from-indigo-400 to-cyan-400">
                3<span class="text-sm text-white/40">+</span>
              </div>
              <p class="text-sm text-white/60 font-light">LLM Orchestration</p>
            </div>
            <div class="space-y-2">
              <div class="text-3xl font-bold text-transparent bg-clip-text bg-linear-to-r from-cyan-400 to-emerald-400">
                ∞
              </div>
              <p class="text-sm text-white/60 font-light">Stateful Context</p>
            </div>
            <div class="space-y-2">
              <div class="text-3xl font-bold text-transparent bg-clip-text bg-linear-to-r from-emerald-400 to-indigo-400">
                1<span class="text-sm text-white/40">-click</span>
              </div>
              <p class="text-sm text-white/60 font-light">Production Deploy</p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ============================================
         MANIFESTO SECTION
        ============================================ -->
    <section class="relative py-24 sm:py-40 border-t border-white/10">
      <div class="max-w-6xl mx-auto px-6">
        <div class="grid lg:grid-cols-2 gap-16 items-center">
          
          <!-- Left: Text -->
          <div class="space-y-6 max-w-2xl">
            <h2 class="text-5xl sm:text-6xl font-black leading-tight">
              How do we prevent you
              <br />
              <span class="bg-linear-to-r from-indigo-400 via-cyan-400 to-emerald-400 bg-clip-text text-transparent">
                from prompting.
              </span>
            </h2>

            <p class="text-xl text-white/70 leading-relaxed font-light">
              Most AI tools are optimized for <span class="text-white">conversation</span>. LLM Studio is optimized for <span class="text-white font-bold">construction.</span>
            </p>

            <p class="text-lg text-white/60 leading-relaxed">
              Persistent context, explicit intent, structured flows—everything you need to ship real products instead of fine-tuning prompts.
            </p>

            <div class="pt-4 space-y-3">
              <div class="flex items-start gap-3 text-white/70">
                <span class="text-indigo-400 text-xl mt-1">▸</span>
                <span>Projects, not conversations</span>
              </div>
              <div class="flex items-start gap-3 text-white/70">
                <span class="text-cyan-400 text-xl mt-1">▸</span>
                <span>State management, not chat history</span>
              </div>
              <div class="flex items-start gap-3 text-white/70">
                <span class="text-emerald-400 text-xl mt-1">▸</span>
                <span>Artifacts, not screenshots</span>
              </div>
            </div>
          </div>

          <!-- Right: Visual -->
          <div class="relative h-96 hidden lg:block">
            <div class="absolute inset-0 bg-linear-to-br from-indigo-600/20 via-cyan-600/10 to-transparent rounded-3xl blur-2xl" />
            <div class="absolute inset-8 border border-white/10 rounded-2xl backdrop-blur-md bg-white/5 flex items-center justify-center overflow-hidden">
              <div class="absolute inset-0 bg-linear-to-br from-indigo-600/10 to-transparent" />
              <div class="relative text-center space-y-4">
                <div class="text-6xl">🏗️</div>
                <p class="text-white/60 text-sm max-w-xs">Built for shipping, not chatting</p>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ============================================
         FEATURES SECTION (IMPROVED)
        ============================================ -->
    <section class="relative py-24 sm:py-40 border-t border-white/10 overflow-hidden">
      <!-- Background grid -->
      <div class="absolute inset-0 opacity-10">
        <svg class="w-full h-full" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <pattern id="grid-features" width="40" height="40" patternUnits="userSpaceOnUse">
              <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#grid-features)" />
        </svg>
      </div>

      <div class="max-w-6xl mx-auto px-6 relative z-10">
        <!-- Section header -->
        <div class="text-center mb-20 space-y-4">
          <h2 class="text-5xl sm:text-6xl font-black text-white leading-tight">
            Everything you need
          </h2>
          <p class="text-xl text-white/60 max-w-2xl mx-auto leading-relaxed font-light">
            Orchestrate models, maintain state, and deploy artifacts in one unified platform.
          </p>
        </div>

        <!-- Features grid -->
        <div class="grid md:grid-cols-3 gap-6 sm:gap-8">

          <!-- Feature 1: Multi-LLM Orchestration -->
          <div 
            class="group relative cursor-pointer"
            @mouseenter="activeFeature = 0"
            @mouseleave="activeFeature = null"
          >
            <!-- Background glow -->
            <div class="absolute -inset-1 bg-linear-to-br from-indigo-600 to-indigo-400 rounded-3xl blur-2xl opacity-0 group-hover:opacity-50 transition duration-500" />
            
            <!-- Card -->
            <div class="relative bg-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 h-full space-y-6 group-hover:border-indigo-400/50 transition duration-300 overflow-hidden">
              <!-- Decorative accent -->
              <div class="absolute -top-12 -right-12 w-40 h-40 bg-indigo-500/20 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition duration-500" />
              
              <!-- Icon -->
              <div class="relative w-16 h-16 rounded-2xl bg-linear-to-br from-indigo-500/30 to-indigo-400/10 flex items-center justify-center text-4xl border border-indigo-400/30 group-hover:border-indigo-400/60 transition">
                <span class="group-hover:scale-125 transition duration-300">🔀</span>
              </div>

              <!-- Content -->
              <div class="relative space-y-3">
                <h3 class="text-2xl font-bold text-white group-hover:text-indigo-200 transition">
                  Multi-LLM<br>Orchestration
                </h3>
                <p class="text-white/60 leading-relaxed">
                  Route reasoning, creativity, and execution across models without losing context or state.
                </p>
              </div>

              <!-- Features list -->
              <div class="relative pt-4 border-t border-white/10 space-y-2">
                <div class="flex items-center gap-3 text-white/60 group-hover:text-white/80 transition text-sm">
                  <span class="w-1.5 h-1.5 rounded-full bg-indigo-400" />
                  Smart routing engine
                </div>
                <div class="flex items-center gap-3 text-white/60 group-hover:text-white/80 transition text-sm">
                  <span class="w-1.5 h-1.5 rounded-full bg-indigo-400" />
                  Zero-loss context switching
                </div>
              </div>

              <!-- Bottom accent -->
              <div class="absolute bottom-0 left-0 right-0 h-1 bg-linear-to-r from-indigo-600 to-indigo-400 transform scale-x-0 group-hover:scale-x-100 transition duration-500 origin-left" />
            </div>
          </div>

          <!-- Feature 2: Stateful Projects -->
          <div 
            class="group relative cursor-pointer md:mt-8"
            @mouseenter="activeFeature = 1"
            @mouseleave="activeFeature = null"
          >
            <!-- Background glow -->
            <div class="absolute -inset-1 bg-linear-to-br from-cyan-600 to-cyan-400 rounded-3xl blur-2xl opacity-0 group-hover:opacity-50 transition duration-500" />
            
            <!-- Card -->
            <div class="relative bg-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 h-full space-y-6 group-hover:border-cyan-400/50 transition duration-300 overflow-hidden">
              <!-- Decorative accent -->
              <div class="absolute -top-12 -right-12 w-40 h-40 bg-cyan-500/20 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition duration-500" />
              
              <!-- Icon -->
              <div class="relative w-16 h-16 rounded-2xl bg-linear-to-br from-cyan-500/30 to-cyan-400/10 flex items-center justify-center text-4xl border border-cyan-400/30 group-hover:border-cyan-400/60 transition">
                <span class="group-hover:scale-125 transition duration-300">💾</span>
              </div>

              <!-- Content -->
              <div class="relative space-y-3">
                <h3 class="text-2xl font-bold text-white group-hover:text-cyan-200 transition">
                  Stateful<br>Projects
                </h3>
                <p class="text-white/60 leading-relaxed">
                  Every project has memory, structure, and a complete lifecycle—not just a fleeting chat history.
                </p>
              </div>

              <!-- Features list -->
              <div class="relative pt-4 border-t border-white/10 space-y-2">
                <div class="flex items-center gap-3 text-white/60 group-hover:text-white/80 transition text-sm">
                  <span class="w-1.5 h-1.5 rounded-full bg-cyan-400" />
                  Persistent memory banks
                </div>
                <div class="flex items-center gap-3 text-white/60 group-hover:text-white/80 transition text-sm">
                  <span class="w-1.5 h-1.5 rounded-full bg-cyan-400" />
                  Full project lineage
                </div>
              </div>

              <!-- Bottom accent -->
              <div class="absolute bottom-0 left-0 right-0 h-1 bg-linear-to-r from-cyan-600 to-cyan-400 transform scale-x-0 group-hover:scale-x-100 transition duration-500 origin-left" />
            </div>
          </div>

          <!-- Feature 3: Ship-Ready Outputs -->
          <div 
            class="group relative cursor-pointer"
            @mouseenter="activeFeature = 2"
            @mouseleave="activeFeature = null"
          >
            <!-- Background glow -->
            <div class="absolute -inset-1 bg-linear-to-br from-emerald-600 to-emerald-400 rounded-3xl blur-2xl opacity-0 group-hover:opacity-50 transition duration-500" />
            
            <!-- Card -->
            <div class="relative bg-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 h-full space-y-6 group-hover:border-emerald-400/50 transition duration-300 overflow-hidden">
              <!-- Decorative accent -->
              <div class="absolute -top-12 -right-12 w-40 h-40 bg-emerald-500/20 rounded-full blur-3xl opacity-0 group-hover:opacity-100 transition duration-500" />
              
              <!-- Icon -->
              <div class="relative w-16 h-16 rounded-2xl bg-linear-to-br from-emerald-500/30 to-emerald-400/10 flex items-center justify-center text-4xl border border-emerald-400/30 group-hover:border-emerald-400/60 transition">
                <span class="group-hover:scale-125 transition duration-300">🚀</span>
              </div>

              <!-- Content -->
              <div class="relative space-y-3">
                <h3 class="text-2xl font-bold text-white group-hover:text-emerald-200 transition">
                  Ship-Ready<br>Outputs
                </h3>
                <p class="text-white/60 leading-relaxed">
                  Generate specs, repos, docs, websites, and narratives you can deploy immediately to production.
                </p>
              </div>

              <!-- Features list -->
              <div class="relative pt-4 border-t border-white/10 space-y-2">
                <div class="flex items-center gap-3 text-white/60 group-hover:text-white/80 transition text-sm">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                  Production-grade quality
                </div>
                <div class="flex items-center gap-3 text-white/60 group-hover:text-white/80 transition text-sm">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                  Deploy in minutes
                </div>
              </div>

              <!-- Bottom accent -->
              <div class="absolute bottom-0 left-0 right-0 h-1 bg-linear-to-r from-emerald-600 to-emerald-400 transform scale-x-0 group-hover:scale-x-100 transition duration-500 origin-left" />
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ============================================
         FINAL CTA SECTION
        ============================================ -->
    <section class="relative py-24 sm:py-40 pb-40">
      <div class="max-w-6xl mx-auto px-6">
        <div class="group relative">
          <!-- Gradient background -->
          <div class="absolute inset-0 bg-linear-to-br from-indigo-600/40 via-cyan-600/30 to-emerald-600/20 rounded-4xl blur-3xl opacity-0 group-hover:opacity-100 transition duration-500" />
          
          <!-- Card -->
          <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/20 rounded-4xl px-8 sm:px-16 py-16 sm:py-24 space-y-10 group-hover:border-white/30 transition duration-300">
            
            <div class="space-y-6 max-w-3xl">
              <h2 class="text-6xl sm:text-7xl font-black text-white leading-tight">
                Build optimistically.
              </h2>
              <p class="text-2xl text-white/70 leading-relaxed font-light">
                Web3-native tools for people who actually ship. No theory, no endless tweaking—just <span class="text-white font-bold">results</span> that matter.
              </p>
            </div>

            <NuxtLink
              to="/build"
              class="group/btn relative inline-flex px-10 py-5 rounded-xl font-bold text-white text-lg overflow-hidden"
            >
              <!-- Gradient background -->
              <div class="absolute inset-0 bg-linear-to-r from-indigo-600 via-indigo-500 to-cyan-500 opacity-100 group-hover/btn:opacity-90 transition-opacity duration-300" />
              <!-- Shimmer -->
              <div class="absolute inset-0 bg-linear-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover/btn:translate-x-full transition-transform duration-700" />
              <!-- Text -->
              <span class="relative flex items-center gap-3">
                Enter workspace
                <svg class="w-6 h-6 group-hover/btn:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </span>
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const activeFeature = ref<number | null>(null)

useHead({
  title: 'LLM Studio - Build Web3 Products with Intention',
  meta: [
    {
      name: 'description',
      content: 'A Web3-native workspace to orchestrate LLMs, manage state, and ship real artifacts from idea to production.',
    }
  ]
})
</script>

<style scoped>
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

@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(10px);
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

.animate-float {
  animation: float 6s ease-in-out infinite;
}

.animate-float-delayed {
  animation: float-delayed 8s ease-in-out infinite;
}

.animate-fade-in {
  animation: fade-in 0.8s ease-out forwards;
  opacity: 0;
}

.animate-gradient {
  background-size: 200% 200%;
  animation: gradient 3s ease infinite;
}
</style>