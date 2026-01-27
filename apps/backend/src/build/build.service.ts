import { Injectable, HttpException, HttpStatus } from '@nestjs/common'
import axios from 'axios'
import { GenerateDocDto } from './dto/project-config.dto'

@Injectable()
export class BuildService {
  private readonly N8N_WEBHOOK_URL =
    process.env.N8N_WEBHOOK_URL || "http://llm-n8n:5678/webhook/a78c2256-c123-4280-b22d-b375ff664f36"

  async triggerWorkflow(payload: any) {
    try {
		console.log(this.N8N_WEBHOOK_URL);
      const res = await axios.post(
        this.N8N_WEBHOOK_URL,
        payload,
        {
          headers: {
            'Content-Type': 'application/json',
          },
          timeout: 15_000,
        },
      )

      return {
        status: 'ok',
        n8nResponse: res.data,
      }
    } catch (err: any) {
      throw new HttpException(
        {
          status: 'n8n_error',
          message: err.message,
          response: err.response?.data,
        },
        HttpStatus.BAD_GATEWAY,
      )
    }
  }
}
