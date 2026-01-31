<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '~/stores/auth'

interface Build {
  id: number
  ownerAddress: string
  createdAt: string
}

interface Props {
  isOpen: boolean
  build: Build | null
}

const { isOpen, build } = defineProps<Props>()
const emit = defineEmits<{
  close: []
  deleted: []
}>()

const authStore = useAuthStore()
const isAnimating = ref(false)
const isDownloading = ref(false)
const isDeleting = ref(false)
const showDeleteConfirm = ref(false)

const copyToClipboard = async (text: string) => {
  try {
    if (typeof navigator !== 'undefined' && navigator.clipboard) {
      await navigator.clipboard.writeText(text)
    } else {
      const textarea = document.createElement('textarea')
      textarea.value = text
      document.body.appendChild(textarea)
      textarea.select()
      document.execCommand('copy')
      document.body.removeChild(textarea)
    }
  } catch (err) {
    console.error('Failed to copy:', err)
  }
}

const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
}

const handleClose = () => {
  showDeleteConfirm.value = false
  isAnimating.value = true
  setTimeout(() => {
    isAnimating.value = false
    emit('close')
  }, 300)
}

const downloadBuild = async () => {
  if (!build) return
  
  try {
    isDownloading.value = true
    
    const response = await fetch(`/api/v1/builds/${build.id}/download`, {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${authStore.token}`,
      },
    })

    if (!response.ok) {
      throw new Error('Failed to download build')
    }

    const blob = await response.blob()
    const url = window.URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = `build-${build.id}.zip`
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
    window.URL.revokeObjectURL(url)
  } catch (err) {
    console.error('Error downloading build:', err)
  } finally {
    isDownloading.value = false
  }
}

const deleteBuild = async () => {
  if (!build) return
  
  try {
    isDeleting.value = true
    
    const response = await fetch(`/api/v1/builds/${build.id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${authStore.token}`,
        'Content-Type': 'application/json',
      },
    })

    if (!response.ok) {
      throw new Error('Failed to delete build')
    }

    emit('deleted')
    handleClose()
  } catch (err) {
    console.error('Error deleting build:', err)
  } finally {
    isDeleting.value = false
    showDeleteConfirm.value = false
  }
}
</script>

<template>
  <!-- Backdrop -->
  <Transition name="modal-backdrop">
    <div
      v-if="isOpen"
      @click="handleClose"
      class="fixed inset-0 bg-black/80 backdrop-blur-sm z-40"
    />
  </Transition>

  <!-- Modal -->
  <Transition name="modal-expand" mode="out-in">
    <div
      v-if="isOpen && build"
      :key="`build-${build.id}`"
      class="fixed inset-0 z-50 flex items-center justify-center p-4 pointer-events-none"
    >
      <div
        @click.stop
        class="relative w-full max-w-2xl bg-linear-to-br from-white/10 via-white/5 to-white/0 backdrop-blur-xl rounded-2xl border border-white/20 overflow-hidden pointer-events-auto"
      >
        <!-- Background -->
        <div class="absolute inset-0 bg-linear-to-br from-indigo-600/20 via-purple-600/10 to-cyan-500/20 opacity-40" />
        <div class="absolute top-0 right-0 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl" />
        <div class="absolute bottom-0 left-0 w-96 h-96 bg-indigo-600/10 rounded-full blur-3xl" />

        <!-- Content -->
        <div class="relative z-10 p-8 md:p-12 space-y-8">
          <!-- Header -->
          <div class="space-y-4">
            <div class="flex items-center gap-4">
              <div class="w-20 h-20 rounded-2xl bg-linear-to-br from-indigo-600 to-cyan-500 flex items-center justify-center shrink-0">
                <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div>
                <h2 class="text-4xl font-bold text-white">Build #{{ build.id }}</h2>
                <div class="flex items-center gap-3 mt-2">
                  <span class="w-3 h-3 rounded-full bg-green-500" />
                  <span class="text-green-400 font-medium text-sm">Active</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Info Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Address -->
            <div class="p-6 rounded-lg bg-white/5 border border-white/10 space-y-3">
              <p class="text-xs text-white/50 uppercase tracking-widest">Owner Address</p>
              <p class="font-mono text-sm text-white break-all">{{ build.ownerAddress }}</p>
              <button
                @click="copyToClipboard(build.ownerAddress)"
                class="text-xs text-white/40 hover:text-white/70 transition-colors flex items-center gap-2"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
                Copy
              </button>
            </div>

            <!-- Date -->
            <div class="p-6 rounded-lg bg-white/5 border border-white/10 space-y-3">
              <p class="text-xs text-white/50 uppercase tracking-widest">Created</p>
              <p class="text-sm text-white">{{ formatDate(build.createdAt) }}</p>
              <p class="text-xs text-white/40">ID: #{{ build.id }}</p>
            </div>
          </div>

          <!-- Actions -->
          <div class="flex flex-col sm:flex-row gap-3 pt-4 border-t border-white/10">
            <button
              @click="downloadBuild"
              :disabled="isDownloading || isDeleting"
              class="flex-1 px-6 py-3 rounded-lg font-semibold text-white bg-linear-to-r from-indigo-600 to-cyan-600 hover:opacity-90 disabled:opacity-50 transition-all flex items-center justify-center gap-2"
            >
              <svg v-if="!isDownloading" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
              <svg v-else class="w-5 h-5 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              {{ isDownloading ? 'Downloading...' : 'Download' }}
            </button>
            <button
              @click="showDeleteConfirm = true"
              :disabled="isDeleting"
              class="px-6 py-3 rounded-lg font-semibold border border-red-500/30 hover:border-red-500/60 text-red-400 hover:text-red-300 hover:bg-red-500/10 transition-all flex items-center justify-center gap-2 disabled:opacity-50"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
              Delete
            </button>
            <button
              @click="handleClose"
              class="px-6 py-3 rounded-lg font-semibold border border-white/20 hover:border-white/40 text-white hover:bg-white/5 transition-all"
            >
              Close
            </button>
          </div>

          <!-- Stats -->
          <div class="grid grid-cols-3 gap-4">
            <div class="text-center p-4 rounded-lg bg-white/5 border border-white/10">
              <p class="text-2xl font-bold text-indigo-400">1</p>
              <p class="text-xs text-white/60 mt-1">Version</p>
            </div>
            <div class="text-center p-4 rounded-lg bg-white/5 border border-white/10">
              <p class="text-2xl font-bold text-cyan-400">100%</p>
              <p class="text-xs text-white/60 mt-1">Ready</p>
            </div>
            <div class="text-center p-4 rounded-lg bg-white/5 border border-white/10">
              <p class="text-2xl font-bold text-emerald-400">✓</p>
              <p class="text-xs text-white/60 mt-1">Active</p>
            </div>
          </div>
        </div>

        <!-- Bottom border -->
        <div class="absolute bottom-0 left-0 right-0 h-px bg-linear-to-r from-transparent via-indigo-500/50 to-transparent" />
      </div>
    </div>
  </Transition>

  <!-- Delete Confirmation Modal -->
  <Transition name="modal-backdrop">
    <div
      v-if="showDeleteConfirm"
      @click="showDeleteConfirm = false"
      class="fixed inset-0 bg-black/80 backdrop-blur-sm z-50"
    />
  </Transition>

  <Transition name="modal-expand">
    <div
      v-if="showDeleteConfirm"
      class="fixed inset-0 z-50 flex items-center justify-center p-4 pointer-events-none"
    >
      <div
        @click.stop
        class="relative w-full max-w-sm bg-linear-to-br from-white/10 via-white/5 to-white/0 backdrop-blur-xl rounded-2xl border border-white/20 overflow-hidden pointer-events-auto p-8 space-y-6"
      >
        <!-- Background -->
        <div class="absolute inset-0 bg-linear-to-br from-red-600/20 via-purple-600/10 to-transparent opacity-40" />

        <!-- Content -->
        <div class="relative z-10 space-y-6">
          <!-- Icon -->
          <div class="flex justify-center">
            <div class="w-16 h-16 rounded-full bg-red-500/20 border border-red-500/30 flex items-center justify-center">
              <svg class="w-8 h-8 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4v2m0 4v2m0-14a9 9 0 1 0 0 18 9 9 0 0 0 0-18z" />
              </svg>
            </div>
          </div>

          <!-- Text -->
          <div class="text-center space-y-2">
            <h3 class="text-xl font-bold text-white">Delete Build #{{ build?.id }}?</h3>
            <p class="text-white/60 text-sm">This action cannot be undone. All files will be permanently deleted.</p>
          </div>

          <!-- Buttons -->
          <div class="flex gap-3 pt-4">
            <button
              @click="showDeleteConfirm = false"
              :disabled="isDeleting"
              class="flex-1 px-4 py-2.5 rounded-lg border border-white/20 hover:border-white/40 text-white hover:bg-white/5 transition-all font-medium disabled:opacity-50"
            >
              Cancel
            </button>
            <button
              @click="deleteBuild"
              :disabled="isDeleting"
              class="flex-1 px-4 py-2.5 rounded-lg bg-red-600 hover:bg-red-700 text-white transition-all font-medium flex items-center justify-center gap-2 disabled:opacity-50"
            >
              <svg v-if="!isDeleting" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
              <svg v-else class="w-4 h-4 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              {{ isDeleting ? 'Deleting...' : 'Delete' }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<style scoped>
.modal-backdrop-enter-active,
.modal-backdrop-leave-active {
  transition: opacity 0.3s ease;
}

.modal-backdrop-enter-from,
.modal-backdrop-leave-to {
  opacity: 0;
}

.modal-expand-enter-active {
  transition: all 0.4s cubic-bezier(0.23, 1, 0.320, 1);
}

.modal-expand-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.modal-expand-enter-from {
  opacity: 0;
  transform: scale(0.85) translateY(20px);
}

.modal-expand-leave-to {
  opacity: 0;
  transform: scale(0.85) translateY(20px);
}
</style>