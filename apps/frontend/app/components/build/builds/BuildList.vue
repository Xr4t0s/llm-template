<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useAuthStore } from '~/stores/auth'
import BuildCard from './ui/BuildCard.vue'
import BuildDetailModal from './ui/BuildModal.vue'

interface Build {
  id: number
  ownerAddress: string
  createdAt: string
}

defineEmits<{
  back: []
}>()

const authStore = useAuthStore()
const builds = ref<Build[]>([])
const loading = ref(true)
const error = ref<string | null>(null)
const hoveredId = ref<number | null>(null)
const refreshing = ref(false)
const selectedBuild = ref<Build | null>(null)
const isModalOpen = ref(false)

const hasBuilds = computed(() => builds.value.length > 0)
const isEmpty = computed(() => !loading.value && !error.value && builds.value.length === 0)

const fetchBuilds = async () => {
  try {
    refreshing.value = true
    loading.value = true
    error.value = null
    
    const response = await fetch('/api/v1/builds', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${authStore.token}`,
        'Content-Type': 'application/json',
      },
    })

    if (!response.ok) {
      throw new Error(response.status === 401 ? 'Unauthorized' : 'Failed to fetch builds')
    }

    const data = await response.json()
    builds.value = data.builds || []
    
    await new Promise(resolve => setTimeout(resolve, 400))
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'An error occurred'
    console.error('Error fetching builds:', err)
  } finally {
    loading.value = false
    refreshing.value = false
  }
}

const openBuildDetail = (build: Build) => {
  selectedBuild.value = build
  isModalOpen.value = true
}

const closeBuildDetail = () => {
  isModalOpen.value = false
  setTimeout(() => {
    selectedBuild.value = null
  }, 300)
}

onMounted(() => {
  fetchBuilds()
})
</script>

<template>
  <div class="w-full space-y-8">
    <!-- Header -->
    <div class="space-y-4">
      <div class="flex items-center justify-between">
        <div>
          <h1 class="text-5xl font-thin text-white">Your Builds</h1>
          <p class="text-white/60 mt-2">
            {{ hasBuilds ? `${builds.length} build${builds.length !== 1 ? 's' : ''} available` : 'No builds yet' }}
          </p>
        </div>
        <button
          v-if="hasBuilds && !loading"
          @click="fetchBuilds"
          :disabled="refreshing"
          class="p-2.5 rounded-lg border border-white/20 hover:border-white/40 bg-white/5 hover:bg-white/10 text-white/60 hover:text-white transition-all disabled:opacity-50"
        >
          <svg 
            :class="{ 'animate-spin': refreshing }" 
            class="w-5 h-5" 
            fill="none" 
            stroke="currentColor" 
            viewBox="0 0 24 24"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
        </button>
      </div>

      <!-- Stats -->
      <div v-if="hasBuilds" class="flex gap-8 pt-2 border-t border-white/10">
        <div>
          <p class="text-3xl font-bold text-white">{{ builds.length }}</p>
          <p class="text-sm text-white/50 mt-1">Total</p>
        </div>
        <div>
          <p class="text-3xl font-bold text-indigo-400">{{ builds[0]?.id }}</p>
          <p class="text-sm text-white/50 mt-1">Latest</p>
        </div>
      </div>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="space-y-4">
      <div v-for="i in 4" :key="i" class="h-32 rounded-lg bg-white/5 animate-pulse border border-white/10" />
      <div class="flex flex-col items-center justify-center py-12 space-y-3">
        <div class="w-12 h-12 rounded-full border-2 border-white/20 border-t-indigo-500 animate-spin" />
        <p class="text-white/60">Loading builds...</p>
      </div>
    </div>

    <!-- Error -->
    <div v-else-if="error" class="p-8 rounded-lg border border-red-500/30 bg-red-500/5 space-y-4">
      <div class="flex items-start gap-4">
        <div class="text-3xl">⚠️</div>
        <div>
          <p class="font-semibold text-white">Error loading builds</p>
          <p class="text-white/60 text-sm mt-1">{{ error }}</p>
        </div>
      </div>
      <div class="flex gap-2 pt-2">
        <button
          @click="fetchBuilds"
          class="px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-medium transition-colors"
        >
          Retry
        </button>
        <button
          @click="$emit('back')"
          class="px-4 py-2 rounded-lg border border-white/20 hover:border-white/40 text-white text-sm font-medium transition-colors"
        >
          Back
        </button>
      </div>
    </div>

    <!-- Empty -->
    <div v-else-if="isEmpty" class="text-center py-16 space-y-4">
      <div class="text-6xl">📦</div>
      <div>
        <p class="text-2xl font-bold text-white">No builds yet</p>
        <p class="text-white/60 mt-2">Create your first build to see it here</p>
      </div>
      <button
        @click="$emit('back')"
        class="px-6 py-2.5 rounded-lg bg-linear-to-r from-indigo-600 to-cyan-600 hover:opacity-90 text-white font-medium transition-opacity mt-4"
      >
        Create a build
      </button>
    </div>

    <!-- Grid -->
    <div v-else class="grid grid-cols-1 sm:grid-cols-1">
      <Transition name="fade-scale" appear>
		<div>
        <template v-for="(build, index) in builds" :key="build.id">
          <div
            :style="{ 'animation-delay': `${index * 50}ms` }"
            class="animate-in p-4"
          >
            <BuildCard
              :build="build"
              :index="index"
              :hoveredId="hoveredId"
              @click="openBuildDetail(build)"
              @mouseenter="hoveredId = build.id"
              @mouseleave="hoveredId = null"
            />
          </div>
        </template>
		</div>
      </Transition>
    </div>

    <!-- Modal -->
    <BuildDetailModal
      :isOpen="isModalOpen"
      :build="selectedBuild"
      @close="closeBuildDetail"
    />
  </div>
</template>

<style scoped>
@keyframes fadeScale {
  from {
    opacity: 0;
    transform: scale(0.9) translateY(10px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

.fade-scale-enter-active {
  transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
}

.fade-scale-enter-from {
  opacity: 0;
  transform: scale(0.9) translateY(10px);
}

.animate-in {
  animation: fadeScale 0.4s cubic-bezier(0.23, 1, 0.320, 1) forwards;
  opacity: 0;
}
</style>