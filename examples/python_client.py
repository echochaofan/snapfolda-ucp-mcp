#!/usr/bin/env python3
"""Minimal client for the SnapFolda UCP MCP endpoint.

Usage:
    python python_client.py "iPhone 18 Pro wallet case"

Set PROFILE to a JSON URL that Shopify can fetch. The store's own UCP profile
works for experiments; real agents should publish their own.
"""

import json
import sys
import urllib.request

ENDPOINT = "https://snapfolda.com/api/ucp/mcp"
PROFILE = "https://snapfolda.com/.well-known/ucp"
PROTOCOL = "2025-06-18"


def call(payload):
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode(),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "MCP-Protocol-Version": PROTOCOL,
            "User-Agent": "snapfolda-ucp-mcp-example/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read().decode("utf-8", "replace")
        content_type = resp.headers.get("Content-Type", "")

    if "text/event-stream" in content_type:
        events = [
            json.loads(line[5:].strip())
            for line in raw.splitlines()
            if line.startswith("data:") and line[5:].strip().startswith("{")
        ]
        return events[-1] if events else {}

    return json.loads(raw) if raw.strip() else {}


def main():
    init = call(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": PROTOCOL,
                "capabilities": {},
                "clientInfo": {"name": "snapfolda-example", "version": "1.0"},
            },
        }
    )
    print("server:", init["result"]["serverInfo"])

    listing = call({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
    print("tools:", len(listing["result"]["tools"]))

    query = sys.argv[1] if len(sys.argv) > 1 else "iPhone 18 Pro wallet case"
    result = call(
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "search_catalog",
                "arguments": {
                    "meta": {"ucp-agent": {"profile": PROFILE}},
                    "catalog": {"query": query},
                },
            },
        }
    )

    if "error" in result:
        raise SystemExit(f"error: {result['error']}")

    text = "".join(
        part.get("text", "")
        for part in result["result"]["content"]
        if part.get("type") == "text"
    )
    payload = json.loads(text)

    print("matches:", len(payload.get("products", [])))
    for item in payload.get("products", [])[:5]:
        print("-", item.get("title"))


if __name__ == "__main__":
    main()
