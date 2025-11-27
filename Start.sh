#!/usr/bin/env bash
# simple entrypoint for Codespaces
export PYTHONUNBUFFERED=1
# optionally install deps (Codespaces' devcontainer will usually handle this)
pip install -r requirements.txt
# Run streamlit on 0.0.0.0 so Codespaces can forward it
streamlit run main.py --server.address=0.0.0.0 --server.port=8501
