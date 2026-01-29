import { Controller, Get, Req, Post, Body, Patch, Param, Delete, UseGuards } from '@nestjs/common';
import { ProfilesService } from './profiles.service';
import { CreateProfileDto } from './dto/create-profile.dto';
import { JwtAuthGuard } from '../auth/auth.guard';
import { cpSync } from 'fs';

@UseGuards(JwtAuthGuard)
@Controller('profile')
export class ProfilesController {
  constructor(private readonly profilesService: ProfilesService) {}

//   @Post()
//   create(@Body() createProfileDto: CreateProfileDto) {
//     return this.profilesService.create(createProfileDto);
//   }

//   @Get()
//   findAll() {
//     return this.profilesService.findAll();
//   }
	@Get()
		async findMe(@Req() req: any) {
		const profile = await this.profilesService.find(req.user.publicKey);
		return {success: true, profile}
	}

//   @Patch(':id')
//   update(@Param('id') id: string, @Body() updateProfileDto: UpdateProfileDto) {
//     return this.profilesService.update(+id, updateProfileDto);
//   }

//   @Delete(':id')
//   remove(@Param('id') id: string) {
//     return this.profilesService.remove(+id);
//   }
}
