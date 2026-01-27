import { Module } from '@nestjs/common'
import { HealthController } from './health/health.controller'
import { BuildController } from './build/build.controller';
import { BuildModule } from './build/build.module';

@Module({
  controllers: [HealthController],
  imports: [BuildModule],
})
export class AppModule {}
