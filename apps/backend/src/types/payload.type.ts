export type ProjectConfig = {
  step: number

  lore: string
  hasMascot: boolean
  tone: 'Serious' | 'Meme' | 'Professional' | 'Technical'
  taglineStyle: 'Short & punchy' | 'Long' | 'Descriptive'
  projectType: 'meme' | 'defi' | 'nft' | 'dao' | 'protocol'
  goal: 'community' | 'utility' | 'governance'
  visualVibe: 'clean' | 'bold' | 'dark' | 'playful'

  palettes: Array<
    | 'indigo'
    | 'lime'
    | 'red'
    | 'blue'
    | 'purple'
    | 'black'
    | 'white'
  >

  outputs: {
    logo: boolean
    banner: boolean
    pfp: boolean
    announcements: boolean
    memes: boolean
    stickers: boolean
    documentation: boolean
    onepager: boolean
    roadmap: boolean
    faq: boolean
  }
}
