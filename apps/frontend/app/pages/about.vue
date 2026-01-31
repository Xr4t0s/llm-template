<template>
  <main class="relative min-h-screen bg-black pt-24 sm:pt-32 pb-24 sm:pb-32 overflow-hidden">
    <!-- Animated background -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <!-- Gradient orbs -->
      <div class="absolute top-1/4 -right-40 w-96 h-96 bg-indigo-600/25 rounded-full blur-3xl animate-float" />
      <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-cyan-500/20 rounded-full blur-3xl animate-float-delayed" />
      <div class="absolute top-2/3 left-1/3 w-80 h-80 bg-emerald-500/15 rounded-full blur-3xl animate-pulse" style="animation-duration: 8s;" />
      
      <!-- Grid -->
      <svg class="absolute inset-0 w-full h-full opacity-5" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <pattern id="grid-about" width="50" height="50" patternUnits="userSpaceOnUse">
            <path d="M 50 0 L 0 0 0 50" fill="none" stroke="rgba(139, 92, 246, 0.1)" stroke-width="1"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid-about)" />
      </svg>
      
      <!-- Gradient overlays -->
      <div class="absolute inset-0 bg-linear-to-b from-black/0 via-transparent to-black/40" />
    </div>

    <div class="relative z-10 max-w-5xl mx-auto px-6 sm:px-8">
      <!-- Hero Header -->
      <section class="space-y-8 mb-24 sm:mb-32 max-w-4xl">
        <div class="space-y-6">
          <!-- Accent -->
          <div class="inline-block">
            <span class="text-sm font-mono text-transparent bg-clip-text bg-linear-to-r from-indigo-400 to-cyan-400 tracking-widest uppercase">
              🎯 Our Story
            </span>
          </div>
          
          <!-- Title -->
          <h1 class="text-6xl sm:text-7xl lg:text-8xl font-thin leading-tight text-white">
            Built by
            <br />
            <span class="bg-linear-to-r from-indigo-400 via-cyan-400 to-emerald-400 bg-clip-text text-transparent">
              builders for builders
            </span>
          </h1>
          
          <!-- Subtitle -->
          <p class="text-xl sm:text-2xl text-white/70 leading-relaxed font-light max-w-2xl">
            We're not building another AI chat wrapper. We're building a workspace for clarity, structure, and real production-ready output.
          </p>
        </div>
      </section>

      <!-- Mission Section -->
      <section class="space-y-10 mb-24 sm:mb-32">
        <div class="space-y-4">
          <h2 class="text-4xl sm:text-5xl font-thin text-white">Our Mission</h2>
        </div>

        <div class="group relative">
          <!-- Glow background -->
          <div class="absolute -inset-3 bg-linear-to-br from-indigo-600/20 via-cyan-600/20 to-emerald-600/20 rounded-4xl blur-3xl opacity-0 group-hover:opacity-50 transition-opacity duration-500" />
          
          <!-- Card -->
          <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/10 rounded-4xl p-10 sm:p-14 space-y-8 group-hover:border-white/20 transition-all duration-300">
            <div class="space-y-8">
              <p class="text-xl text-white/80 leading-relaxed font-light">
                We noticed something troubling: Web3 builders were drowning in fragmented tools. Too many tabs. Too many frameworks. Too much cognitive overhead. Context loss between sessions. Outputs that needed further refinement.
              </p>
              
              <div class="h-px bg-linear-to-r from-white/0 via-white/20 to-white/0" />
              
              <p class="text-xl text-white/80 leading-relaxed font-light">
                What they actually needed wasn't another AI chat interface. They needed a <span class="font-bold text-white bg-linear-to-r from-indigo-300 to-cyan-300 bg-clip-text">workspace</span>—one that understood their intent, maintained their context across sessions, and shipped production-ready artifacts from day one.
              </p>
              
              <div class="h-px bg-linear-to-r from-white/0 via-white/20 to-white/0" />
              
              <p class="text-xl text-white/80 leading-relaxed font-light">
                <span class="font-bold text-white">RunMCP is that workspace.</span> Built by people who've shipped products. For people who care about craft and clarity.
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Philosophy Section -->
      <section class="space-y-12 mb-24 sm:mb-32">
        <div class="space-y-4">
          <h2 class="text-4xl sm:text-5xl font-thin text-white">Our Philosophy</h2>
          <p class="text-lg text-white/50 font-light">Core principles guiding everything we build</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8">
          <!-- Intent over Iteration -->
          <div class="group relative h-full">
            <!-- Glow -->
            <div class="absolute -inset-2 bg-linear-to-br from-indigo-600/20 to-cyan-500/10 rounded-3xl blur-2xl opacity-0 group-hover:opacity-60 transition-opacity duration-500" />
            
            <!-- Card -->
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 sm:p-10 space-y-6 group-hover:border-indigo-400/40 transition-all duration-300 h-full flex flex-col">
              <!-- Icon -->
              <div class="w-14 h-14 rounded-2xl bg-linear-to-br from-indigo-500/30 to-cyan-500/10 flex items-center justify-center text-3xl group-hover:scale-110 group-hover:rotate-6 transition-all duration-300 border border-indigo-400/20">
                🎯
              </div>
              
              <!-- Content -->
              <div class="space-y-3 flex-1">
                <h3 class="text-2xl font-bold text-white group-hover:text-indigo-200 transition-colors">Intent over Iteration</h3>
                <p class="text-white/60 leading-relaxed">
                  Clear vision beats endless tweaking. We help you articulate what you're building and why, then execute with laser precision.
                </p>
              </div>
            </div>
          </div>

          <!-- Structure over Chaos -->
          <div class="group relative h-full">
            <!-- Glow -->
            <div class="absolute -inset-2 bg-linear-to-br from-cyan-600/20 to-emerald-500/10 rounded-3xl blur-2xl opacity-0 group-hover:opacity-60 transition-opacity duration-500" />
            
            <!-- Card -->
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 sm:p-10 space-y-6 group-hover:border-cyan-400/40 transition-all duration-300 h-full flex flex-col">
              <!-- Icon -->
              <div class="w-14 h-14 rounded-2xl bg-linear-to-br from-cyan-500/30 to-emerald-500/10 flex items-center justify-center text-3xl group-hover:scale-110 group-hover:rotate-6 transition-all duration-300 border border-cyan-400/20">
                🏗️
              </div>
              
              <!-- Content -->
              <div class="space-y-3 flex-1">
                <h3 class="text-2xl font-bold text-white group-hover:text-cyan-200 transition-colors">Structure over Chaos</h3>
                <p class="text-white/60 leading-relaxed">
                  No random prompts. Everything flows through defined steps. Every decision is tracked, recorded, and reproducible.
                </p>
              </div>
            </div>
          </div>

          <!-- Ownership over Dependency -->
          <div class="group relative h-full">
            <!-- Glow -->
            <div class="absolute -inset-2 bg-linear-to-br from-purple-600/20 to-pink-500/10 rounded-3xl blur-2xl opacity-0 group-hover:opacity-60 transition-opacity duration-500" />
            
            <!-- Card -->
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 sm:p-10 space-y-6 group-hover:border-purple-400/40 transition-all duration-300 h-full flex flex-col">
              <!-- Icon -->
              <div class="w-14 h-14 rounded-2xl bg-linear-to-br from-purple-500/30 to-pink-500/10 flex items-center justify-center text-3xl group-hover:scale-110 group-hover:rotate-6 transition-all duration-300 border border-purple-400/20">
                🔐
              </div>
              
              <!-- Content -->
              <div class="space-y-3 flex-1">
                <h3 class="text-2xl font-bold text-white group-hover:text-purple-200 transition-colors">Ownership over Dependency</h3>
                <p class="text-white/60 leading-relaxed">
                  Your wallet is your identity. Your builds are your property. We never store keys. We never lock you in.
                </p>
              </div>
            </div>
          </div>

          <!-- Quality over Quantity -->
          <div class="group relative h-full">
            <!-- Glow -->
            <div class="absolute -inset-2 bg-linear-to-br from-emerald-600/20 to-cyan-500/10 rounded-3xl blur-2xl opacity-0 group-hover:opacity-60 transition-opacity duration-500" />
            
            <!-- Card -->
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/10 rounded-3xl p-8 sm:p-10 space-y-6 group-hover:border-emerald-400/40 transition-all duration-300 h-full flex flex-col">
              <!-- Icon -->
              <div class="w-14 h-14 rounded-2xl bg-linear-to-br from-emerald-500/30 to-cyan-500/10 flex items-center justify-center text-3xl group-hover:scale-110 group-hover:rotate-6 transition-all duration-300 border border-emerald-400/20">
                ✨
              </div>
              
              <!-- Content -->
              <div class="space-y-3 flex-1">
                <h3 class="text-2xl font-bold text-white group-hover:text-emerald-200 transition-colors">Quality over Quantity</h3>
                <p class="text-white/60 leading-relaxed">
                  One great build beats ten mediocre ones. We optimize for craft, not churn. Everything shipped is production-ready.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Team Section -->
      <section class="space-y-10 mb-24 sm:mb-32">
        <div class="space-y-4">
          <h2 class="text-4xl sm:text-5xl font-thin text-white">Who We Are</h2>
          <p class="text-lg text-white/50 font-light">The people behind this mission</p>
        </div>

        <div class="group relative">
          <!-- Glow -->
          <div class="absolute -inset-3 bg-linear-to-br from-cyan-600/20 via-purple-600/20 to-indigo-600/20 rounded-4xl blur-3xl opacity-0 group-hover:opacity-50 transition-opacity duration-500" />
          
          <!-- Card -->
          <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-2xl border border-white/10 rounded-4xl p-10 sm:p-14 space-y-8 group-hover:border-white/20 transition-all duration-300">
            <div class="space-y-8">
              <p class="text-lg text-white/80 leading-relaxed font-light">
                We're a diverse team of Web3 builders, AI researchers, and design-obsessed engineers. We've shipped products. We've failed spectacularly. We've learned deeply.
              </p>
              
              <div class="h-px bg-linear-to-r from-white/0 via-white/20 to-white/0" />
              
              <p class="text-lg text-white/80 leading-relaxed font-light">
                We're not theoretical. We build for people like us: people who care about craft, who understand the leverage of good tooling, and who are obsessed with shipping real, useful products that people actually want to use.
              </p>
              
              <div class="h-px bg-linear-to-r from-white/0 via-white/20 to-white/0" />
              
              <p class="text-lg text-white/80 leading-relaxed font-light">
                RunMCP is born from years of frustration with bloated AI tools and scattered workflows. It's built with deep empathy for the builder's journey—the chaos, the iteration, the moments of clarity.
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Values Section -->
      <section class="space-y-12 mb-24 sm:mb-32">
        <div class="space-y-4">
          <h2 class="text-4xl sm:text-5xl font-thin text-white">Our Values</h2>
          <p class="text-lg text-white/50 font-light">What drives our decisions</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          <!-- Ship First -->
          <div class="group relative">
            <div class="absolute -inset-2 bg-linear-to-br from-indigo-600/20 to-cyan-500/10 rounded-2xl blur-xl opacity-0 group-hover:opacity-40 transition-opacity duration-500" />
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 space-y-4 group-hover:border-indigo-400/40 transition-all duration-300">
              <div class="flex items-start gap-4">
                <span class="text-3xl group-hover:scale-125 transition-transform duration-300">🚀</span>
                <div class="space-y-2 pt-1">
                  <p class="font-bold text-white group-hover:text-indigo-200 transition-colors">Ship First</p>
                  <p class="text-sm text-white/60">Theory is nice. Real products matter.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Craft Matters -->
          <div class="group relative">
            <div class="absolute -inset-2 bg-linear-to-br from-cyan-600/20 to-emerald-500/10 rounded-2xl blur-xl opacity-0 group-hover:opacity-40 transition-opacity duration-500" />
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 space-y-4 group-hover:border-cyan-400/40 transition-all duration-300">
              <div class="flex items-start gap-4">
                <span class="text-3xl group-hover:scale-125 transition-transform duration-300">🎨</span>
                <div class="space-y-2 pt-1">
                  <p class="font-bold text-white group-hover:text-cyan-200 transition-colors">Craft Matters</p>
                  <p class="text-sm text-white/60">Details compound. Polish is respect.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Web3 Native -->
          <div class="group relative">
            <div class="absolute -inset-2 bg-linear-to-br from-purple-600/20 to-pink-500/10 rounded-2xl blur-xl opacity-0 group-hover:opacity-40 transition-opacity duration-500" />
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 space-y-4 group-hover:border-purple-400/40 transition-all duration-300">
              <div class="flex items-start gap-4">
                <span class="text-3xl group-hover:scale-125 transition-transform duration-300">🔗</span>
                <div class="space-y-2 pt-1">
                  <p class="font-bold text-white group-hover:text-purple-200 transition-colors">Web3 Native</p>
                  <p class="text-sm text-white/60">Decentralization is the future.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Community First -->
          <div class="group relative">
            <div class="absolute -inset-2 bg-linear-to-br from-emerald-600/20 to-indigo-500/10 rounded-2xl blur-xl opacity-0 group-hover:opacity-40 transition-opacity duration-500" />
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 space-y-4 group-hover:border-emerald-400/40 transition-all duration-300">
              <div class="flex items-start gap-4">
                <span class="text-3xl group-hover:scale-125 transition-transform duration-300">🤝</span>
                <div class="space-y-2 pt-1">
                  <p class="font-bold text-white group-hover:text-emerald-200 transition-colors">Community First</p>
                  <p class="text-sm text-white/60">Builders help builders. We all win.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Speed Matters -->
          <div class="group relative">
            <div class="absolute -inset-2 bg-linear-to-br from-cyan-600/20 to-purple-500/10 rounded-2xl blur-xl opacity-0 group-hover:opacity-40 transition-opacity duration-500" />
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 space-y-4 group-hover:border-cyan-400/40 transition-all duration-300">
              <div class="flex items-start gap-4">
                <span class="text-3xl group-hover:scale-125 transition-transform duration-300">⚡</span>
                <div class="space-y-2 pt-1">
                  <p class="font-bold text-white group-hover:text-cyan-200 transition-colors">Speed Matters</p>
                  <p class="text-sm text-white/60">Fast iteration beats perfect planning.</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Focus -->
          <div class="group relative">
            <div class="absolute -inset-2 bg-linear-to-br from-pink-600/20 to-cyan-500/10 rounded-2xl blur-xl opacity-0 group-hover:opacity-40 transition-opacity duration-500" />
            <div class="relative bg-linear-to-br from-white/10 to-white/5 backdrop-blur-xl border border-white/10 rounded-2xl p-6 space-y-4 group-hover:border-pink-400/40 transition-all duration-300">
              <div class="flex items-start gap-4">
                <span class="text-3xl group-hover:scale-125 transition-transform duration-300">🎯</span>
                <div class="space-y-2 pt-1">
                  <p class="font-bold text-white group-hover:text-pink-200 transition-colors">Focus</p>
                  <p class="text-sm text-white/60">One thing. Done well. Repeated.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- CTA Section -->
      <section class="relative">
        <!-- Glow background -->
        <div class="absolute -inset-4 bg-linear-to-r from-indigo-600/30 via-cyan-600/30 to-emerald-600/30 rounded-4xl blur-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 group" />
        
        <!-- Card -->
        <div class="relative bg-linear-to-br from-indigo-500/20 via-cyan-500/15 to-emerald-500/10 backdrop-blur-2xl border border-white/20 rounded-4xl p-12 sm:p-16 text-center space-y-8 hover:border-white/30 transition-all duration-300">
          <div class="space-y-4">
            <h2 class="text-4xl sm:text-5xl lg:text-6xl font-thin text-white leading-tight">
              Ready to build
              <br />
              <span class="bg-linear-to-r from-indigo-300 to-cyan-300 bg-clip-text text-transparent">
                with intention?
              </span>
            </h2>
            <p class="text-lg text-white/70 font-light max-w-2xl mx-auto">
              Join us in reshaping how Web3 projects are built. From clarity to ship, we've got you covered.
            </p>
          </div>
          
          <NuxtLink
            to="/build"
            class="inline-block group relative px-10 py-5 rounded-xl font-bold text-white text-lg overflow-hidden"
          >
            <!-- Gradient background -->
            <div class="absolute inset-0 bg-linear-to-r from-indigo-600 via-indigo-500 to-cyan-500 opacity-100 group-hover:opacity-90 transition-opacity duration-300" />
            <!-- Shimmer -->
            <div class="absolute inset-0 bg-linear-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-700" />
            <!-- Text -->
            <span class="relative flex items-center gap-3 justify-center">
              Start building
              <svg class="w-6 h-6 group-hover:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </span>
          </NuxtLink>
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

.animate-float {
  animation: float 6s ease-in-out infinite;
}

.animate-float-delayed {
  animation: float-delayed 8s ease-in-out infinite;
}
</style>