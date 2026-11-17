#!/usr/bin/env bash
set -euo pipefail

export TEST_ENV=true
export DATABASE_URL="${TEST_DATABASE_URL:-sqlite:///test.db}"

uv run python src/db_helper.py
exec uv run python src/index.py
