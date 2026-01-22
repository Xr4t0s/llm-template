export type ProjectType = 'meme' | 'tool' | 'defi' | ''
export type ProjectGoal = 'community' | 'utility' | 'experiment' | 'launch' | ''

export interface BuildOutputs {
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
