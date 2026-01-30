import { defineStore } from 'pinia'
import type { ProjectType, ProjectGoal, BuildOutputs } from '~/types/build'

export const useBuildProtocol = defineStore('buildProtocol', {
  state: () => ({
	step: 1,
	buildDone: false,

	lore: '',
	hasMascot: true,
	tone: '',
	taglineStyle: 'Short & punchy',

	projectType: '' as ProjectType,
	goal: '' as ProjectGoal,

	visualVibe: 'clean', // ✅ OK (lowercase)
	palettes: [] as string[],

	outputs: {
		documentation: {
			markdown: false,
			tweets: false
		},
		visuals: {
			logo: false,
			banners: false,
			x_assets: false
		},
		website: {
			landingPage: false
		}
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

