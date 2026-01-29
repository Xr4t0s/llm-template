<template>
  <div class="build-shell">
    <div class="build-panel">
      <div class="build-content build-section">

        <!-- =========================
             LOADING
        ========================== -->
        <template v-if="loading">
          <div class="flex flex-col items-center gap-4 py-20">
            <div class="animate-spin">
              <svg class="w-10 h-10 text-white/70" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                <path
                  class="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.3 0 0 5.3 0 12h4z"
                />
              </svg>
            </div>
            <p class="build-subtitle">Récupération du statut du build…</p>
          </div>
        </template>

        <!-- =========================
             RUNNING
        ========================== -->
        <template v-else-if="profile?.running">
          <!-- Header -->
          <div class="build-header">
            <div class="build-header-top">
              <h1 class="build-title">Build en cours</h1>
              <span class="build-pill">RUNNING</span>
            </div>

            <div class="build-progress">
              <div
                class="build-progress-bar"
                :style="{ width: `${progress}%` }"
              />
            </div>

            <p class="build-helper">
              Étape {{ profile.step }} / {{ totalSteps }} · {{ getCurrentStepName() }}
            </p>
          </div>

          <!-- Status card -->
          <div class="build-card build-card-active space-y-3">
            <div class="flex justify-between">
              <span class="build-label">Sous-étape</span>
              <span>{{ profile.substep }}</span>
            </div>

            <div class="flex justify-between">
              <span class="build-label">Adresse</span>
              <span class="font-mono text-xs">
                {{ shortAddress }}
              </span>
            </div>
          </div>

          <p class="build-subtitle">
            Les assets sont en cours de génération. Cette page se met à jour automatiquement.
          </p>
        </template>

        <!-- =========================
             IDLE / DONE
        ========================== -->
        <template v-else-if="profile">
          <div class="build-header">
            <h1 class="build-title">Build prêt</h1>
            <p class="build-subtitle">
              Aucun build actif pour le moment.
            </p>
          </div>

          <div class="build-card space-y-2">
            <div class="flex justify-between">
              <span class="build-label">Builds complétés</span>
              <span>{{ profile.builds }}</span>
            </div>

            <div class="flex justify-between">
              <span class="build-label">Dernière étape</span>
              <span>{{ profile.step }}</span>
            </div>
          </div>

          <div class="build-footer">
            <button
              class="build-btn build-btn-primary"
              @click="refreshStatus"
            >
              Actualiser
            </button>

            <span class="build-footer-hint">
              Les nouveaux builds apparaîtront ici.
            </span>
          </div>
        </template>

        <!-- =========================
             ERROR
        ========================== -->
        <template v-else-if="error">
          <div class="flex flex-col items-center gap-4 py-16">
            <h2 class="text-lg font-semibold text-red-400">Erreur</h2>
            <p class="build-subtitle">{{ error }}</p>

            <button
              class="build-btn build-btn-secondary"
              @click="fetchProfile"
            >
              Réessayer
            </button>
          </div>
        </template>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useAuthStore } from '@/stores/auth'

const profile = ref(null)
const loading = ref(true)
const error = ref(null)
const pollInterval = ref(null)

const totalSteps = 10

const progress = computed(() => {
  if (!profile.value) return 0
  return Math.min(
    100,
    (profile.value.step / totalSteps) * 80 +
    (profile.value.substep / 10) * 20
  )
})

const shortAddress = computed(() => {
  if (!profile.value?.address) return ''
  return `${profile.value.address.slice(0, 6)}…${profile.value.address.slice(-6)}`
})

const getCurrentStepName = () => {
  const map = {
    0: 'Initialisation',
    1: 'Compilation',
    2: 'Bundling',
    3: 'Optimisation',
    4: 'Génération',
    5: 'Validation',
    6: 'Finalisation',
    7: 'Déploiement',
  }
  return map[profile.value?.step] ?? 'En cours'
}

const fetchProfile = async () => {
  try {
    loading.value = true
    error.value = null

    const { token } = useAuthStore()
    if (!token) throw new Error('Non authentifié')

    const res = await fetch('/api/v1/profile', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })

    const data = await res.json()
    profile.value = data.profile
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

const startPolling = () => {
  pollInterval.value = setInterval(() => {
    if (profile.value?.running) fetchProfile()
  }, 2000)
}

const stopPolling = () => {
  clearInterval(pollInterval.value)
}

const refreshStatus = fetchProfile

onMounted(() => {
  fetchProfile()
  startPolling()
})

onUnmounted(stopPolling)
</script>
