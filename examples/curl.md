# curl examples

The endpoint answers `POST` only.

## Initialize

```bash
curl -sS https://snapfolda.com/api/ucp/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"curl","version":"1"}}}'
```

Expected result: `serverInfo.name` is `universal-commerce`.

## List tools

```bash
curl -sS https://snapfolda.com/api/ucp/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
```

## Search the catalog

Replace the profile URL with a document Shopify can fetch.

```bash
curl -sS https://snapfolda.com/api/ucp/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
      "name": "search_catalog",
      "arguments": {
        "meta": {"ucp-agent": {"profile": "https://your-domain.example/.well-known/agent-profile.json"}},
        "catalog": {"query": "iPhone 18 Pro wallet case"}
      }
    }
  }'
```

## Ask about the store

```bash
curl -sS https://snapfolda.com/api/ucp/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{
    "jsonrpc": "2.0",
    "id": 4,
    "method": "tools/call",
    "params": {
      "name": "ask_business",
      "arguments": {
        "meta": {"ucp-agent": {"profile": "https://your-domain.example/.well-known/agent-profile.json"}},
        "ask": {"query": "What is your refund policy?"}
      }
    }
  }'
```

## Common errors

| Status | Code | Cause |
|---|---|---|
| 422 | `profile_unreachable` | Shopify could not fetch the profile URL |
| 422 | `profile_malformed` | The URL returned something that is not JSON |
| 422 | `version_unsupported` | The profile has no `ucp.version` |
| 404 | | The request used `GET` instead of `POST` |
