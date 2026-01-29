<template>
  <main class="relative min-h-screen bg-black pt-24 sm:pt-32 pb-24 sm:pb-32 overflow-hidden">
    <!-- Animated background -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <!-- Gradient orbs -->
      <div class="absolute top-1/4 -right-40 w-96 h-96 bg-indigo-600/25 rounded-full blur-3xl animate-float" />
      <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-cyan-500/20 rounded-full blur-3xl animate-float-delayed" />
      <div class="absolute top-1/2 left-1/2 w-80 h-80 bg-emerald-500/15 rounded-full blur-3xl animate-pulse" style="animation-duration: 8s;" />
      
      <!-- Grid -->
      <svg class="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <pattern id="grid-docs" width="50" height="50" patternUnits="userSpaceOnUse">
            <path d="M 50 0 L 0 0 0 50" fill="none" stroke="rgba(139, 92, 246, 0.1)" stroke-width="1"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid-docs)" />
      </svg>
      
      <!-- Gradient overlays -->
      <div class="absolute inset-0 bg-linear-to-b from-black/0 via-transparent to-black/40" />
    </div>

    <div class="relative z-10 max-w-6xl mx-auto px-6 sm:px-8">
      <!-- Hero Header -->
      <section class="space-y-8 mb-24 sm:mb-32 max-w-4xl">
        <div class="space-y-6">
          <!-- Accent -->
          <div class="inline-block">
            <span class="text-sm font-mono text-transparent bg-clip-text bg-linear-to-r from-indigo-400 to-cyan-400 tracking-widest uppercase">
              📚 Documentation Hub
            </span>
          </div>
          
          <!-- Title -->
          <h1 class="text-6xl sm:text-7xl lg:text-8xl font-black leading-tight text-white">
            Learn to
            <br />
            <span class="bg-linear-to-r from-indigo-400 via-cyan-400 to-emerald-400 bg-clip-text text-transparent animate-gradient">
              build better
            </span>
          </h1>
          
          <!-- Subtitle -->
          <p class="text-xl sm:text-2xl text-white/70 leading-relaxed font-light max-w-2xl">
            Master LLM Studio from fundamentals to advanced workflows. Everything you need to orchestrate AI and ship products that matter.
          </p>
        </div>
      </section>

      <!-- Core Concepts Section -->
      <section class="space-y-12 mb-24 sm:mb-32">
        <div class="space-y-4">
          <h2 class="text-4xl sm:text-5xl font-black text-white">Core Concepts</h2>
          <p class="text-lg text-white/50 font-light">The foundation that makes everything possible</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8">
          <!-- Intent -->
          <div class="group relative cursor-pointer h-full">
            <!-- Background glow -->
            <div class="absolute -inset-2 bg-linear-to-br from-indigo-600/20 to-cyan-500/10 rounded-3xl blur-2xl opacity-0 group-hover:opacity-60 transition-opacity duration-500" />
            
            <!-- Card -->
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 sm:p-10 space-y-5 group-hover:border-indigo-400/40 transition-all duration-300 h-full flex flex-col">
              <!-- Icon -->
              <div class="w-16 h-16 rounded-2xl bg-linear-to-br from-indigo-500/30 to-cyan-500/10 flex items-center justify-center text-4xl group-hover:scale-110 group-hover:rotate-6 transition-all duration-300 border border-indigo-400/20">
                🎯
              </div>
              
              <!-- Content -->
              <div class="space-y-3 flex-1">
                <h3 class="text-2xl font-bold text-white group-hover:text-indigo-200 transition-colors">Intent</h3>
                <p class="text-white/60 leading-relaxed">
                  Clear, explicit goal definition. Every project starts with intention, not endless iteration. We guide you to articulate what truly matters.
                </p>
              </div>
              
              <!-- Footer accent -->
              <div class="pt-4 border-t border-white/10">
                <p class="text-sm text-indigo-300 font-medium">Why it matters →</p>
              </div>
            </div>
          </div>

          <!-- State Management -->
          <div class="group relative cursor-pointer h-full">
            <!-- Background glow -->
            <div class="absolute -inset-2 bg-linear-to-br from-cyan-600/20 to-emerald-500/10 rounded-3xl blur-2xl opacity-0 group-hover:opacity-60 transition-opacity duration-500" />
            
            <!-- Card -->
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 sm:p-10 space-y-5 group-hover:border-cyan-400/40 transition-all duration-300 h-full flex flex-col">
              <!-- Icon -->
              <div class="w-16 h-16 rounded-2xl bg-linear-to-br from-cyan-500/30 to-emerald-500/10 flex items-center justify-center text-4xl group-hover:scale-110 group-hover:rotate-6 transition-all duration-300 border border-cyan-400/20">
                💾
              </div>
              
              <!-- Content -->
              <div class="space-y-3 flex-1">
                <h3 class="text-2xl font-bold text-white group-hover:text-cyan-200 transition-colors">State Management</h3>
                <p class="text-white/60 leading-relaxed">
                  Projects maintain persistent context across sessions. Every decision is recorded, tracked, and reversible. Your build history is your audit trail.
                </p>
              </div>
              
              <!-- Footer accent -->
              <div class="pt-4 border-t border-white/10">
                <p class="text-sm text-cyan-300 font-medium">Learn more →</p>
              </div>
            </div>
          </div>

          <!-- Structured Flows -->
          <div class="group relative cursor-pointer h-full">
            <!-- Background glow -->
            <div class="absolute -inset-2 bg-linear-to-br from-purple-600/20 to-pink-500/10 rounded-3xl blur-2xl opacity-0 group-hover:opacity-60 transition-opacity duration-500" />
            
            <!-- Card -->
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 sm:p-10 space-y-5 group-hover:border-purple-400/40 transition-all duration-300 h-full flex flex-col">
              <!-- Icon -->
              <div class="w-16 h-16 rounded-2xl bg-linear-to-br from-purple-500/30 to-pink-500/10 flex items-center justify-center text-4xl group-hover:scale-110 group-hover:rotate-6 transition-all duration-300 border border-purple-400/20">
                🔀
              </div>
              
              <!-- Content -->
              <div class="space-y-3 flex-1">
                <h3 class="text-2xl font-bold text-white group-hover:text-purple-200 transition-colors">Structured Flows</h3>
                <p class="text-white/60 leading-relaxed">
                  No freeform chaos. Each step builds on the previous with purpose. Guide your LLMs through logical, repeatable workflows that compound.
                </p>
              </div>
              
              <!-- Footer accent -->
              <div class="pt-4 border-t border-white/10">
                <p class="text-sm text-purple-300 font-medium">Explore →</p>
              </div>
            </div>
          </div>

          <!-- Ship-Ready Artifacts -->
          <div class="group relative cursor-pointer h-full">
            <!-- Background glow -->
            <div class="absolute -inset-2 bg-linear-to-br from-emerald-600/20 to-cyan-500/10 rounded-3xl blur-2xl opacity-0 group-hover:opacity-60 transition-opacity duration-500" />
            
            <!-- Card -->
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 sm:p-10 space-y-5 group-hover:border-emerald-400/40 transition-all duration-300 h-full flex flex-col">
              <!-- Icon -->
              <div class="w-16 h-16 rounded-2xl bg-linear-to-br from-emerald-500/30 to-cyan-500/10 flex items-center justify-center text-4xl group-hover:scale-110 group-hover:rotate-6 transition-all duration-300 border border-emerald-400/20">
                📦
              </div>
              
              <!-- Content -->
              <div class="space-y-3 flex-1">
                <h3 class="text-2xl font-bold text-white group-hover:text-emerald-200 transition-colors">Ship-Ready Artifacts</h3>
                <p class="text-white/60 leading-relaxed">
                  Output that's production-ready from day one. Logos, documentation, code, and narratives you can actually use immediately.
                </p>
              </div>
              
              <!-- Footer accent -->
              <div class="pt-4 border-t border-white/10">
                <p class="text-sm text-emerald-300 font-medium">See examples →</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Architecture Section -->
      <section class="space-y-12 mb-24 sm:mb-32">
        <div class="space-y-4">
          <h2 class="text-4xl sm:text-5xl font-black text-white">Architecture</h2>
          <p class="text-lg text-white/50 font-light">Built for performance and reliability at scale</p>
        </div>

        <div class="space-y-4 sm:space-y-5">
          <!-- Frontend -->
          <div class="group relative">
            <div class="absolute -inset-1 bg-linear-to-r from-indigo-600/10 to-cyan-600/10 rounded-2xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 sm:p-8 group-hover:border-white/20 transition-all duration-300">
              <div class="flex items-start gap-4 sm:gap-6">
                <!-- Icon -->
                <div class="w-14 h-14 rounded-xl bg-linear-to-br from-indigo-500/30 to-cyan-500/20 flex items-center justify-center shrink-0 text-3xl border border-indigo-400/20">
                  🎨
                </div>
                
                <!-- Content -->
                <div class="space-y-2 flex-1 pt-1">
                  <h3 class="text-xl font-bold text-white group-hover:text-indigo-200 transition-colors">Frontend</h3>
                  <p class="text-white/60 leading-relaxed">
                    Built with Vue 3 + Nuxt for reactive experiences. Tailwind CSS for precise styling. Real-time state sync with optimized data flows for both desktop and mobile.
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Backend Orchestration -->
          <div class="group relative">
            <div class="absolute -inset-1 bg-linear-to-r from-cyan-600/10 to-emerald-600/10 rounded-2xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 sm:p-8 group-hover:border-white/20 transition-all duration-300">
              <div class="flex items-start gap-4 sm:gap-6">
                <!-- Icon -->
                <div class="w-14 h-14 rounded-xl bg-linear-to-br from-cyan-500/30 to-emerald-500/20 flex items-center justify-center shrink-0 text-3xl border border-cyan-400/20">
                  ⚙️
                </div>
                
                <!-- Content -->
                <div class="space-y-2 flex-1 pt-1">
                  <h3 class="text-xl font-bold text-white group-hover:text-cyan-200 transition-colors">Backend Orchestration</h3>
                  <p class="text-white/60 leading-relaxed">
                    Handles multi-LLM routing with intelligent model selection. Manages context persistence across sessions. Scalable cloud infrastructure with real-time progress tracking and error recovery.
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- LLM Routing -->
          <div class="group relative">
            <div class="absolute -inset-1 bg-linear-to-r from-purple-600/10 to-pink-600/10 rounded-2xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 sm:p-8 group-hover:border-white/20 transition-all duration-300">
              <div class="flex items-start gap-4 sm:gap-6">
                <!-- Icon -->
                <div class="w-14 h-14 rounded-xl bg-linear-to-br from-purple-500/30 to-pink-500/20 flex items-center justify-center shrink-0 text-3xl border border-purple-400/20">
                  🧠
                </div>
                
                <!-- Content -->
                <div class="space-y-2 flex-1 pt-1">
                  <h3 class="text-xl font-bold text-white group-hover:text-purple-200 transition-colors">Multi-LLM Routing</h3>
                  <p class="text-white/60 leading-relaxed">
                    Intelligently routes tasks to different models based on complexity and requirements. Separates reasoning, creativity, and execution for optimal results.
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- Web3 Integration -->
          <div class="group relative">
            <div class="absolute -inset-1 bg-linear-to-r from-emerald-600/10 to-indigo-600/10 rounded-2xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 sm:p-8 group-hover:border-white/20 transition-all duration-300">
              <div class="flex items-start gap-4 sm:gap-6">
                <!-- Icon -->
                <div class="w-14 h-14 rounded-xl bg-linear-to-br from-emerald-500/30 to-indigo-500/20 flex items-center justify-center shrink-0 text-3xl border border-emerald-400/20">
                  🔗
                </div>
                
                <!-- Content -->
                <div class="space-y-2 flex-1 pt-1">
                  <h3 class="text-xl font-bold text-white group-hover:text-emerald-200 transition-colors">Web3 Integration</h3>
                  <p class="text-white/60 leading-relaxed">
                    Wallet authentication for secure entry. On-chain artifact verification for authenticity. Decentralized data ownership means your identity is your wallet and your data is yours.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Getting Started Section -->
      <section class="space-y-12">
        <div class="space-y-4">
          <h2 class="text-4xl sm:text-5xl font-black text-white">Getting Started</h2>
          <p class="text-lg text-white/50 font-light">Your journey begins in three steps</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8">
          <!-- Step 1 -->
          <div class="group relative">
            <div class="absolute -inset-2 bg-linear-to-br from-indigo-600/20 to-cyan-500/10 rounded-3xl blur opacity-0 group-hover:opacity-50 transition-opacity duration-500" />
            <div class="relative bg-linear-to-br from-indigo-500/15 to-indigo-500/5 backdrop-blur-xl border border-indigo-500/20 rounded-3xl p-8 sm:p-10 space-y-6 group-hover:border-indigo-400/40 transition-all duration-300 h-full flex flex-col">
              <!-- Step indicator -->
              <div class="inline-flex w-12 h-12 rounded-full bg-linear-to-r from-indigo-500 to-cyan-500 items-center justify-center">
                <span class="text-white font-black text-lg">1</span>
              </div>
              
              <!-- Content -->
              <div class="space-y-3 flex-1">
                <h3 class="text-2xl font-bold text-white">Connect Wallet</h3>
                <p class="text-white/60 leading-relaxed">
                  Authenticate with your Solana wallet to claim your identity and secure your session.
                </p>
              </div>
              
              <!-- CTA -->
              <div class="pt-4 border-t border-indigo-400/20">
                <p class="text-sm text-indigo-300 font-medium">2 minutes →</p>
              </div>
            </div>
          </div>

          <!-- Step 2 -->
          <div class="group relative">
            <div class="absolute -inset-2 bg-linear-to-br from-cyan-600/20 to-emerald-500/10 rounded-3xl blur opacity-0 group-hover:opacity-50 transition-opacity duration-500" />
            <div class="relative bg-linear-to-br from-cyan-500/15 to-cyan-500/5 backdrop-blur-xl border border-cyan-500/20 rounded-3xl p-8 sm:p-10 space-y-6 group-hover:border-cyan-400/40 transition-all duration-300 h-full flex flex-col">
              <!-- Step indicator -->
              <div class="inline-flex w-12 h-12 rounded-full bg-linear-to-r from-cyan-500 to-emerald-500 items-center justify-center">
                <span class="text-white font-black text-lg">2</span>
              </div>
              
              <!-- Content -->
              <div class="space-y-3 flex-1">
                <h3 class="text-2xl font-bold text-white">Define Your Vision</h3>
                <p class="text-white/60 leading-relaxed">
                  Walk through our guided questionnaire to shape and articulate your project's intent and direction.
                </p>
              </div>
              
              <!-- CTA -->
              <div class="pt-4 border-t border-cyan-400/20">
                <p class="text-sm text-cyan-300 font-medium">5 minutes →</p>
              </div>
            </div>
          </div>

          <!-- Step 3 -->
          <div class="group relative">
            <div class="absolute -inset-2 bg-linear-to-br from-emerald-600/20 to-purple-500/10 rounded-3xl blur opacity-0 group-hover:opacity-50 transition-opacity duration-500" />
            <div class="relative bg-linear-to-br from-emerald-500/15 to-emerald-500/5 backdrop-blur-xl border border-emerald-500/20 rounded-3xl p-8 sm:p-10 space-y-6 group-hover:border-emerald-400/40 transition-all duration-300 h-full flex flex-col">
              <!-- Step indicator -->
              <div class="inline-flex w-12 h-12 rounded-full bg-linear-to-r from-emerald-500 to-cyan-500 items-center justify-center">
                <span class="text-white font-black text-lg">3</span>
              </div>
              
              <!-- Content -->
              <div class="space-y-3 flex-1">
                <h3 class="text-2xl font-bold text-white">Generate & Ship</h3>
                <p class="text-white/60 leading-relaxed">
                  AI generates production-ready assets. Download, customize if needed, and launch your project.
                </p>
              </div>
              
              <!-- CTA -->
              <div class="pt-4 border-t border-emerald-400/20">
                <p class="text-sm text-emerald-300 font-medium">Ready immediately →</p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </main>
</template>

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

.animate-gradient {
  background-size: 200% 200%;
  animation: gradient 3s ease infinite;
}
</style>