FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    GRADIO_SERVER_NAME=0.0.0.0 \
    GRADIO_SERVER_PORT=7860 \
    HF_HOME=/data/hf

# Dépendances système minimales
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    bash \
    curl \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Clone du repo
RUN git clone --depth 1 https://github.com/newideas99/ultra-fast-image-gen.git /app

# Install deps python
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Prépare les dossiers (volumes)
RUN mkdir -p /data/hf /data/shared/images

EXPOSE 7860

# Healthcheck simple (Gradio répond en HTTP)
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=5 \
  CMD curl -fsS http://127.0.0.1:7860/ || exit 1

# Démarrage :
# - on s'assure que /data/shared/images existe
# - on crée des symlinks "best effort" vers des noms de dossiers de sortie courants
#   (si l'app écrit dans l'un d'eux, ça finira dans ton volume)
CMD ["bash", "-lc", "\
  set -e; \
  mkdir -p /data/shared/images; \
  for d in outputs output results images generated; do \
    rm -rf \"/app/${d}\"; \
    ln -s \"/data/shared/images\" \"/app/${d}\"; \
  done; \
  python app.py \
"]
