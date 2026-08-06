#!/usr/bin/env bash
# Launcher for the EQUALICE Brief Generator Streamlit app.
# Resolves streamlit even when it's a Python user-install on macOS.

set -e
cd "$(dirname "$0")/../.."

if command -v streamlit >/dev/null 2>&1; then
  STREAMLIT="streamlit"
elif [ -x "$HOME/Library/Python/3.9/bin/streamlit" ]; then
  STREAMLIT="$HOME/Library/Python/3.9/bin/streamlit"
elif [ -x "$HOME/Library/Python/3.10/bin/streamlit" ]; then
  STREAMLIT="$HOME/Library/Python/3.10/bin/streamlit"
elif [ -x "$HOME/Library/Python/3.11/bin/streamlit" ]; then
  STREAMLIT="$HOME/Library/Python/3.11/bin/streamlit"
elif [ -x "$HOME/Library/Python/3.12/bin/streamlit" ]; then
  STREAMLIT="$HOME/Library/Python/3.12/bin/streamlit"
else
  echo "streamlit not found. Install with: pip3 install --user streamlit"
  exit 1
fi

exec "$STREAMLIT" run tools/brief_app/app.py "$@"
