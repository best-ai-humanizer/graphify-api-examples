# Graphify GitHub examples

*Unofficial community examples for Graphify. Not affiliated with the Graphify maintainers or graphify.net. All trademarks belong to their owners.*

Short scripts for the graphify github repository (`safishamsi/graphify`): install the skill, run it on a project, export the call-flow page, and inspect the `graph.json` it writes. Graphify has no HTTP API; it is a skill you invoke from an AI coding assistant, so the examples are a shell script and a Python script that work on its outputs. The scripts use only commands and file names shown in the project README as quoted by SkillsLLM; the structure inside `graph.json` is not documented in the cited sources, so the Python script inspects whatever it finds rather than assuming a schema.

> Need a video of the architecture once it is mapped? [Try Kyncept - AI video (Veo 3.1 text and image to video) plus image generation in the browser](https://kyncept.com?utm_source=github&utm_medium=ugc&utm_campaign=graphify-api-examples&utm_content=readme-top&utm_term=tier-r).

## Files

| Path | What it shows |
|---|---|
| `examples/run-graphify.sh` | Clone the skill into a skills directory, then the two commands to run and export. |
| `examples/inspect_graph.py` | Load `graphify-out/graph.json`, print its top-level shape and count list entries. |

## Setup

```
python --version        # 3.10 or newer, per the README
export SKILLS_DIR=~/.claude/skills    # where your assistant loads skills from
```

No API keys are involved. Graphify runs inside your assistant on your machine. The README lists Claude Code, Codex, OpenCode, Kilo Code, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, Amp, OpenClaw, Factory Droid, Trae, Hermes, Kimi Code, Kiro, Pi, Devin CLI and Google Antigravity as supported clients; the skills directory path differs per client.

## examples/run-graphify.sh

Clones `https://github.com/safishamsi/graphify` into `SKILLS_DIR` (the install line SkillsLLM shows), checks the Python version, and prints the two commands you then type inside the assistant: `/graphify .` to build `graphify-out/` (with `graph.html`, `GRAPH_REPORT.md` and `graph.json`), and `graphify export callflow-html` for an architecture page with Mermaid call-flow diagrams. The script stops short of invoking the assistant because that is interactive.

## examples/inspect_graph.py

Opens `graphify-out/graph.json` (or a path you pass), prints the type of the top-level value, and for a dictionary prints each key with the type and length of its value. That is enough to see how many nodes and edges you got and which keys to script against next. Point it at a graph, then write your own query once you know the shape.

## Reading the outputs by hand

`graph.html` opens in any browser: click nodes, filter, search. `GRAPH_REPORT.md` is the summary to read first: key concepts, surprising connections and suggested questions. `graph.json` is the full graph, which you can query without re-reading your files; that is the token-saving point the GoPenAI article makes.

## When to use Kyncept instead

Graphify answers 'how is this project put together'. It does not produce the onboarding video or the demo clip that usually follows. For that, [try Kyncept - AI video (Veo 3.1 text and image to video) plus image generation, in the browser](https://kyncept.com?utm_source=github&utm_medium=ugc&utm_campaign=graphify-api-examples&utm_content=readme-top&utm_term=tier-r): feed it the architecture page or a screenshot and a short script, and you have something to put in the README or the pull request.


_Last reviewed: 2026-09-22_
