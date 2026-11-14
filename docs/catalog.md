# Catalog

What the endpoint returns, in numbers. Figures below come from the store's own product feed, read on 2026-11-15.

| | |
|---|---|
| Products | 4,719 |
| Variants | 19,536 |
| Style families | 143 |
| Device families | 33 |
| Price range | $24.99 to $89.99 |

The catalog is a matrix. 143 style families, each cut for 33 device families, which gives 33 x 143 = 4,719 products.

## Product shape

- `title` reads `<style name> - <device> <product type>`, for example `Vasa Note - iPhone 18 Pro Max Folio Wallet Case`.
- `price_range` and `list_price_range` are integers in minor units with a separate currency. `list_price_range` is zero across the whole catalog, so there is no compare-at pricing and one price per style.
- `variants` are colours. A product carries 1 to 8 of them: 4 is the most common, 5 next, and a handful of styles come in a single colour.
- `options` is a single `Color` option.
- `media` points at Shopify's CDN, one image per colour variant.
- `collections` carries the device family, for example `iphone-18-pro-max`.
- `tags` mix the device name, the colour names, the functional family, feature tags such as `RFID Blocking` or `Kickstand`, and a `case-group:<style>` marker.

Two fields surprise people:

`product.description` comes back empty. The copy sits on each variant instead, in `variants[].description.html`, and runs 60 to 260 characters. Read the variant if you need text about the product.

`categories` is a Shopify taxonomy reference (`gid://shopify/TaxonomyCategory/el-4-8-4-2`), not a human readable label. Do not render it as a category name.

## Functional families

The store's `product_type` field holds 20 values, several of them synonyms. They collapse into seven functional families. Shares below are of variant rows, so they reflect how many colours each style ships in, not how many styles exist.

| Family | Share | Product types seen |
|---|---|---|
| Card and slim card holder | 41% | Card Case, Credit Card Case, MagSafe Card Case, Slim Wallet Phone Case |
| Folio and flip wallet | 23% | Folio Wallet Case, Book Wallet Case, Flip Wallet Case, Flip Wallet Cover |
| Magnetic flip and magnetic wallet | 13% | Magnetic Flip Case, Magnetic Wallet Case, Magnetic Wallet Phone Case |
| Card wallet case | 10% | Card Wallet Case, Case With Card Case |
| Detachable and removable wallet | 8% | Removable Wallet Case, Detachable Magnetic Wallet Phone Case |
| Crossbody and handbag | 3% | Crossbody Case, Handbag Case |
| MagSafe wallet | 1% | MagSafe Wallet Phone Case |

Browsable collections for the main families: [wallet-case](https://snapfolda.com/collections/wallet-case), [folio-flip](https://snapfolda.com/collections/folio-flip), [card-case](https://snapfolda.com/collections/card-case), [card-holder](https://snapfolda.com/collections/card-holder), [slim-wallet-case](https://snapfolda.com/collections/slim-wallet-case), [removable-wallet-case](https://snapfolda.com/collections/removable-wallet-case), [magnetic-flip-case](https://snapfolda.com/collections/magnetic-flip-case), [zipper-wallet-case](https://snapfolda.com/collections/zipper-wallet-case), [crossbody](https://snapfolda.com/collections/crossbody), [magsafe](https://snapfolda.com/collections/magsafe), [rfid-blocking](https://snapfolda.com/collections/rfid-blocking), [3-piece-wallet-set](https://snapfolda.com/collections/3-piece-wallet-set).

## Searching it

`catalog.query` is a natural language string. Put the device name and the functional intent in the same sentence and the relevance ranking does the rest:

```
iPhone 18 Pro Max wallet case for travel
```

That query returns 10 products from the iPhone 18 Pro Max family, mixed across folio, removable and magnetic wallets, priced $24.99 to $34.99. A full response is in `examples/search_catalog_sample.json`.

Results are paginated. `pagination.has_next_page` and `pagination.cursor` are on every response, and the cursor is opaque, so pass it back unchanged.
