<template>
  <main class="relative min-h-screen bg-linear-to-br from-slate-950 via-purple-950 to-slate-950 pt-24 pb-20">
    <!-- Animated background -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <div class="absolute -top-40 -right-40 w-80 h-80 bg-indigo-600/10 rounded-full blur-3xl animate-pulse" />
      <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl animate-pulse delay-1000" />
    </div>

    <div class="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Header -->
      <section class="space-y-8 mb-24">
        <div class="space-y-6">
          <h1 class="text-5xl sm:text-6xl font-bold text-white leading-tight">
            About LLM Studio
          </h1>
          <p class="text-lg sm:text-xl text-white/70 max-w-2xl leading-relaxed">
            We're building tools for people who actually ship. 
            Not another chat wrapper. Not another AI gimmick. 
            A workspace for clarity, structure, and real production.
          </p>
        </div>
      </section>

      <!-- Mission Section -->
      <section class="space-y-8 mb-24">
        <div>
          <h2 class="text-3xl font-bold text-white mb-2">Our Mission</h2>
          <p class="text-white/50 text-sm">Why we built this</p>
        </div>

        <div class="space-y-6">
          <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-8 space-y-4 hover:border-white/30 transition-all duration-300">
            <p class="text-lg text-white/80 leading-relaxed">
              We noticed something: Web3 builders were drowning in tools.
              Too many tabs. Too many frameworks. Too much chaos.
            </p>
            <p class="text-lg text-white/80 leading-relaxed">
              What they needed wasn't another AI chat. They needed a <span class="font-semibold text-white">workspace</span>. 
              One that understood their intent, maintained their context, and shipped production-ready artifacts.
            </p>
            <p class="text-lg text-white/80 leading-relaxed">
              LLM Studio is that workspace. Built by builders. For builders.
            </p>
          </div>
        </div>
      </section>

      <!-- Philosophy Section -->
      <section class="space-y-8 mb-24">
        <div>
          <h2 class="text-3xl font-bold text-white mb-2">Our Philosophy</h2>
          <p class="text-white/50 text-sm">Core principles that guide everything we do</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Intent over Iteration -->
          <div class="group relative">
            <div class="absolute inset-0 bg-linear-to-br from-indigo-600/20 to-cyan-500/20 rounded-xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-6 space-y-3 group-hover:border-white/30 transition-all duration-300">
              <h3 class="text-lg font-semibold text-white">Intent over Iteration</h3>
              <p class="text-white/60 text-sm leading-relaxed">
                Clear vision beats endless tweaking. We guide you to articulate what you're building and why.
                Then we execute with precision.
              </p>
            </div>
          </div>

          <!-- Structure over Chaos -->
          <div class="group relative">
            <div class="absolute inset-0 bg-linear-to-br from-cyan-600/20 to-emerald-500/20 rounded-xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-6 space-y-3 group-hover:border-white/30 transition-all duration-300">
              <h3 class="text-lg font-semibold text-white">Structure over Chaos</h3>
              <p class="text-white/60 text-sm leading-relaxed">
                No more random prompts. Everything flows through defined steps.
                Every decision is tracked. Every output is reproducible.
              </p>
            </div>
          </div>

          <!-- Ownership over Dependency -->
          <div class="group relative">
            <div class="absolute inset-0 bg-linear-to-br from-purple-600/20 to-pink-500/20 rounded-xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-6 space-y-3 group-hover:border-white/30 transition-all duration-300">
              <h3 class="text-lg font-semibold text-white">Ownership over Dependency</h3>
              <p class="text-white/60 text-sm leading-relaxed">
                Your wallet is your identity. Your builds are your property.
                We're not storing your keys. We're not locking you in.
              </p>
            </div>
          </div>

          <!-- Quality over Quantity -->
          <div class="group relative">
            <div class="absolute inset-0 bg-linear-to-br from-emerald-600/20 to-cyan-500/20 rounded-xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            <div class="relative bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-6 space-y-3 group-hover:border-white/30 transition-all duration-300">
              <h3 class="text-lg font-semibold text-white">Quality over Quantity</h3>
              <p class="text-white/60 text-sm leading-relaxed">
                One great build beats ten mediocre ones. We optimize for craft, not churn.
                Everything we ship should be production-ready.
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Team Section -->
      <section class="space-y-8 mb-24">
        <div>
          <h2 class="text-3xl font-bold text-white mb-2">Who We Are</h2>
          <p class="text-white/50 text-sm">The people building this</p>
        </div>

        <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-8 space-y-4">
          <p class="text-white/80 leading-relaxed">
            We're a diverse team of Web3 builders, AI researchers, and design enthusiasts. 
            We've shipped products. We've failed. We've learned.
          </p>
          <p class="text-white/80 leading-relaxed">
            We're not theoretical. We build for people like us: people who care about craft, 
            who understand the power of good tooling, and who want to ship real, useful products.
          </p>
          <p class="text-white/80 leading-relaxed">
            LLM Studio is born from years of frustration with bloated AI tools and scattered workflows. 
            It's built with empathy for the builder's journey.
          </p>
        </div>
      </section>

      <!-- Values Section -->
      <section class="space-y-8 mb-20">
        <div>
          <h2 class="text-3xl font-bold text-white mb-2">Our Values</h2>
          <p class="text-white/50 text-sm">What we stand for</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div class="flex items-start gap-3 p-4 rounded-lg bg-white/5 border border-white/20 hover:border-white/30 transition-all">
            <span class="text-2xl flex-shrink-0">🚀</span>
            <div>
              <p class="font-semibold text-white text-sm">Ship First</p>
              <p class="text-xs text-white/50">Theory is nice. Real products are better.</p>
            </div>
          </div>

          <div class="flex items-start gap-3 p-4 rounded-lg bg-white/5 border border-white/20 hover:border-white/30 transition-all">
            <span class="text-2xl flex-shrink-0">🎨</span>
            <div>
              <p class="font-semibold text-white text-sm">Craft Matters</p>
              <p class="text-xs text-white/50">Details compound. Polish is respect.</p>
            </div>
          </div>

          <div class="flex items-start gap-3 p-4 rounded-lg bg-white/5 border border-white/20 hover:border-white/30 transition-all">
            <span class="text-2xl flex-shrink-0">🔗</span>
            <div>
              <p class="font-semibold text-white text-sm">Web3 Native</p>
              <p class="text-xs text-white/50">Decentralization isn't a feature. It's the future.</p>
            </div>
          </div>

          <div class="flex items-start gap-3 p-4 rounded-lg bg-white/5 border border-white/20 hover:border-white/30 transition-all">
            <span class="text-2xl flex-shrink-0">🤝</span>
            <div>
              <p class="font-semibold text-white text-sm">Community First</p>
              <p class="text-xs text-white/50">Builders help builders. That's how we win.</p>
            </div>
          </div>

          <div class="flex items-start gap-3 p-4 rounded-lg bg-white/5 border border-white/20 hover:border-white/30 transition-all">
            <span class="text-2xl flex-shrink-0">⚡</span>
            <div>
              <p class="font-semibold text-white text-sm">Speed Matters</p>
              <p class="text-xs text-white/50">Fast iteration beats perfect planning.</p>
            </div>
          </div>

          <div class="flex items-start gap-3 p-4 rounded-lg bg-white/5 border border-white/20 hover:border-white/30 transition-all">
            <span class="text-2xl flex-shrink-0">🎯</span>
            <div>
              <p class="font-semibold text-white text-sm">Focus</p>
              <p class="text-xs text-white/50">Do one thing. Do it well. Repeat.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- CTA Section -->
      <section class="text-center space-y-6 p-8 rounded-xl bg-linear-to-r from-indigo-500/10 to-cyan-500/10 border border-indigo-500/20">
        <div class="space-y-4">
          <h2 class="text-2xl sm:text-3xl font-bold text-white">
            Ready to build with intention?
          </h2>
          <p class="text-white/60">
            Join us in reshaping how Web3 projects are built.
          </p>
        </div>
        <NuxtLink
          to="/build"
          class="inline-block group relative px-8 py-4 rounded-xl font-semibold text-white overflow-hidden"
        >
          <div class="absolute inset-0 bg-linear-to-r from-indigo-600 to-cyan-500 opacity-100 group-hover:opacity-90 transition-opacity" />
          <div class="absolute inset-0 bg-linear-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-500" />
          <span class="relative flex items-center gap-2">
            Start building
            <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </span>
        </NuxtLink>
      </section>
    </div>
  </main>
</template>

<style scoped>
/* No custom styles needed - all Tailwind */
</style>