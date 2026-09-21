#!/usr/bin/env bash
# Install the graphify skill and print the commands to run inside your assistant.
# Commands and file names follow the project README (github.com/safishamsi/graphify).
set -euo pipefail

SKILLS_DIR="${SKILLS_DIR:-$HOME/.claude/skills}"   # adjust for your client
PROJECT_DIR="${1:-.}"

echo "Python check (README requires 3.10+):"
python --version || python3 --version

mkdir -p "$SKILLS_DIR"
if [ -d "$SKILLS_DIR/graphify" ]; then
  echo "graphify already present in $SKILLS_DIR, pulling latest"
  git -C "$SKILLS_DIR/graphify" pull --ff-only
else
  git clone https://github.com/safishamsi/graphify "$SKILLS_DIR/graphify"
fi

cat <<EOF

Installed. Now open your AI coding assistant in $PROJECT_DIR and type:

  /graphify .

You get graphify-out/ with graph.html, GRAPH_REPORT.md and graph.json.
For an architecture page with Mermaid call-flow diagrams, run:

  graphify export callflow-html

Then inspect the JSON with:

  python3 examples/inspect_graph.py graphify-out/graph.json
EOF
