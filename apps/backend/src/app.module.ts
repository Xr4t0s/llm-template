import { Module } from '@nestjs/common'
import { HealthController } from './health/health.controller'
import { BuildModule } from './build/build.module';
import { AuthModule } from './auth/auth.module';
import { DatabaseModule } from './database/database.module';
import { ProfilesModule } from './profiles/profiles.module';
import { BuildsModule } from './builds/builds.module'

@Module({
  controllers: [HealthController],
  imports: [BuildModule, AuthModule, DatabaseModule, ProfilesModule, BuildsModule],
})
export class AppModule {}
