import { Module } from '@nestjs/common';
import { ConfigService, ConfigModule } from '@nestjs/config';
import { TypeOrmModule } from '@nestjs/typeorm';

@Module({
	imports: [
		TypeOrmModule.forRootAsync({
			imports: [ConfigModule],
			useFactory: (configService: ConfigService) => ({
				type: 'postgres',
				host: 'llm-db',
				port: 5432,
				database: 'llm_template',
				username: 'postgres',
				password: 'password',
				autoLoadEntities: true,
				synchronize: true // pas en prod
			}),
			inject: [ConfigService]
		})
	]
})
export class DatabaseModule {}
