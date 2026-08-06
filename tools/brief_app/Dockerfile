FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    BRIEF_APP_DATA=/data

WORKDIR /app

# System libs reportlab/Pillow need at runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    libjpeg62-turbo \
    zlib1g \
    libfreetype6 \
    && rm -rf /var/lib/apt/lists/*

COPY tools/brief_app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy app code. tools/ is the package root.
COPY tools/ /app/tools/

# Streamlit reads .streamlit/config.toml from the working dir (/app) → force light EQUALICE theme.
COPY tools/brief_app/.streamlit /app/.streamlit

# Persistent data lives on a mounted volume at /data
RUN mkdir -p /data/customers /data/briefs /data/assets/cache

EXPOSE 8501

# Railway/Render inject $PORT; fall back to 8501 for local docker runs.
CMD ["sh", "-c", "streamlit run tools/brief_app/app.py --server.headless=true --server.port=${PORT:-8501} --server.address=0.0.0.0 --browser.gatherUsageStats=false"]
