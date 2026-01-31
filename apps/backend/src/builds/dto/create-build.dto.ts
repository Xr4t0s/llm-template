import { IsString } from 'class-validator'

export class CreateBuildDto {
  @IsString()
  ownerAddress: string
}