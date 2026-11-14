# SnapFolda UCP MCP

MCP endpoint for the SnapFolda store. Shopify hosts it on the store's own domain.

| | |
|---|---|
| Endpoint | `https://snapfolda.com/api/ucp/mcp` |
| Transport | Streamable HTTP, POST only |
| Protocol | MCP `2025-06-18`, UCP `2026-08-25` |
| Server | `universal-commerce/0.1.0` |
| Auth | none at the HTTP layer; each tool call carries an agent profile |

This repository holds notes and a client example. The server runs on Shopify's platform, so questions about its behaviour belong to Shopify.

## Discovery

Two documents describe the endpoint:

- `https://snapfolda.com/.well-known/ucp` returns the UCP profile with the endpoint, capabilities, and the current `payment_handlers` list.
- `https://snapfolda.com/agents.md` is the store's guide for agents.

`GET` on the endpoint returns 404. Send JSON-RPC over `POST`.

## Tools

The server exposes 14 tools.

### Catalog

- `search_catalog` product search by natural language, filters, or both
- `lookup_catalog` resolve several product or variant GIDs in one call
- `get_product` product detail with variants, price, and stock

### Store

- `ask_business` answer questions about the store, its policies, and its services

### Cart and checkout

- `create_cart`, `get_cart`, `update_cart`, `cancel_cart`
- `create_checkout`, `get_checkout`, `update_checkout`, `complete_checkout`, `cancel_checkout`

### Orders

- `get_order`

`prompts/list` and `resources/list` appear in the server capabilities but return 422.

## Calling a tool

Every tool takes `meta.ucp-agent.profile`, a public JSON URL that describes your agent. Shopify fetches that URL before running the tool. If it cannot be fetched, or it has no `ucp.version`, the call fails with 422 and one of `profile_unreachable`, `profile_malformed`, or `version_unsupported`.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "search_catalog",
    "arguments": {
      "meta": {
        "ucp-agent": {
          "profile": "https://your-domain.example/.well-known/agent-profile.json"
        }
      },
      "catalog": {
        "query": "iPhone 18 Pro wallet case"
      }
    }
  }
}
```

Send `Content-Type: application/json` and `Accept: application/json, text/event-stream`. The reply is either JSON or an SSE stream, and both carry the same JSON-RPC message.

A catalog response has `products`, `pagination`, and `messages`. Prices are integers in ISO 4217 minor units with a separate currency code, so `{"amount": 3499, "currency": "USD"}` is $34.99.

## Limits

`payment_handlers` in the UCP profile is empty. `complete_checkout` needs the buyer to approve on the checkout page or through Shop Pay, so it is not an unattended payment path.

`agents.md` asks agents to identify themselves with Web Bot Auth and to honour `Retry-After` on 429.

The store has about 4,700 products, so catalog search can return large payloads. Page with `pagination.cursor`.

## Files

- `examples/python_client.py` connects, lists the tools, and runs one search
- `examples/curl.md` has copy-paste requests

## License

MIT for this repository. The service is Shopify's.
