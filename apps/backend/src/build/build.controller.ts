import { Body, Controller, Post, Req, UseGuards } from '@nestjs/common'
import { BuildService } from './build.service'
import { JwtAuthGuard } from 'src/auth/auth.guard'

@Controller('generate')
export class BuildController {
  constructor(private readonly buildService: BuildService) {}

  @Post('doc')
  @UseGuards(JwtAuthGuard)
  async buildBuild(@Req() req: any, @Body() payload: any) {
	return this.buildService.triggerWorkflow({
      ...payload,
      address: req.user.publicKey,
    })
  }
}