<script setup lang="ts">
import { computed } from 'vue'

interface Build {
  id: number
  ownerAddress: string
  createdAt: string
}

interface Props {
  build: Build
  index: number
  hoveredId: number | null
}

defineProps<Props>()
defineEmits<{
  click: []
  mouseenter: []
  mouseleave: []
}>()

const truncateAddress = (address: string) => {
  return `${address.slice(0, 6)}...${address.slice(-4)}`
}

const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  const now = new Date()
  const diff = now.getTime() - date.getTime()
  const days = Math.floor(diff / (1000 * 60 * 60 * 24))
  const hours = Math.floor(diff / (1000 * 60 * 60))
  const minutes = Math.floor(diff / (1000 * 60))
  
  if (minutes < 1) return 'Just now'
  if (minutes < 60) return `${minutes}m ago`
  if (hours < 24) return `${hours}h ago`
  if (days === 0) return 'Today'
  if (days === 1) return 'Yesterday'
  if (days < 7) return `${days}d ago`
  
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  })
}
</script>

<template>
  <div
    class="group cursor-pointer relative"
    @click="$emit('click')"
    @mouseenter="$emit('mouseenter')"
    @mouseleave="$emit('mouseleave')"
    :style="{ 
      'animation-delay': `${index * 80}ms`,
      'transition': 'all 0.4s cubic-bezier(0.23, 1, 0.320, 1)'
    }"
  >
    <!-- Card Container - Compact -->
    <div class="relative overflow-hidden rounded-lg border border-white/10 bg-gradient-to-br from-white/8 via-white/3 to-white/0 p-4 backdrop-blur-md transition-all duration-500 group-hover:border-indigo-500/50 group-hover:from-white/15 group-hover:via-indigo-500/10">
      
      <!-- Animated Background Blur -->
      <div class="absolute inset-0 bg-gradient-to-br from-indigo-500/0 via-purple-500/0 to-cyan-500/0 group-hover:from-indigo-500/10 group-hover:via-purple-500/5 group-hover:to-cyan-500/10 transition-all duration-500" />
      
      <!-- Top Glow Effect -->
      <div class="absolute -top-16 -right-16 w-40 h-40 bg-gradient-to-br from-indigo-500 to-cyan-500 opacity-0 group-hover:opacity-15 blur-2xl transition-all duration-500 rounded-full" />
      
      <!-- Content -->
      <div class="relative z-10 space-y-3">
        
        <!-- Header with Icon - Compact -->
        <div class="flex items-start justify-between gap-2">
          <div class="flex items-center gap-2 flex-1 min-w-0">
            <div class="w-9 h-9 rounded-lg bg-gradient-to-br from-indigo-600 to-cyan-500 flex items-center justify-center group-hover:scale-105 transition-transform duration-300 flex-shrink-0">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <div class="min-w-0">
              <h3 class="text-base font-bold text-white group-hover:text-transparent group-hover:bg-clip-text group-hover:bg-gradient-to-r group-hover:from-indigo-400 group-hover:to-cyan-400 transition-all duration-300 truncate leading-tight">
                Build #{{ build.id }}
              </h3>
              <div class="flex items-center gap-1.5 mt-0.5">
                <span class="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse" />
                <span class="text-xs text-green-400">Active</span>
              </div>
            </div>
          </div>
          <svg class="w-5 h-5 text-white/30 group-hover:text-indigo-400 group-hover:translate-x-0.5 transition-all duration-300 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
          </svg>
        </div>

        <!-- Address - Compact -->
        <div class="space-y-1 py-2.5 border-y border-white/10">
          <p class="text-xs text-white/40 uppercase tracking-wider font-semibold">Address</p>
          <p class="text-xs font-mono text-white/70 hover:text-white transition-colors group-hover:text-indigo-300 truncate" :title="build.ownerAddress">
            {{ truncateAddress(build.ownerAddress) }}
          </p>
        </div>

        <!-- Footer Stats - Compact -->
        <div class="flex items-center justify-between pt-1">
          <div class="space-y-0.5">
            <p class="text-xs text-white/40 uppercase tracking-wider">Created</p>
            <p class="text-xs text-white/70 group-hover:text-indigo-300 transition-colors leading-tight">
              {{ formatDate(build.createdAt) }}
            </p>
          </div>
          <div class="w-7 h-7 rounded-lg bg-gradient-to-br from-indigo-500/20 to-cyan-500/20 group-hover:from-indigo-500/40 group-hover:to-cyan-500/40 flex items-center justify-center transition-all duration-300 flex-shrink-0">
            <span class="text-xs font-bold text-indigo-300">→</span>
          </div>
        </div>
      </div>

      <!-- Bottom Border Glow -->
      <div class="absolute bottom-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-indigo-500/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
      
      <!-- Hover Border Animation -->
      <div class="absolute inset-0 rounded-lg border border-transparent bg-gradient-to-r from-indigo-500/20 via-purple-500/0 to-cyan-500/20 opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none" />
    </div>

    <!-- Shadow Glow -->
    <div class="absolute -inset-1.5 bg-gradient-to-r from-indigo-600/0 via-purple-600/0 to-cyan-500/0 group-hover:from-indigo-600/15 group-hover:via-purple-600/5 group-hover:to-cyan-500/15 rounded-lg blur-xl opacity-0 group-hover:opacity-100 transition-all duration-500 -z-10" />
  </div>
</template>

<style scoped>
</style>