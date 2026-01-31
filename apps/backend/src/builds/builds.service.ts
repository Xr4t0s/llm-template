import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Build } from './entities/build.entity';
import { CreateBuildDto } from './dto/create-build.dto';
import { UpdateBuildDto } from './dto/update-build.dto';

@Injectable()
export class BuildsService {
  constructor(
    @InjectRepository(Build)
    private readonly buildRepository: Repository<Build>,
  ) {}

  async create(createBuildDto: CreateBuildDto) {
    const build = this.buildRepository.create(createBuildDto);
    return this.buildRepository.save(build);
  }

  async findByOwnerAddress(ownerAddress: string) {
    return this.buildRepository.find({
      where: { ownerAddress },
      order: {
        createdAt: 'DESC', // le plus récent en premier
      },
    });
  }

  async findOne(id: number) {
    return this.buildRepository.findOneBy({ id });
  }

  async update(id: number, updateBuildDto: UpdateBuildDto) {
    await this.buildRepository.update(id, updateBuildDto);
    return this.buildRepository.findOneBy({ id });
  }

  async remove(id: number) {
    const build = await this.buildRepository.findOneBy({ id });
    if (build) {
      return this.buildRepository.remove(build);
    }
  }
}