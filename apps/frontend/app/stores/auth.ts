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

export const useAuthStore = defineStore('auth', () => {
  const isConnected = ref(false);
  const publicKey = ref<string | null>(null);
  const isLoading = ref(false);
  const token = ref<string | null>(null);
  const profile = ref<Profile | null>(null);

  const toHex = (arr: Uint8Array): string => {
    return Array.from(arr)
      .map(b => b.toString(16).padStart(2, '0'))
      .join('');
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

  const connect = async () => {
    if (!window.phantom?.solana) {
      alert('Install Phantom wallet');
      return;
    }

    isLoading.value = true;
    try {
      const response = await window.phantom.solana.connect();
      const userPublicKey = response.publicKey.toString();
      publicKey.value = userPublicKey;

      const payloadRes = await fetch('/api/v1/auth/connect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ publicKey: userPublicKey }),
      });

      if (!payloadRes.ok) throw new Error('Failed to get payload');
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

      if (!verifyRes.ok) throw new Error('Verification failed');
      
      const result = await verifyRes.json();
      token.value = result.token;
	  profile.value = result.profile;
      
      if (typeof window !== 'undefined') {
        localStorage.setItem('auth_token', result.token);
      }
      
      isConnected.value = true;
      return result;
    } catch (error) {
      console.error('Connection failed:', error);
      publicKey.value = null;
      isConnected.value = false;
      token.value = null;
      throw error;
    } finally {
      isLoading.value = false;
    }
  };

  const logout = () => {
    isConnected.value = false;
    publicKey.value = null;
    token.value = null;
    if (typeof window !== 'undefined') {
      localStorage.removeItem('auth_token');
    }
  };

  const pay = async (recipientAddress: string) => {
    if (!publicKey.value) return;
    
    isLoading.value = true;
    try {
      const connection = new Connection('https://solana-mainnet.g.alchemy.com/v2/rU0nq5sFxE-T0pZgsspPrSWpQ6tvKo5-');
      
      const transaction = new Transaction().add(
        SystemProgram.transfer({
          fromPubkey: new PublicKey(publicKey.value),
          toPubkey: new PublicKey(recipientAddress),
          lamports: Math.floor(0.5 * LAMPORTS_PER_SOL),
        })
      );

      const { blockhash } = await connection.getLatestBlockhash();
      transaction.recentBlockhash = blockhash;
      transaction.feePayer = new PublicKey(publicKey.value);

      const signed = await window.phantom?.solana!.signTransaction(transaction);
      const sig = await connection.sendRawTransaction(signed.serialize());
      
      return sig;
    } finally {
      isLoading.value = false;
    }
  };

  return { isConnected, publicKey, token, isLoading, connect, logout, pay, initFromStorage };
});