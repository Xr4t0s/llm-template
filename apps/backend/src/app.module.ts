import { Module } from '@nestjs/common'
import { HealthController } from './health/health.controller'
import { BuildController } from './build/build.controller';
import { BuildModule } from './build/build.module';
import { AuthModule } from './auth/auth.module';

@Module({
  controllers: [HealthController],
  imports: [BuildModule, AuthModule],
})
export class AppModule {}
