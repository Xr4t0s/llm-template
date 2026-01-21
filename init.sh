#!/usr/bin/env bash
set -e

echo "🚀 Initialisation du repo AI / Web3"

# --------------------------------------------------
# Base folders
# --------------------------------------------------
mkdir -p apps/frontend apps/backend

# --------------------------------------------------
# PNPM workspace
# --------------------------------------------------
cat > pnpm-workspace.yaml <<'EOF'
packages:
  - "apps/*"
EOF

# --------------------------------------------------
# ENV
# --------------------------------------------------
cat > .env <<'EOF'
FRONTEND_PORT=3000
BACKEND_PORT=3001
EOF

# --------------------------------------------------
# Frontend — Nuxt 3
# --------------------------------------------------
echo "🧩 Initialisation Nuxt 3"
cd apps/frontend

pnpm create nuxt-app . \
  --packageManager pnpm \
  --no-install

pnpm install

# Dockerfile Front
cat > Dockerfile <<'EOF'
FROM node:20-alpine

WORKDIR /app

RUN corepack enable && corepack prepare pnpm@latest --activate

COPY . .

RUN pnpm install
RUN pnpm build

EXPOSE 3000

CMD ["pnpm", "preview", "--host"]
EOF

cat > .dockerignore <<'EOF'
node_modules
.nuxt
.output
EOF

cd ../../

# --------------------------------------------------
# Backend — NestJS
# --------------------------------------------------
echo "🧠 Initialisation NestJS"
cd apps/backend

pnpm dlx @nestjs/cli new . --package-manager pnpm --skip-git

# Dockerfile Back
cat > Dockerfile <<'EOF'
FROM node:20-alpine

WORKDIR /app

RUN corepack enable && corepack prepare pnpm@latest --activate

COPY . .

RUN pnpm install
RUN pnpm build

EXPOSE 3001

CMD ["node", "dist/main.js"]
EOF

cat > .dockerignore <<'EOF'
node_modules
dist
EOF

cd ../../

# --------------------------------------------------
# docker-compose
# --------------------------------------------------
cat > docker-compose.yml <<'EOF'
version: "3.9"

services:
  frontend:
    build: ./apps/frontend
    ports:
      - "${FRONTEND_PORT}:3000"
    volumes:
      - ./apps/frontend:/app
    command: pnpm dev --host
    depends_on:
      - backend

  backend:
    build: ./apps/backend
    ports:
      - "${BACKEND_PORT}:3001"
    volumes:
      - ./apps/backend:/app
    command: pnpm start:dev
EOF

echo "✅ Initialisation terminée"
echo "➡️ docker compose up --build"
