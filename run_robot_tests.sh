#!/usr/bin/env bash
set -euo pipefail

bash scripts/start-test-server.sh &
server_pid=$!
trap 'kill "$server_pid" 2>/dev/null || true' EXIT

curl --fail --silent --show-error --output /dev/null \
  --retry 20 --retry-delay 1 --retry-connrefused \
  http://localhost:5001/

uv run robot --variable HEADLESS:true src/tests/references.robot
