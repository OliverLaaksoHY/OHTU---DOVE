#!/usr/bin/env bash
set -euo pipefail

export TEST_ENV=true
export DATABASE_URL="${TEST_DATABASE_URL:-sqlite:///test.db}"
export SECRET_KEY="${TEST_SECRET_KEY:-test-only-secret-key}"

uv run python src/db_helper.py
exec uv run python src/index.py
