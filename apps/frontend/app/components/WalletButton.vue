<template>
  <div class="flex items-center gap-3">
    <!-- Not Connected State -->
    <button
      v-if="!authStore.isConnected"
      @click="openAppKit"
      :disabled="isLoading"
      class="group relative px-6 py-2.5 rounded-lg font-medium text-sm text-white overflow-hidden disabled:opacity-50 disabled:cursor-not-allowed transition-all"
    >
      <!-- Gradient background -->
      <div class="absolute inset-0 bg-gradient-to-r from-indigo-600 to-cyan-500 opacity-100 group-hover:opacity-90 group-disabled:opacity-70 transition-opacity" />
      <!-- Shimmer effect -->
      <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:translate-x-full group-disabled:translate-x-full transition-transform duration-500" />
      <!-- Content -->
      <span class="relative flex items-center gap-2">
        <svg
          v-if="isLoading"
          class="w-4 h-4 animate-spin"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
        </svg>
        <span v-else>
          <svg class="w-4 h-4 inline mr-1" fill="currentColor" viewBox="0 0 20 20">
            <path d="M18 9a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          Connect Wallet
        </span>
      </span>
    </button>

    <!-- Connected State -->
    <div v-else class="flex items-center gap-3">
      <!-- Address Display with Copy -->
      <div class="group relative">
        <!-- Background glow -->
        <div class="absolute inset-0 bg-gradient-to-r from-indigo-600/20 to-cyan-500/20 rounded-lg blur opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
        <!-- Card -->
        <button
          @click="copyAddress"
          class="relative flex items-center gap-2 px-4 py-2.5 rounded-lg bg-white/5 backdrop-blur-xl border border-white/20 group-hover:border-white/30 group-hover:bg-white/10 transition-all duration-300 cursor-pointer"
          :title="account.address || undefined"
        >
          <!-- Online indicator -->
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-gradient-to-r from-green-400 to-emerald-500 animate-pulse" />
            <span class="font-mono text-xs text-white/80">
              {{ shortenAddress(account.address!) }}
            </span>
          </div>

          <!-- Copy icon -->
          <svg
            class="w-4 h-4 text-white/50 group-hover:text-white/80 transition-colors opacity-0 group-hover:opacity-100"
            fill="currentColor"
            viewBox="0 0 20 20"
          >
            <path d="M7 9a2 2 0 11-4 0 2 2 0 014 0z" />
            <path fill-rule="evenodd" d="M7.465 11.293a1 1 0 001.414 0l2.828-2.829a1 1 0 00-1.414-1.414L8 9.172V5a1 1 0 00-2 0v4.172L5.05 7.05a1 1 0 00-1.414 1.414l2.828 2.829z" clip-rule="evenodd" />
          </svg>
        </button>

        <!-- Tooltip on copy -->
        <Transition name="fade">
          <div
            v-if="copied"
            class="absolute top-full left-1/2 -translate-x-1/2 mt-2 px-3 py-1.5 rounded-lg bg-emerald-500/20 border border-emerald-500/30 text-emerald-300 text-xs font-medium whitespace-nowrap"
          >
            ✓ Copied!
          </div>
        </Transition>
      </div>

      <!-- Disconnect Button -->
      <button
        @click="handleDisconnect"
        class="group relative px-4 py-2.5 rounded-lg font-medium text-sm text-white/80 overflow-hidden transition-all hover:text-white"
      >
        <!-- Border -->
        <div class="absolute inset-0 border border-white/20 rounded-lg group-hover:border-red-500/50 transition-colors" />
        <!-- Hover background -->
        <div class="absolute inset-0 bg-red-500/10 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity" />
        <!-- Content -->
        <span class="relative flex items-center gap-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
          </svg>
          Disconnect
        </span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue'
import { useAppKit, useAppKitAccount, useDisconnect } from "@reown/appkit/vue"
import { useAppKitProvider } from "@reown/appkit/vue"
import type { Provider } from "@reown/appkit-adapter-solana/vue"
import { useAuthStore } from '~/stores/auth'

const authStore = useAuthStore()
const { open, close } = useAppKit()
const account = useAppKitAccount({ namespace: "solana" })
const { walletProvider } = useAppKitProvider<Provider>("solana")

const copied = ref(false)
const isLoading = ref(false)

// Computed pour accéder facilement à isConnected
const isConnected = computed(() => account.value.isConnected)

/**
 * Raccourcit une adresse Solana
 */
function shortenAddress(addr: string | null): string {
  if (!addr) return ''
  return `${addr.slice(0, 6)}...${addr.slice(-4)}`
}

/**
 * Ouvre le modal de connexion AppKit
 */
function openAppKit() {
//   open()
}

/**
 * Copie l'adresse dans le presse-papiers
 */
async function copyAddress() {
  if (!account.value.address) return

  try {
    await navigator.clipboard.writeText(account.value.address)
    copied.value = true
    setTimeout(() => {
      copied.value = false
    }, 2000)
  } catch (err) {
    console.error('Erreur lors de la copie:', err)
  }
}

/**
 * Déconnecte le portefeuille
 */
async function handleDisconnect() {
  try {
    authStore.logout()
  } catch (err) {
    console.error('Erreur lors de la déconnexion:', err)
  }
}

/**
 * Signe le payload avec le wallet
 */
async function sign(payload: string): Promise<string> {
  if (!walletProvider) {
    throw new Error("Wallet provider non disponible")
  }

  const messageBytes = new TextEncoder().encode(payload)
  const sig = await walletProvider.signMessage(messageBytes)

  if (!sig) {
    throw new Error("Signature manquante")
  }

  return Buffer.from(sig).toString("hex")
}

/**
 * Écoute la connexion et synchronise avec le store d'authentification
 */
watch(
  () => account.value.isConnected,
  async (connected) => {
    if (!connected) {
      authStore.logout()
      return
    }

    isLoading.value = true

    try {
      // 1. Récupérer le payload à signer
      const response = await fetch("/api/v1/auth/connect", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          publicKey: account.value.address,
        }),
      })

      if (!response.ok) {
        throw new Error(`Erreur API Connect: ${response.status}`)
      }

      const data = await response.json()

      if (!data.payload) {
        throw new Error("Payload manquant dans la réponse")
      }

      // 2. Signer le payload
      const signature = await sign(data.payload)

      // 3. Vérifier la signature et récupérer le token
      const verifyRes = await fetch("/api/v1/auth/verify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          publicKey: account.value.address,
          payload: data.payload,
          signature: signature,
        }),
      })

      if (!verifyRes.ok) {
        throw new Error(`Erreur API Verify: ${verifyRes.status}`)
      }

      const verifyData = await verifyRes.json()

      // 4. Synchroniser avec le store d'authentification
      if (verifyData.token && verifyData.profile) {
        authStore.setConnection(
          account.value.address || '',
          walletProvider,
          verifyData.token,
          verifyData.profile
        )
      } else {
        throw new Error("Token ou profile manquant dans la réponse")
      }
    } catch (error) {
      const message = error instanceof Error ? error.message : "Erreur de connexion"
      console.error("Erreur lors de la synchronisation:", error)
      authStore.error = message
      await close()
    } finally {
      isLoading.value = false
    }
  },
  { immediate: true }
)
</script>

<style scoped>
/* Fade transition for tooltip */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>