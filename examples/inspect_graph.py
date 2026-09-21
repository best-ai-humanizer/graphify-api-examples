"""Print the shape of a graphify-out/graph.json without assuming its schema.

Usage: python3 examples/inspect_graph.py [path/to/graph.json]

The cited sources do not document the JSON structure, so this script reports
what is there (top-level keys, types, lengths) and leaves querying to you.
"""
import json
import sys
from pathlib import Path

path = Path(sys.argv[1] if len(sys.argv) > 1 else "graphify-out/graph.json")
if not path.exists():
    sys.exit(f"not found: {path} (run /graphify . in your assistant first)")

with path.open() as fh:
    data = json.load(fh)

print(f"file: {path} ({path.stat().st_size} bytes)")
print(f"top-level type: {type(data).__name__}")


def describe(value):
    if isinstance(value, list):
        inner = type(value[0]).__name__ if value else "empty"
        return f"list of {len(value)} ({inner})"
    if isinstance(value, dict):
        return f"dict with {len(value)} keys"
    return f"{type(value).__name__}: {str(value)[:60]}"


if isinstance(data, dict):
    for key, value in data.items():
        print(f"  {key}: {describe(value)}")
        # Show the keys of the first element so you know what to query on.
        if isinstance(value, list) and value and isinstance(value[0], dict):
            print(f"    first item keys: {sorted(value[0].keys())}")
elif isinstance(data, list):
    print(f"  {describe(data)}")
    if data and isinstance(data[0], dict):
        print(f"  first item keys: {sorted(data[0].keys())}")
