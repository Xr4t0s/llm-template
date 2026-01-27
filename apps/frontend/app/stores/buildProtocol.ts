import { defineStore } from 'pinia'
import type { ProjectType, ProjectGoal, BuildOutputs } from '~/types/build'

export const useBuildProtocol = defineStore('buildProtocol', {
  state: () => ({
	step: 1,

	lore: '',
	hasMascot: true,
	tone: 'Meme', // ✅ FIX
	taglineStyle: 'Short & punchy',

	projectType: '' as ProjectType,
	goal: '' as ProjectGoal,

	visualVibe: 'clean', // ✅ OK (lowercase)
	palettes: [] as string[],

	outputs: {
		logo: true,
		banner: true,
		pfp: true,
		announcements: true,
		memes: false,
		stickers: false,
		documentation: true,
		onepager: false,
		roadmap: true,
		faq: true,
	},
	}),


  getters: {
    canGoNext(state) {
      if (state.step === 1) return state.lore.length >= 20
      if (state.step === 2) return !!state.projectType && !!state.goal
      if (state.step === 3) return state.palettes.length >= 1
      if (state.step === 4) return Object.values(state.outputs).some(Boolean)
      return true
    },
  },

  actions: {
    next() {
      if (this.canGoNext && this.step < 5) this.step++
    },
    prev() {
      if (this.step > 1) this.step--
    },
    goTo(step: number) {
      this.step = step
    },
    reset() {
      this.$reset()
    },
  },
})
