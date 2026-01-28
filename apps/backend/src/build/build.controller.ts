import { Body, Controller, Post, UseGuards } from '@nestjs/common'
import { BuildService } from './build.service'
import { JwtAuthGuard } from 'src/auth/auth.guard'

@Controller('generate')
export class BuildController {
  constructor(private readonly daService: BuildService) {}

  @Post('doc')
  @UseGuards(JwtAuthGuard)
  async buildBuild(@Body() payload: any) {
    return this.daService.triggerWorkflow(payload)
  }
}