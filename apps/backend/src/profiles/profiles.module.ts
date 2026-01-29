import { Module } from '@nestjs/common';
import { Profile } from './entities/profile.entity';
import { ProfilesService } from './profiles.service';
import { ProfilesController } from './profiles.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { JwtStrategy } from 'src/auth/jwt.strategy';
import { PassportModule } from '@nestjs/passport';
import { JwtModule } from '@nestjs/jwt';

@Module({
  imports: [
	TypeOrmModule.forFeature([Profile]),
	PassportModule,
	JwtModule.register({
	  secret: process.env.JWT_SECRET || 'your-secret-key',
      signOptions: { expiresIn: '1h' },
	})
  ],
  controllers: [ProfilesController],
  providers: [ProfilesService, JwtStrategy],
  exports: [ProfilesService]
})
export class ProfilesModule {}
