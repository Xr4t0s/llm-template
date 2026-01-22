FROM node:20-alpine

WORKDIR /app

RUN corepack enable && corepack prepare pnpm@latest --activate

COPY package.json pnpm-lock.yaml* ./
RUN pnpm install
RUN pnpm add @pinia/nuxt

COPY . .

EXPOSE 3000

CMD ["pnpm", "dev", "--host"]
