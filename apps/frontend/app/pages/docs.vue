<template>
  <main class="relative min-h-screen bg-linear-to-br from-slate-950 via-purple-950 to-slate-950 pt-24 pb-20">
    <!-- Animated background -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <div class="absolute -top-40 -right-40 w-80 h-80 bg-indigo-600/10 rounded-full blur-3xl animate-pulse" />
      <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl animate-pulse delay-1000" />
    </div>

    <div class="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <section class="space-y-6 mb-20">
        <div class="space-y-4">
          <h1 class="text-5xl sm:text-6xl font-bold text-white leading-tight">
            Documentation
          </h1>
          <p class="text-lg sm:text-xl text-white/60 max-w-2xl leading-relaxed">
            Everything you need to understand and master LLM Studio.
            From core concepts to advanced workflows, we've got it covered.
          </p>
        </div>
      </section>

      <!-- Core Concepts Section -->
      <section class="space-y-8 mb-20">
        <div>
          <h2 class="text-3xl font-bold text-white mb-2">Core Concepts</h2>
          <p class="text-white/50 text-sm">Foundation of the platform</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Intent -->
          <div class="group relative">
            <div class="absolute inset-0 bg-linear-to-br from-indigo-600/20 to-cyan-500/20 rounded-xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-6 space-y-3 group-hover:border-white/30 transition-all duration-300">
              <div class="w-10 h-10 rounded-lg bg-linear-to-br from-indigo-500/20 to-cyan-500/20 flex items-center justify-center text-lg">
                🎯
              </div>
              <h3 class="text-lg font-semibold text-white">Intent</h3>
              <p class="text-white/60 text-sm leading-relaxed">
                Clear, explicit goal definition. Every build starts with intention, not iteration.
                We guide you to articulate what matters.
              </p>
            </div>
          </div>

          <!-- State Management -->
          <div class="group relative">
            <div class="absolute inset-0 bg-linear-to-br from-cyan-600/20 to-emerald-500/20 rounded-xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-6 space-y-3 group-hover:border-white/30 transition-all duration-300">
              <div class="w-10 h-10 rounded-lg bg-linear-to-br from-cyan-500/20 to-emerald-500/20 flex items-center justify-center text-lg">
                💾
              </div>
              <h3 class="text-lg font-semibold text-white">State Management</h3>
              <p class="text-white/60 text-sm leading-relaxed">
                Projects maintain persistent context. Every decision is recorded, tracked, and reversible.
                Your build history is your audit trail.
              </p>
            </div>
          </div>

          <!-- Structured Flows -->
          <div class="group relative">
            <div class="absolute inset-0 bg-linear-to-br from-purple-600/20 to-pink-500/20 rounded-xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-6 space-y-3 group-hover:border-white/30 transition-all duration-300">
              <div class="w-10 h-10 rounded-lg bg-linear-to-br from-purple-500/20 to-pink-500/20 flex items-center justify-center text-lg">
                🔀
              </div>
              <h3 class="text-lg font-semibold text-white">Structured Flows</h3>
              <p class="text-white/60 text-sm leading-relaxed">
                No freeform chaos. Each step builds on the previous.
                Guide your LLM through logical, repeatable workflows.
              </p>
            </div>
          </div>

          <!-- Ship-Ready Artifacts -->
          <div class="group relative">
            <div class="absolute inset-0 bg-linear-to-br from-emerald-600/20 to-cyan-500/20 rounded-xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-6 space-y-3 group-hover:border-white/30 transition-all duration-300">
              <div class="w-10 h-10 rounded-lg bg-linear-to-br from-emerald-500/20 to-cyan-500/20 flex items-center justify-center text-lg">
                📦
              </div>
              <h3 class="text-lg font-semibold text-white">Ship-Ready Artifacts</h3>
              <p class="text-white/60 text-sm leading-relaxed">
                Output that's production-ready from day one.
                Logos, docs, code, and narratives you can actually use.
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Architecture Section -->
      <section class="space-y-8 mb-20">
        <div>
          <h2 class="text-3xl font-bold text-white mb-2">Architecture</h2>
          <p class="text-white/50 text-sm">How the platform is built</p>
        </div>

        <div class="space-y-4">
          <!-- Frontend -->
          <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-6 space-y-3 hover:border-white/30 transition-all duration-300">
            <div class="flex items-start gap-4">
              <div class="w-10 h-10 rounded-lg bg-linear-to-br from-indigo-500/20 to-cyan-500/20 flex items-center justify-center flex-shrink-0 text-lg">
                🎨
              </div>
              <div class="space-y-2">
                <h3 class="text-lg font-semibold text-white">Frontend</h3>
                <p class="text-white/60 text-sm">
                  Built with Vue 3 + Nuxt, Tailwind CSS for styling. Real-time state synchronization with reactive data flows.
                  Optimized for both desktop and mobile experiences.
                </p>
              </div>
            </div>
          </div>

          <!-- Backend Orchestration -->
          <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-6 space-y-3 hover:border-white/30 transition-all duration-300">
            <div class="flex items-start gap-4">
              <div class="w-10 h-10 rounded-lg bg-linear-to-br from-cyan-500/20 to-emerald-500/20 flex items-center justify-center flex-shrink-0 text-lg">
                ⚙️
              </div>
              <div class="space-y-2">
                <h3 class="text-lg font-semibold text-white">Backend Orchestration</h3>
                <p class="text-white/60 text-sm">
                  Handles multi-LLM routing, context persistence, and artifact generation.
                  Built on scalable cloud infrastructure with real-time progress tracking.
                </p>
              </div>
            </div>
          </div>

          <!-- LLM Routing -->
          <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-6 space-y-3 hover:border-white/30 transition-all duration-300">
            <div class="flex items-start gap-4">
              <div class="w-10 h-10 rounded-lg bg-linear-to-br from-purple-500/20 to-pink-500/20 flex items-center justify-center flex-shrink-0 text-lg">
                🧠
              </div>
              <div class="space-y-2">
                <h3 class="text-lg font-semibold text-white">Multi-LLM Routing</h3>
                <p class="text-white/60 text-sm">
                  Intelligently routes tasks to different models based on complexity and requirements.
                  Reasoning, creativity, and execution each get optimized separately.
                </p>
              </div>
            </div>
          </div>

          <!-- Web3 Integration -->
          <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-6 space-y-3 hover:border-white/30 transition-all duration-300">
            <div class="flex items-start gap-4">
              <div class="w-10 h-10 rounded-lg bg-linear-to-br from-emerald-500/20 to-cyan-500/20 flex items-center justify-center flex-shrink-0 text-lg">
                🔗
              </div>
              <div class="space-y-2">
                <h3 class="text-lg font-semibold text-white">Web3 Integration</h3>
                <p class="text-white/60 text-sm">
                  Wallet authentication, on-chain artifact verification, and decentralized data ownership.
                  Your identity is your wallet. Your data is yours.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Getting Started Section -->
      <section class="space-y-8">
        <div>
          <h2 class="text-3xl font-bold text-white mb-2">Getting Started</h2>
          <p class="text-white/50 text-sm">Your first steps with LLM Studio</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="bg-linear-to-br from-indigo-500/10 to-cyan-500/10 border border-indigo-500/20 rounded-lg p-4 space-y-2">
            <p class="text-sm font-semibold text-indigo-400">Step 1</p>
            <h3 class="text-white font-semibold">Connect Wallet</h3>
            <p class="text-xs text-white/60">
              Sign in with your Solana wallet to start building.
            </p>
          </div>

          <div class="bg-linear-to-br from-cyan-500/10 to-emerald-500/10 border border-cyan-500/20 rounded-lg p-4 space-y-2">
            <p class="text-sm font-semibold text-cyan-400">Step 2</p>
            <h3 class="text-white font-semibold">Define Your Project</h3>
            <p class="text-xs text-white/60">
              Walk through our guided questionnaire to shape your vision.
            </p>
          </div>

          <div class="bg-linear-to-br from-purple-500/10 to-pink-500/10 border border-purple-500/20 rounded-lg p-4 space-y-2">
            <p class="text-sm font-semibold text-purple-400">Step 3</p>
            <h3 class="text-white font-semibold">Generate & Ship</h3>
            <p class="text-xs text-white/60">
              AI generates assets. Download, customize, and launch.
            </p>
          </div>
        </div>
      </section>
    </div>
  </main>
</template>

<style scoped>
/* No custom styles needed - all Tailwind */
</style>