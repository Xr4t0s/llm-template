<template>
  <main class="relative overflow-hidden">

    <!-- HERO -->
    <section class="relative pt-40 pb-48">
      <div class="max-w-6xl mx-auto px-6">
        <div class="max-w-4xl space-y-8">

          <h1 class="text-6xl font-semibold leading-tight animate-fade-up">
            Build products<br />
            <span class="gradient-text">
              with intention.
            </span>
          </h1>

          <p class="text-xl text-(--text-soft) max-w-2xl">
            A Web3-native workspace to orchestrate LLMs,
            manage state, and ship real artifacts —
            from idea to production.
          </p>

          <div class="flex items-center gap-6 pt-4">
            <NuxtLink
              to="/build"
              class="px-7 py-3.5 rounded-xl
                     bg-(--primary)
                     text-white font-medium
                     hover:opacity-90
                     glow transition"
            >
              Start building
            </NuxtLink>

            <NuxtLink
              to="/docs"
              class="text-sm text-(--text-soft)
                     hover:text-white transition"
            >
              Read the docs →
            </NuxtLink>
          </div>

        </div>
      </div>

      <!-- background glow -->
      <div
        class="absolute inset-0 -z-10
               bg-linear-to-br
               from-indigo-600/10
               via-cyan-500/10
               to-emerald-400/10"
      />
    </section>

    <!-- MANIFESTO -->
    <section class="py-32">
      <div class="max-w-6xl mx-auto px-6">
        <div class="max-w-3xl space-y-6">

          <h2 class="text-3xl font-semibold">
            Built for builders, not prompts.
          </h2>

          <p class="text-lg text-(--text-soft) leading-relaxed">
            Most AI tools are optimized for conversation.
            LLM Studio is optimized for construction.
            Persistent context, explicit intent, structured flows.
          </p>

        </div>
      </div>
    </section>

    <!-- FEATURES -->
    <section class="py-32">
      <div class="max-w-6xl mx-auto px-6 grid md:grid-cols-3 gap-10">

        <div class="glass rounded-2xl p-8 space-y-4">
          <h3 class="text-lg font-semibold text-(--accent)">
            Multi-LLM orchestration
          </h3>
          <p class="text-(--text-soft) leading-relaxed">
            Route reasoning, creativity, and execution
            across models without losing state.
          </p>
        </div>

        <div class="glass rounded-2xl p-8 space-y-4">
          <h3 class="text-lg font-semibold text-(--primary)">
            Stateful projects
          </h3>
          <p class="text-(--text-soft) leading-relaxed">
            Every project has memory, structure,
            and a lifecycle — not just a chat history.
          </p>
        </div>

        <div class="glass rounded-2xl p-8 space-y-4">
          <h3 class="text-lg font-semibold text-(--success)">
            Ship-ready outputs
          </h3>
          <p class="text-(--text-soft) leading-relaxed">
            Generate specs, repositories, docs,
            websites, and narratives you can deploy.
          </p>
        </div>

      </div>
    </section>

    <!-- CTA -->
    <section class="pb-40">
      <div class="max-w-6xl mx-auto px-6">
        <div class="glass rounded-3xl px-12 py-16">
          <div class="max-w-2xl space-y-6">
            <h2 class="text-4xl font-semibold">
              Build optimistically.
            </h2>
            <p class="text-(--text-soft) text-lg">
              Web3-native tools for people who actually ship.
            </p>

            <NuxtLink
              to="/build"
              class="inline-block px-7 py-3.5 rounded-xl
                     bg--primary
                     text-white font-medium
                     hover:opacity-90 transition"
            >
              Enter workspace
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>

  </main>
</template>
