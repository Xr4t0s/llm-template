import { Injectable, HttpException, HttpStatus } from '@nestjs/common'
import axios from 'axios'

@Injectable()
export class BuildService {
  private readonly N8N_WEBHOOK_URL =
    process.env.N8N_WEBHOOK_URL || "http://llm-n8n:5678/webhook-test/a78c2256-c123-4280-b22d-b375ff664f36"

  async triggerWorkflow(payload: any) {
    try {
	  console.log(this.N8N_WEBHOOK_URL);
      let res = await axios.post(
        this.N8N_WEBHOOK_URL,
		payload={
			sessionId: "2b6390ca51ec4a7eb3f9e65ed9536684",
			step: 1,
			prompt: "Use only the generate_documentation tool to perform the step mentionned, STEP 1: Documentation generation.",
			data: payload,
		},
        {
          headers: {
            'Content-Type': 'application/json',
          },
		  timeout: 300000
        },
      )
	  
	  if (res.status == 200) {
        return {
		  success: true,
          result: res.data
        }
	  } else {
		return {
			success: false,
			result: res.data
		}
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
