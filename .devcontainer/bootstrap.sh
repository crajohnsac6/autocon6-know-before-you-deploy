#!/usr/bin/env bash
# Prepare a workshop Codespace. Safe to re-run; prints no secret values.
set -euo pipefail
cd "$(dirname "$0")/.."

CONTAINERLAB_VERSION=0.82.0

step() { printf '\n== %s\n' "$*"; }

step "Python tools (uv; the workshop CLI, netlab, NAPALM and the Forward SDK from uv.lock)"
command -v uv >/dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
uv sync --frozen
# netlab (pinned in pyproject.toml, with the Netmiko it configures the routers with) is installed by uv sync above, into the
# same environment as the workshop: `workshop up` calls it in-process, and `netlab status` / `netlab connect r1` work in the terminal.

step "sshpass (netlab checks the routers' SSH with it before it configures them)"
command -v sshpass >/dev/null || { sudo apt-get update -qq && sudo apt-get install -y -qq sshpass >/dev/null; }

step "containerlab ${CONTAINERLAB_VERSION}"
if ! containerlab version 2>/dev/null | grep -q "version: ${CONTAINERLAB_VERSION}"; then
  bash -c "$(curl -sL https://get.containerlab.dev)" -- -v "${CONTAINERLAB_VERSION}"
fi

step "cEOS image"
if ! docker image inspect ceos:4.36.0.1F >/dev/null 2>&1; then
  echo "cEOS 4.36.0.1F is not imported yet: download the 64-bit cEOS-lab image from Arista with your own account, then"
  echo "  docker import <that file> ceos:4.36.0.1F"
  echo "and run this script again. Carrying on with the rest of the setup."
fi

step "Headless collector (matching the Forward server release)"
if [ -n "${FORWARD_URL:-}" ]; then
  .venv/bin/workshop collector || echo "collector download deferred: run 'workshop collector' after your seat secrets are set"
fi

step "Doctor"
.venv/bin/workshop doctor || true
