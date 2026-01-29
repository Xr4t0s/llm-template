<template>
  <div class="relative overflow-hidden">

    <!-- ============================================
         HERO SECTION
        ============================================ -->
    <section class="relative min-h-[calc(100vh-80px)] flex items-center justify-center pt-20 pb-20">
      <div class="max-w-6xl mx-auto px-6 w-full">
        <div class="max-w-4xl space-y-8 mx-auto text-center lg:text-left lg:mx-0">

          <!-- Main Heading -->
          <div class="space-y-4">
            <h1 class="text-5xl sm:text-6xl lg:text-7xl font-bold leading-tight text-white">
              Build products
              <br />
              <span class="bg-linear-to-r from-indigo-400 via-cyan-400 to-emerald-400 bg-clip-text text-transparent">
                with intention
              </span>
            </h1>
          </div>

          <!-- Subheading -->
          <p class="text-lg sm:text-xl text-white/60 max-w-2xl mx-auto lg:mx-0 leading-relaxed">
            A Web3-native workspace to orchestrate LLMs using our customs MCP services, where you can manage state, and ship real artifacts —
            <span class="text-white font-medium">from idea to production.</span>
          </p>

          <!-- CTA Buttons -->
          <div class="flex flex-col sm:flex-row items-center gap-4 pt-6 lg:justify-start justify-center">
            <NuxtLink
              to="/build"
              class="group relative px-8 py-4 rounded-xl font-semibold text-white overflow-hidden"
            >
              <!-- Gradient background -->
              <div class="absolute inset-0 bg-linear-to-r from-indigo-600 to-cyan-500 opacity-100 group-hover:opacity-90 transition-opacity" />
              <!-- Shimmer effect -->
              <div class="absolute inset-0 bg-linear-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-500" />
              <!-- Text -->
              <span class="relative flex items-center gap-2">
                Start building
                <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </span>
            </NuxtLink>

            <NuxtLink
              to="/docs"
              class="group relative px-8 py-4 rounded-xl font-semibold text-white border-2 border-white/20 hover:border-white/40 transition-colors"
            >
              <span class="flex items-center gap-2">
                Read the docs
                <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </span>
            </NuxtLink>
          </div>

        </div>
      </div>

      <!-- Animated glow elements -->
      <div class="absolute top-1/4 -right-32 w-96 h-96 bg-indigo-600/20 rounded-full blur-3xl -z-10 animate-pulse" />
      <div class="absolute bottom-0 -left-32 w-80 h-80 bg-cyan-500/20 rounded-full blur-3xl -z-10 animate-pulse delay-700" />
    </section>

    <!-- ============================================
         MANIFESTO SECTION
        ============================================ -->
    <section class="relative py-20 sm:py-32 border-t border-white/10">
      <div class="max-w-6xl mx-auto px-6">
        <div class="max-w-3xl space-y-6">

          <h2 class="text-3xl sm:text-4xl font-bold text-white">
            How do we prevent you from <span class="text-transparent bg-linear-to-r from-indigo-400 to-cyan-400 bg-clip-text">prompting.</span>
          </h2>

          <p class="text-lg text-white/60 leading-relaxed">
            Most AI tools are optimized for conversation. <span class="text-white font-medium">LLM Studio is optimized for construction.</span> Persistent context, explicit intent, structured flows — everything you need to ship real products.
          </p>

        </div>
      </div>
    </section>

    <!-- ============================================
         FEATURES SECTION
        ============================================ -->
    <section class="relative py-20 sm:py-32">
      <div class="max-w-6xl mx-auto px-6">
        <div class="grid md:grid-cols-3 gap-6 sm:gap-8">

          <!-- Feature 1 -->
          <div class="group relative">
            <div class="absolute inset-0 bg-linear-to-br from-indigo-600/20 to-transparent rounded-2xl blur opacity-0 group-hover:opacity-100 transition duration-500" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-8 space-y-4 group-hover:border-white/20 transition duration-300">
              <div class="w-12 h-12 rounded-lg bg-linear-to-br from-indigo-500/20 to-indigo-400/20 flex items-center justify-center text-2xl">
                🔀
              </div>
              <h3 class="text-lg font-semibold text-white">
                Multi-LLM orchestration
              </h3>
              <p class="text-white/60 leading-relaxed">
                Route reasoning, creativity, and execution across models without losing state.
              </p>
            </div>
          </div>

          <!-- Feature 2 -->
          <div class="group relative">
            <div class="absolute inset-0 bg-linear-to-br from-cyan-600/20 to-transparent rounded-2xl blur opacity-0 group-hover:opacity-100 transition duration-500" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-8 space-y-4 group-hover:border-white/20 transition duration-300">
              <div class="w-12 h-12 rounded-lg bg-linear-to-br from-cyan-500/20 to-cyan-400/20 flex items-center justify-center text-2xl">
                💾
              </div>
              <h3 class="text-lg font-semibold text-white">
                Stateful projects
              </h3>
              <p class="text-white/60 leading-relaxed">
                Every project has memory, structure, and a lifecycle — not just a chat history.
              </p>
            </div>
          </div>

          <!-- Feature 3 -->
          <div class="group relative">
            <div class="absolute inset-0 bg-linear-to-br from-emerald-600/20 to-transparent rounded-2xl blur opacity-0 group-hover:opacity-100 transition duration-500" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-8 space-y-4 group-hover:border-white/20 transition duration-300">
              <div class="w-12 h-12 rounded-lg bg-linear-to-br from-emerald-500/20 to-emerald-400/20 flex items-center justify-center text-2xl">
                🚀
              </div>
              <h3 class="text-lg font-semibold text-white">
                Ship-ready outputs
              </h3>
              <p class="text-white/60 leading-relaxed">
                Generate specs, repositories, docs, websites, and narratives you can deploy.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- ============================================
         FINAL CTA SECTION
        ============================================ -->
    <section class="relative py-20 sm:py-32 pb-32">
      <div class="max-w-6xl mx-auto px-6">
        <div class="group relative">
          <!-- Gradient glow background -->
          <div class="absolute inset-0 bg-linear-to-br from-indigo-600/20 via-purple-600/20 to-transparent rounded-3xl blur opacity-0 group-hover:opacity-100 transition duration-500" />
          
          <!-- Card -->
          <div class="relative bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl px-8 sm:px-12 py-12 sm:py-16 space-y-6 group-hover:border-white/20 transition duration-300">
            
            <div class="space-y-4">
              <h2 class="text-4xl sm:text-5xl font-bold text-white">
                Build optimistically.
              </h2>
              <p class="text-lg text-white/60 max-w-2xl">
                Web3-native tools for people who actually ship. No theory, no fluff—just results.
              </p>
            </div>

            <NuxtLink
              to="/build"
              class="group/btn relative inline-flex px-8 py-4 rounded-xl font-semibold text-white overflow-hidden"
            >
              <!-- Gradient background -->
              <div class="absolute inset-0 bg-linear-to-r from-indigo-600 to-cyan-500 opacity-100 group-hover/btn:opacity-90 transition-opacity" />
              <!-- Text -->
              <span class="relative flex items-center gap-2">
                Enter workspace
                <svg class="w-5 h-5 group-hover/btn:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
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
// Page-specific setup if needed
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