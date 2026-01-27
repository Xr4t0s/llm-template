import { IsBoolean, IsEnum, IsNumber, IsString, IsArray, ValidateNested } from 'class-validator'
import { Type } from 'class-transformer'

export enum Tone {
  Serious = 'Serious',
  Meme = 'Meme',
  Professional = 'Professional',
  Technical = 'Technical',
}

export enum TaglineStyle {
  ShortPunchy = 'Short & punchy',
  Long = 'Long',
  Descriptive = 'Descriptive',
}

export enum ProjectType {
  Meme = 'meme',
  Defi = 'defi',
  Nft = 'nft',
  Dao = 'dao',
  Protocol = 'protocol',
  Tool = 'tool', // ✅ AJOUTÉ
}

export enum Goal {
  Community = 'community',
  Utility = 'utility',
  Governance = 'governance',
}

export enum VisualVibe {
  Clean = 'clean',
  Bold = 'bold',
  Dark = 'dark',
  Playful = 'playful',
}


export class OutputsDto {
  @IsBoolean() logo: boolean
  @IsBoolean() banner: boolean
  @IsBoolean() pfp: boolean
  @IsBoolean() announcements: boolean
  @IsBoolean() memes: boolean
  @IsBoolean() stickers: boolean
  @IsBoolean() documentation: boolean
  @IsBoolean() onepager: boolean
  @IsBoolean() roadmap: boolean
  @IsBoolean() faq: boolean
}

export class ProjectConfigDto {
  @IsString()
  lore: string

  @IsBoolean()
  hasMascot: boolean

  @IsEnum(Tone)
  tone: Tone

  @IsEnum(TaglineStyle)
  taglineStyle: TaglineStyle

  @IsEnum(ProjectType)
  projectType: ProjectType

  @IsEnum(Goal)
  goal: Goal

  @IsEnum(VisualVibe)
  visualVibe: VisualVibe

  @IsArray()
  @IsString({ each: true })
  palettes: string[]

  @ValidateNested()
  @Type(() => OutputsDto)
  outputs: OutputsDto
}

export class GenerateDocDto {
  @IsString()
  sessionId: string

  @IsNumber()
  step: number

  @IsString()
  prompt: string

  @ValidateNested()
  @Type(() => ProjectConfigDto)
  data: ProjectConfigDto
}