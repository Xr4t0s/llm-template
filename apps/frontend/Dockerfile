FROM node:20-slim

WORKDIR /app

RUN curl -fsSL https://get.pnpm.io/install.sh | sh
RUN corepack enable pnpm

COPY package.json ./
RUN pnpm install
RUN pnpm add @pinia/nuxt

COPY . .

EXPOSE 3000

CMD ["pnpm", "dev", "--host"]
