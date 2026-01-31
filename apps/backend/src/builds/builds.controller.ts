import { Controller, Get, Post, Body, Param, Delete, Req, Res, UseGuards } from '@nestjs/common';
import type { Response } from 'express';
import { BuildsService } from './builds.service';
import { CreateBuildDto } from './dto/create-build.dto';
import { JwtAuthGuard } from '../auth/auth.guard';
import archiver from 'archiver';
import path from 'path';
import fs from 'fs';

@UseGuards(JwtAuthGuard)
@Controller('builds')
export class BuildsController {
  constructor(private readonly buildsService: BuildsService) {}

  @Get()
  async findMyBuilds(@Req() req: any) {
    const builds = await this.buildsService.findByOwnerAddress(req.user.publicKey);
    return { success: true, builds };
  }

  @Post()
  async create(@Body() createBuildDto: CreateBuildDto, @Req() req: any) {
    return this.buildsService.create({
      ...createBuildDto,
      ownerAddress: req.user.publicKey,
    });
  }

  @Get(':id/download')
  async downloadBuild(
    @Param('id') id: string,
    @Req() req: any,
    @Res() res: Response,
  ) {
    try {
      const build = await this.buildsService.findOne(+id);

      if (!build) {
        return res.status(404).json({ error: 'Build not found' });
      }

      if (build.ownerAddress !== req.user.publicKey) {
        return res.status(403).json({ error: 'Unauthorized' });
      }

      const buildFolderPath = path.join(
        `/data/shared/${req.user.publicKey}/${id}`,
      );

      if (!fs.existsSync(buildFolderPath)) {
        return res.status(404).json({ error: 'Build folder not found' });
      }

      res.setHeader(
        'Content-Disposition',
        `attachment; filename="build-${id}.zip"`,
      );
      res.setHeader('Content-Type', 'application/zip');

      const archive = archiver('zip', { zlib: { level: 9 } });

      archive.on('error', (err) => {
        console.error('Archive error:', err);
        res.status(500).json({ error: 'Failed to create archive' });
      });

      archive.pipe(res);
      archive.directory(buildFolderPath, `build-${id}`);
      await archive.finalize();
    } catch (error) {
      console.error('Download error:', error);
      return res.status(500).json({ error: 'Failed to download build' });
    }
  }

  @Delete(':id')
  async remove(@Param('id') id: string, @Req() req: any) {
    const build = await this.buildsService.findOne(+id);

    if (!build) {
      return { error: 'Build not found' };
    }

    if (build.ownerAddress !== req.user.publicKey) {
      return { error: 'Unauthorized' };
    }

    return this.buildsService.remove(+id);
  }
}