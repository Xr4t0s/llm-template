// auth.controller.ts
import { Controller, Post, Body, BadRequestException } from '@nestjs/common';
import { AuthService } from './auth.service';

@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {}

  @Post('connect')
  connect(@Body() body: { publicKey: string }) {
    if (!body.publicKey) {
      throw new BadRequestException('publicKey required');
    }
    const payload = this.authService.generatePayload(body.publicKey);
    return { payload };
  }

  @Post('verify')
  verify(
    @Body() body: { publicKey: string; payload: string; signature: string },
  ) {
    const { publicKey, payload, signature } = body;

    if (!publicKey || !payload || !signature) {
      throw new BadRequestException('Missing required fields');
    }

    const isValid = this.authService.verifySignature(
      publicKey,
      payload,
      signature,
    );

    if (!isValid) {
      throw new BadRequestException('Invalid signature');
    }

    const token = this.authService.generateToken(publicKey);
    return { success: true, token, publicKey };
  }
}