// auth.service.ts
import { Injectable } from '@nestjs/common';
import nacl from 'tweetnacl';
import * as bs58 from 'bs58';
import { JwtService } from '@nestjs/jwt';
import { ProfilesService } from 'src/profiles/profiles.service';

@Injectable()
export class AuthService {
  constructor(
	private jwtService: JwtService,
	private readonly profilesService: ProfilesService,
  ) {}

  private payloads = new Map<string, { payload: string; timestamp: number }>();

  generatePayload(publicKey: string): string {
    const payload = `Sign this to connect: ${Date.now()}`;
    this.payloads.set(publicKey, { payload, timestamp: Date.now() });
    return payload;
  }

  verifySignature(
    publicKey: string,
    payload: string,
    signature: string,
  ): boolean {
    try {
      const stored = this.payloads.get(publicKey);
      if (!stored || stored.payload !== payload) {
        return false;
      }

      if (Date.now() - stored.timestamp > 5 * 60 * 1000) {
        this.payloads.delete(publicKey);
        return false;
      }

      const publicKeyBytes = bs58.default.decode(publicKey);
      const signatureBytes = Buffer.from(signature, 'hex');
      const messageBytes = Buffer.from(payload, 'utf-8');

      const isValid = nacl.sign.detached.verify(
        messageBytes,
        signatureBytes,
        publicKeyBytes,
      );

      if (isValid) {
        this.payloads.delete(publicKey);
      }

      return isValid;
    } catch (error) {
      console.error('Verification error:', error);
      return false;
    }
  }

  async verifyAndAuthenticate(
    publicKey: string,
    payload: string,
    signature: string,
  ) {
    const isValid = this.verifySignature(publicKey, payload, signature)
  
    if (!isValid) {
      return null
    }
  
    // 🔐 Signature OK → profile garanti
    const profile = await this.profilesService.findOrCreateByAddress(publicKey)
  
    const token = this.generateToken(publicKey)
  
    return {
      token,
      profile,
    }
  }


  generateToken(publicKey: string): string {
    return this.jwtService.sign({ publicKey }, { expiresIn: '7d' });
  }
}