<template>
  <div class="flex items-center gap-2">
    <button 
      v-if="!authStore.isConnected" 
      @click="authStore.connect" 
      :disabled="authStore.isLoading"
      class="
        px-4 py-2 rounded-lg
        bg-indigo-600 hover:bg-indigo-700
        text-white text-sm font-medium
        transition-colors duration-200
        disabled:opacity-50 disabled:cursor-not-allowed
      "
    >
      {{ authStore.isLoading ? 'Connecting...' : 'Connect' }}
    </button>
    
    <div v-else class="flex items-center gap-2">
      <div class="text-xs text-gray-400 font-mono">
        {{ authStore.publicKey?.slice(0, 6) }}...{{ authStore.publicKey?.slice(-4) }}
      </div>
      
      <button 
        @click="authStore.logout"
        class="
          px-3 py-2 rounded-lg
          bg-gray-700 hover:bg-gray-600
          text-white text-xs font-medium
          transition-colors duration-200
        "
      >
        Disconnect
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/stores/auth';

const authStore = useAuthStore();
</script>