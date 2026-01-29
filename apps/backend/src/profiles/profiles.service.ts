import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Profile } from './entities/profile.entity';
import { CreateProfileDto } from './dto/create-profile.dto';

@Injectable()
export class ProfilesService {
  constructor(
    @InjectRepository(Profile)
    private readonly profileRepository: Repository<Profile>,
  ) {}

  async create(createProfileDto: CreateProfileDto) {
    const profile = this.profileRepository.create(createProfileDto);
    return this.profileRepository.save(profile);
  }

//   async findAll() {
//     return this.profileRepository.find();
//   }

  async find(address: string) {
	return await this.profileRepository.findOneBy({ address });
  }

  async findOrCreateByAddress(address: string) {
    let profile = await this.profileRepository.findOneBy({ address })
  
    if (!profile) {
      profile = this.profileRepository.create({
        address,
        builds: 0,
        running: false,
        step: 0,
        substep: 0,
      })
  
      profile = await this.profileRepository.save(profile)
	}
    return profile
  }

//   async remove(id: number) {
//     const profile = await this.profileRepository.findOneBy({ id });
//     if (profile) {
//       return this.profileRepository.remove(profile);
//     }
//   }
}