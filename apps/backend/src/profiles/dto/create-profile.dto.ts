import { IsString, IsNumber, IsOptional, IsBoolean, Min } from 'class-validator'

export class CreateProfileDto {
  @IsString()
  address: string

  @IsNumber()
  @Min(0)
  builds: number

  @IsOptional()
  @IsBoolean()
  running?: boolean

  @IsOptional()
  @IsNumber()
  step?: number

  @IsOptional()
  @IsNumber()
  substep?: number
}
