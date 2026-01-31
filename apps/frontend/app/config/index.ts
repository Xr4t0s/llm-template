import { SolanaAdapter } from '@reown/appkit-adapter-solana'
import { solana, solanaTestnet, solanaDevnet, type AppKitNetwork } from '@reown/appkit/networks'


export const projectId = import.meta.env.VITE_PROJECT_ID || "dfbe3045d4172b6f8b4e332240c3e2a1" // this is a public projectId only to use on localhost
if (!projectId) {
  throw new Error('VITE_PROJECT_ID is not set')
}

export const networks: [AppKitNetwork, ...AppKitNetwork[]] = [solana, solanaTestnet, solanaDevnet]

export const solanaWeb3JsAdapter = new SolanaAdapter()