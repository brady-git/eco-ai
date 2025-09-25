#!/usr/bin/env bash
set -euo pipefail
curl -sS http://localhost:8000/healthz | jq .
curl -sS -X POST http://localhost:8000/ask -H "Content-Type: application/json" \
  -d '{"question":"What is Eco Battery?"}' | jq .
