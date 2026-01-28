import { createAppKit } from '@reown/appkit/vue'
import { EthersAdapter } from '@reown/appkit-adapter-ethers'
import { SolanaAdapter } from '@reown/appkit-adapter-solana'
import { mainnet, arbitrum, base, solana } from '@reown/appkit/networks'

const config = useRuntimeConfig()
const projectId = config.public.projectId

createAppKit({
	adapters: [new EthersAdapter(), new SolanaAdapter()],
	networks: [mainnet, arbitrum, base, solana],
	projectId,
	features: {
		analytics: true
	}
})