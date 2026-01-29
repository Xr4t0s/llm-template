<template>
  <div class="space-y-8 w-full max-w-3xl">
    <!-- Header -->
    <div class="space-y-3">
      <h2 class="text-3xl font-bold text-white">
        Identity & Lore
      </h2>
      <p class="text-white/60 leading-relaxed">
        Define the origin story of your project. This narrative will guide
        the visual direction, tone, and documentation.
      </p>
    </div>

    <!-- Lore textarea section -->
    <div class="space-y-4">
      <label class="block">
        <span class="text-sm font-semibold text-white mb-2 block">
          Project lore
        </span>
        <span class="text-xs text-white/50 mb-3 block">
          Write it like an origin story, not a pitch deck
        </span>

        <div class="relative">
          <!-- Textarea wrapper with glow -->
          <div class="absolute inset-0 bg-linear-to-r from-indigo-600/10 to-cyan-500/10 rounded-xl blur opacity-0 focus-within:opacity-100 transition-opacity duration-300" />

          <textarea
            v-model="store.lore"
            rows="8"
            placeholder="Describe the idea, the intention, the universe behind your project... What problem does it solve? What's the vibe? Why does it matter?"
            class="relative w-full px-4 py-3 rounded-xl bg-white/5 backdrop-blur-xl border border-white/20 text-white placeholder:text-white/30 focus:border-indigo-500/50 focus:outline-none focus:ring-1 focus:ring-indigo-500/30 transition-all duration-300 resize-none font-mono text-sm leading-relaxed"
          />

          <!-- Character counter -->
          <div class="absolute bottom-3 right-4 text-xs text-white/40 font-mono">
            {{ store.lore.length }} / 800
          </div>
        </div>
      </label>

      <!-- Helper text -->
      <p class="text-xs text-cyan-400/70 flex items-center gap-2">
        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
        </svg>
        The better your lore, the better the output. Be specific and authentic.
      </p>
    </div>

    <!-- Options grid -->
    <div class="space-y-6">
      <!-- Mascot toggle -->
      <div class="group relative">
        <div class="absolute inset-0 bg-linear-to-r from-purple-600/10 to-pink-600/10 rounded-xl blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

        <div class="relative bg-white/5 backdrop-blur-xl border border-white/10 rounded-xl p-5 cursor-pointer group-hover:border-white/20 transition-all duration-300"
		  @click="store.hasMascot = !store.hasMascot"
		>
          <div class="flex items-start gap-4">
            <!-- Toggle switch -->
			<div class="flex-1">
			  <h3 class="text-sm font-semibold text-white mb-1">
				Mascot or main character
			  </h3>
			  <p class="text-xs text-white/60">
				A character can be reused across logos, memes, stickers, and social visuals.
			  </p>
			</div>
            <div class="text-xs font-semibold px-3 py-1 rounded-full flex-shrink-0" :class="store.hasMascot ? 'bg-emerald-500/20 text-emerald-300' : 'bg-white/10 text-white/50'">
              {{ store.hasMascot ? '✓ Yes' : 'No' }}
            </div>

            <!-- Content -->

            <!-- Status badge -->
            
          </div>
        </div>
      </div>

      <!-- Tone selection -->
      <div class="space-y-4">
        <div>
          <label class="text-sm font-semibold text-white block mb-2">
            Narrative tone
          </label>
          <p class="text-xs text-white/50">
            Overall attitude and personality of your project
          </p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
          <button
            v-for="tone in tones"
            :key="tone"
            @click="store.tone = tone"
            class="relative group px-4 py-3 rounded-lg font-medium text-sm transition-all duration-300"
            :class="[
              store.tone === tone
                ? 'bg-linear-to-r from-indigo-600 to-cyan-500 text-white shadow-lg shadow-indigo-500/30'
                : 'bg-white/5 border border-white/20 text-white/70 hover:bg-white/10 hover:border-white/30'
            ]"
          >
            {{ tone }}
          </button>
        </div>
      </div>
    </div>

    <!-- Validation hint -->
    <div v-if="!store.lore" class="flex items-center gap-3 px-4 py-3 rounded-lg bg-orange-500/10 border border-orange-500/20">
      <svg class="w-5 h-5 text-orange-400 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
      </svg>
      <p class="text-sm text-orange-300">
        Fill in the lore to continue
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useBuildProtocol } from '~/stores/buildProtocol'

const store = useBuildProtocol()

const tones = [
  'Serious',
  'Playful',
  'Meme',
  'Dark',
  'Experimental',
] as const
</script>