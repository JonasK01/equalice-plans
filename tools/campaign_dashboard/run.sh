#!/usr/bin/env bash
# Launch the campaign-ops dashboard locally.
# Usage: bash tools/campaign_dashboard/run.sh
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PY="$ROOT/.venv/bin/python"
[ -x "$PY" ] || PY=python3
exec "$PY" -m streamlit run "$ROOT/tools/campaign_dashboard/app.py" \
  --server.port "${PORT:-8501}" \
  --browser.gatherUsageStats=false
