# Most Beautiful Item for Each Query

**Difficulty:** Medium

**Source:** LeetCode 2070 (Most Beautiful Item for Each Query)

## Description

You are given a 2D array `items` where `items[i] = [price_i, beauty_i]` denotes
the price and beauty of the `i`-th item, respectively.

You are also given a 0-indexed integer array `queries`. For each `queries[j]`,
you want to determine the **maximum beauty** of an item whose price is **less
than or equal to** `queries[j]`. If no such item exists, then the answer to this
query is `0`.

Return an array `answer` of the same length as `queries` where `answer[j]` is the
answer to the `j`-th query.

Note that the queries are **not** sorted — you must return the answers in the
original query order.

## Constraints

- `1 <= items.length, queries.length <= 10^5`
- `items[i].length == 2`
- `1 <= price_i, beauty_i, queries[j] <= 10^9`

## Examples

### Example 1

```
Input:  items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
Output: [2,4,5,5,6,6]
```

Explanation:
- Query `1`: only item `[1,2]` has price `<= 1`. Max beauty = `2`.
- Query `2`: items `[1,2]`, `[2,4]` qualify. Max beauty = `4`.
- Query `3`: items with price `<= 3` are `[1,2],[2,4],[3,2],[3,5]`. Max beauty = `5`.
- Query `4`: same set as query `3` (no item has price `4`). Max beauty = `5`.
- Query `5`: item `[5,6]` now qualifies. Max beauty = `6`.
- Query `6`: all items qualify. Max beauty = `6`.

### Example 2

```
Input:  items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
Output: [4]
```

Explanation: All items have price `1 <= 1`, so every item qualifies. The largest
beauty among them is `4`.

### Example 3

```
Input:  items = [[10,1000]], queries = [5]
Output: [0]
```

Explanation: The only item costs `10`, which is greater than the query budget
`5`, so no item qualifies and the answer is `0`.

## Hint

Answering each query with a fresh linear scan is `O(n)` per query. Because the
answer for a larger budget always includes everything a smaller budget allowed,
consider **Offline Query Processing**: look at all queries first, sort items and
queries by price/budget, then sweep a single pointer while maintaining a running
maximum beauty. Remember to write each answer back to its original index.
