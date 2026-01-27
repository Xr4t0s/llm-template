import { Body, Controller, Post } from '@nestjs/common'
import { BuildService } from './build.service'

@Controller('generate')
export class BuildController {
  constructor(private readonly daService: BuildService) {}

  @Post('doc')
  async buildBuild(@Body() payload: any) {
    return this.daService.triggerWorkflow(payload)
  }
}