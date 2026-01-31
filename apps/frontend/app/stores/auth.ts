import { defineStore } from 'pinia';
import { ref } from 'vue';
import { Connection, Transaction, SystemProgram, LAMPORTS_PER_SOL, PublicKey } from '@solana/web3.js';

type Profile = {
	address: string
	builds: number
	running: boolean
	step: number
	substep: number
}

const SOLANA_RPC_URL = 'https://api.mainnet-beta.solana.com';

export const useAuthStore = defineStore('auth', () => {
  const isConnected = ref(false);
  const publicKey = ref<string | null>(null);
  const isLoading = ref(false);
  const token = ref<string | null>(null);
  const profile = ref<Profile | null>(null);
  const error = ref<string | null>(null);

  const toHex = (arr: Uint8Array): string => {
    return Array.from(arr)
      .map(b => b.toString(16).padStart(2, '0'))
      .join('');
  };

  const clearError = () => {
    error.value = null;
  };

  const initFromStorage = () => {
    if (typeof window !== 'undefined') {
      const storedToken = localStorage.getItem('auth_token');
      if (storedToken) {
        token.value = storedToken;
        isConnected.value = true;
      }
    }
  };

  /**
   * Initialise la connexion via AppKit (Reown)
   * À utiliser après la connexion depuis AppKit
   */
  const setConnection = (
    key: string,
    provider: any,
    jwt: string,
    prof: Profile
  ) => {
    publicKey.value = key;
    token.value = jwt;
    profile.value = prof;
    isConnected.value = true;
    error.value = null;

    if (typeof window !== 'undefined') {
      localStorage.setItem('auth_token', jwt);
    }
  };

  /**
   * Connexion via Phantom wallet (méthode legacy)
   */
  const connect = async () => {
    if (!window.phantom?.solana) {
      error.value = 'Install Phantom wallet';
      return;
    }

    isLoading.value = true;
    clearError();

    try {
      const response = await window.phantom.solana.connect();
      const userPublicKey = response.publicKey.toString();
      publicKey.value = userPublicKey;

      const payloadRes = await fetch('/api/v1/auth/connect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ publicKey: userPublicKey }),
      });

      if (!payloadRes.ok) {
        throw new Error('Failed to get payload');
      }

      const { payload } = await payloadRes.json();

      const messageBytes = new TextEncoder().encode(payload);
      const signedMessage = await window.phantom.solana.signMessage(messageBytes);
      const signature = toHex(signedMessage.signature);

      const verifyRes = await fetch('/api/v1/auth/verify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          publicKey: userPublicKey,
          payload,
          signature,
        }),
      });

      if (!verifyRes.ok) {
        throw new Error('Verification failed');
      }

      const result = await verifyRes.json();
      token.value = result.token;
      profile.value = result.profile;

      if (typeof window !== 'undefined') {
        localStorage.setItem('auth_token', result.token);
      }

      isConnected.value = true;
      return result;
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Connection failed';
      error.value = message;
      console.error('Connection failed:', err);
      publicKey.value = null;
      isConnected.value = false;
      token.value = null;
      profile.value = null;
      throw err;
    } finally {
      isLoading.value = false;
    }
  };

  const logout = () => {
    isConnected.value = false;
    publicKey.value = null;
    token.value = null;
    profile.value = null;
    error.value = null;

    if (typeof window !== 'undefined') {
      localStorage.removeItem('auth_token');
    }
  };

  const pay = async (recipientAddress: string, amount: number = 0.5) => {
    if (!publicKey.value) {
      error.value = 'Wallet not connected';
      return null;
    }

    isLoading.value = true;
    clearError();

    try {
      // Validate recipient address
      new PublicKey(recipientAddress);

      const connection = new Connection(SOLANA_RPC_URL);

      const transaction = new Transaction().add(
        SystemProgram.transfer({
          fromPubkey: new PublicKey(publicKey.value),
          toPubkey: new PublicKey(recipientAddress),
          lamports: Math.floor(amount * LAMPORTS_PER_SOL),
        })
      );

      const { blockhash } = await connection.getLatestBlockhash();
      transaction.recentBlockhash = blockhash;
      transaction.feePayer = new PublicKey(publicKey.value);

      const signed = await window.phantom?.solana!.signTransaction(transaction);
      const sig = await connection.sendRawTransaction(signed.serialize());

      await connection.confirmTransaction(sig);

      return sig;
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Payment failed';
      error.value = message;
      console.error('Payment error:', err);
      return null;
    } finally {
      isLoading.value = false;
    }
  };

  return {
    isConnected,
    publicKey,
    token,
    profile,
    isLoading,
    error,
    connect,
    setConnection,
    logout,
    pay,
    clearError,
    initFromStorage,
  };
});