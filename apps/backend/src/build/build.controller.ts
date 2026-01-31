import { Body, Controller, Post, Req, UseGuards } from '@nestjs/common'
import { BuildService } from './build.service'
import { JwtAuthGuard } from 'src/auth/auth.guard'
import { BuildsService } from 'src/builds/builds.service'

@Controller('generate')
export class BuildController {
  constructor(private readonly buildService: BuildService, private readonly buildsService: BuildsService) {}

  @Post()
  @UseGuards(JwtAuthGuard)
  async build(@Req() req: any, @Body() payload: any) {
	await this.buildsService.create({
		ownerAddress: req.user.publicKey,
	})
	return this.buildService.triggerWorkflow({
      ...payload,
      address: req.user.publicKey,
    })
  }
}