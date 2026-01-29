<template>
  <div class="w-full max-w-2xl mx-auto py-20">
    <!-- Success animation -->
    <div class="space-y-8 text-center">
      <!-- Celebration emoji -->
      <div class="text-7xl animate-bounce">
        🎉
      </div>

      <!-- Main message -->
      <div class="space-y-4">
        <h1 class="text-4xl sm:text-5xl font-bold text-white">
          Build launched!
        </h1>
        <p class="text-lg text-white/60 max-w-xl mx-auto">
          Your project is now being processed. Assets are being generated and will appear shortly.
        </p>
      </div>

      <!-- Progress card -->
      <div class="bg-white/5 backdrop-blur-xl border border-white/20 rounded-xl p-8 space-y-6 max-w-md mx-auto">
        <!-- Status indicator -->
        <div class="flex items-center gap-3 justify-center">
          <div class="w-3 h-3 rounded-full bg-emerald-400 animate-pulse" />
          <span class="text-white/70 font-medium">
            {{ isRunning ? 'Build in progress' : 'Build complete' }}
          </span>
        </div>

        <!-- Info grid -->
        <div class="grid grid-cols-2 gap-4">
          <div class="text-center p-3 rounded-lg bg-white/10 border border-white/10">
            <p class="text-xs text-white/50 mb-2">Project Type</p>
            <p class="font-semibold text-white text-sm">
              {{ prettyProjectType }}
            </p>
          </div>
          <div class="text-center p-3 rounded-lg bg-white/10 border border-white/10">
            <p class="text-xs text-white/50 mb-2">Outputs</p>
            <p class="font-semibold text-white text-sm">
              {{ selectedCount }}
            </p>
          </div>
        </div>

        <!-- Progress bar -->
        <div class="space-y-2">
          <div class="flex items-center justify-between text-xs">
            <span class="text-white/60">Generation progress</span>
            <span class="text-white font-mono font-semibold">{{ progress }}%</span>
          </div>
          <div class="h-2 bg-white/10 rounded-full overflow-hidden border border-white/20">
            <div
              class="h-full bg-linear-to-r from-emerald-500 to-cyan-400 rounded-full transition-all duration-500 ease-out"
              :style="{ width: `${progress}%` }"
            />
          </div>
        </div>
      </div>

      <!-- Timeline steps -->
      <div class="space-y-3 max-w-md mx-auto pt-8">
        <div
          v-for="(step, idx) in steps"
          :key="idx"
          class="flex items-start gap-3"
          :style="{ animationDelay: `${idx * 0.1}s` }"
        >
          <div
            class="shrink-0 w-8 h-8 rounded-full flex items-center justify-center text-sm font-semibold transition-all duration-300"
            :class="[
              idx < currentStep
                ? 'bg-emerald-500 text-white'
                : idx === currentStep
                  ? 'bg-linear-to-r from-indigo-600 to-cyan-500 text-white animate-pulse'
                  : 'bg-white/20 text-white/60'
            ]"
          >
            {{ idx < currentStep ? '✓' : idx + 1 }}
          </div>
          <div class="flex-1 pt-1">
            <p
              class="text-sm font-medium transition-colors duration-300"
              :class="idx <= currentStep ? 'text-white' : 'text-white/40'"
            >
              {{ step }}
            </p>
          </div>
        </div>
      </div>

      <!-- Action buttons -->
      <div class="flex flex-col sm:flex-row gap-4 justify-center pt-12">
        <NuxtLink
          to="/build"
          class="group relative px-8 py-3 rounded-xl font-semibold text-white overflow-hidden"
        >
          <!-- Border -->
          <div class="absolute inset-0 border border-white/20 rounded-xl group-hover:border-white/40 transition-colors" />
          <div class="absolute inset-0 bg-white/5 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity" />
          <!-- Text -->
          <span class="relative">Start new build</span>
        </NuxtLink>

        <button
          @click="openResults"
          :disabled="isRunning"
          class="group relative px-8 py-3 rounded-xl font-semibold text-white overflow-hidden disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <!-- Gradient background -->
          <div class="absolute inset-0 bg-linear-to-r from-indigo-600 to-cyan-500 opacity-100 group-hover:opacity-90 transition-opacity rounded-xl" />
          <!-- Shimmer effect -->
          <div class="absolute inset-0 bg-linear-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-500 rounded-xl" />
          <!-- Text -->
          <span class="relative flex items-center gap-2">
            View results
            <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
            </svg>
          </span>
        </button>
      </div>

      <!-- Tips -->
      <div class="text-center text-white/50 text-xs pt-8 border-t border-white/10 space-y-2">
        <p>💡 You can edit and regenerate outputs anytime</p>
        <p class="font-mono text-white/40">{{ currentTime }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref, onMounted, onUnmounted } from 'vue'
import { useBuildProtocol } from '~/stores/buildProtocol'

const store = useBuildProtocol()
const progress = ref(0)
const currentStep = ref(0)
const currentTime = ref('')
const isRunning = ref(true)
const loading = ref(true)

const steps = [
  'Preparing assets',
  'Generating visuals',
  'Creating documentation',
  'Optimizing outputs',
  'Finalizing build',
]

const prettyProjectType = computed(() => {
  const map: Record<string, string> = {
    meme: 'Meme project',
    tool: 'Tool / App',
    defi: 'DeFi',
  }
  return map[store.projectType] || '—'
})

const selectedCount = computed(() =>
  Object.values(store.outputs).filter(Boolean).length
)

// Calcul du progress en fonction de step et substep
function calculateProgress(step: number, substep: number): number {
  const stepProgress = step * 20 // 0, 20, 40, 60, 80
  const substepProgress = (substep - 1) * 4 // 0 à 16 par étape
  return Math.min(stepProgress + substepProgress, 100)
}

// Récupère les données du profil depuis l'API
async function fetchProfileData() {
  try {
	const { token } = useAuthStore()
    const response = await fetch('/api/v1/profile',
		{
			headers: {
				"Authorization": `Bearer ${token}`
			}
		}
	)
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`)
    }
    const data = await response.json()
    
    if (data.profile) {
      const { step, substep, running } = data.profile
      currentStep.value = step
      isRunning.value = running
      progress.value = calculateProgress(step, substep)
    }
  } catch (error) {
    console.error('Failed to fetch profile data:', error)
  }
}

function openResults() {
  if (!isRunning.value) {
    // Naviguer vers les résultats
    // navigateTo(`/build/results/${store.id}`)
  }
}

onMounted(() => {
  // Mise à jour de l'heure
  const updateTime = () => {
    const now = new Date()
    currentTime.value = now.toLocaleTimeString()
  }
  updateTime()
  const timeInterval = setInterval(updateTime, 1000)

  // Récupère les données initiales
  fetchProfileData()
  loading.value = false

  // Polling pour les updates du progress
  const pollInterval = setInterval(() => {
    fetchProfileData()
  }, 3000) // Récupère les données toutes les secondes

  onUnmounted(() => {
    clearInterval(pollInterval)
    clearInterval(timeInterval)
  })
})
</script>