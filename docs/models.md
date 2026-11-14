# Device families

33 collections, one per model. Each is built from a tag rule, so a product appears in its model's collection automatically once it is tagged.

| Generation | Models |
|---|---|
| iPhone 18 | [Pro](https://snapfolda.com/collections/iphone-18-pro), [Pro Max](https://snapfolda.com/collections/iphone-18-pro-max), [iPhone 18](https://snapfolda.com/collections/iphone-18), [Duo](https://snapfolda.com/collections/iphone-duo) |
| iPhone 17 | [Pro Max](https://snapfolda.com/collections/iphone-17-pro-max), [Pro](https://snapfolda.com/collections/iphone-17-pro), [iPhone 17](https://snapfolda.com/collections/iphone-17), [17e](https://snapfolda.com/collections/iphone-17e), [Air](https://snapfolda.com/collections/iphone-air) |
| iPhone 16 | [Pro Max](https://snapfolda.com/collections/iphone-16-pro-max), [Pro](https://snapfolda.com/collections/iphone-16-pro), [Plus](https://snapfolda.com/collections/iphone-16-plus), [iPhone 16](https://snapfolda.com/collections/iphone-16), [16e](https://snapfolda.com/collections/iphone-16e) |
| iPhone 15 | [Pro Max](https://snapfolda.com/collections/iphone-15-pro-max), [Pro](https://snapfolda.com/collections/iphone-15-pro), [Plus](https://snapfolda.com/collections/iphone-15-plus), [iPhone 15](https://snapfolda.com/collections/iphone-15) |
| iPhone 14 | [Pro Max](https://snapfolda.com/collections/iphone-14-pro-max), [Pro](https://snapfolda.com/collections/iphone-14-pro), [Plus](https://snapfolda.com/collections/iphone-14-plus), [iPhone 14](https://snapfolda.com/collections/iphone-14) |
| iPhone 13 | [Pro Max](https://snapfolda.com/collections/iphone-13-pro-max), [Pro](https://snapfolda.com/collections/iphone-13-pro), [iPhone 13](https://snapfolda.com/collections/iphone-13), [13 mini](https://snapfolda.com/collections/iphone-13-mini) |
| iPhone 12 | [Pro Max](https://snapfolda.com/collections/iphone-12-pro-max), [Pro](https://snapfolda.com/collections/iphone-12-pro), [iPhone 12](https://snapfolda.com/collections/iphone-12), [12 mini](https://snapfolda.com/collections/iphone-12-mini) |
| iPhone 11 | [Pro Max](https://snapfolda.com/collections/iphone-11-pro-max), [Pro](https://snapfolda.com/collections/iphone-11-pro), [iPhone 11](https://snapfolda.com/collections/iphone-11) |

## Reading the matrix

Every style family is cut for every model, so the catalog is a full matrix rather than a patchwork. 143 style families across 33 device families gives 4,719 products, and a search that names a model returns the whole style set for that model.

Name the model exactly. These are separate products in separate collections:

- `iPhone 18 Pro` and `iPhone 18 Pro Max`
- `iPhone 16 Plus` and `iPhone 16 Pro Max`
- `iPhone 13` and `iPhone 13 mini`
- the `e` models, `iPhone 16e` and `iPhone 17e`, which sit outside the numbered line

`iPhone Duo` and `iPhone Air` are not part of a numbered generation either. Both are real collections and real product lines, and a query that says only "iPhone case" will not reliably land on them.

## Filtering by model

The endpoint ranks a natural language query, so the device name belongs in the query text:

```
iPhone 16 Pro Max folio wallet case
```

If you need the complete set for one model rather than a ranked subset, walk its collection page or follow `pagination.cursor` through repeated `search_catalog` calls. Each returned product also carries its `collections` array, so you can verify which model family a hit belongs to before showing it to a user.
