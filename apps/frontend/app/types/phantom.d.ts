// types/phantom.d.ts

export {};

declare global {
  interface Window {
    phantom?: {
      solana?: {
        isConnected: boolean;
        publicKey: { toString(): string };
        connect(): Promise<{ publicKey: { toString(): string } }>;
        disconnect(): Promise<void>;
        signTransaction(tx: any): Promise<any>;
        signMessage(msg: Uint8Array): Promise<any>;
      };
    };
  }
}
