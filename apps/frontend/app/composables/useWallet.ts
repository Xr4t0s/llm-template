import { createAppKit } from '@reown/appkit/vue'
import { EthersAdapter } from '@reown/appkit-adapter-ethers'
import { mainnet, arbitrum, base, solana } from '@reown/appkit/networks'

const config = useRuntimeConfig()
const projectId = config.public.projectId

createAppKit({
	adapters: [new EthersAdapter()],
	networks: [mainnet, arbitrum, base, solana],
	projectId,
	features: {
		analytics: true
	}
})