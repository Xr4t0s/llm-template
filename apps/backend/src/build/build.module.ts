import { Module } from '@nestjs/common'
import { BuildController } from './build.controller'
import { BuildService } from './build.service'
import { BuildsModule } from 'src/builds/builds.module'

@Module({
  controllers: [BuildController],
  providers: [BuildService],
  imports: [
	BuildsModule
  ]
})
export class BuildModule {}