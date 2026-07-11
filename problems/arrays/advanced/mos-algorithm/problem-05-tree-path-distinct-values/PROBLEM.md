# Count Distinct Values on Tree Paths

**Difficulty:** Hard

**Source:** SPOJ COT2 — "Count on a tree II" (Mo's Algorithm on trees)

## Description

You are given a tree with `n` nodes (numbered `1..n`). Each node `i` carries a value
`val[i]`. You are given `q` queries; each query is a pair `(u, v)` and asks:

> How many **distinct** values appear on the unique simple path between node `u` and
> node `v` (both endpoints inclusive)?

The tree and node values never change, and all queries may be read before answering
(**offline**). Return the answer for each query in the original input order.

## Constraints

- `1 <= n <= 4 * 10^4`
- `1 <= q <= 10^5`
- `1 <= val[i] <= 10^9` (values can be large — compress them)
- The graph is a tree: `n - 1` edges, connected, no cycles.
- `1 <= u, v <= n` (`u` and `v` may be equal).

## Examples

Consider this tree (values in parentheses):

```
            1 (val 1)
           /        \
        2 (val 2)   3 (val 1)
       /       \
    4 (val 3)  5 (val 2)
```

### Example 1

```
Input:
  val = {1:1, 2:2, 3:1, 4:3, 5:2}
  queries = [(4, 5), (4, 3)]
Output:
  [2, 3]
```

**Explanation:**
- Path `4 → 5` visits nodes `4, 2, 5` with values `3, 2, 2` → distinct `{2, 3}` → `2`.
- Path `4 → 3` visits nodes `4, 2, 1, 3` with values `3, 2, 1, 1` → distinct
  `{1, 2, 3}` → `3`.

### Example 2

```
Input:
  val = {1:1, 2:2, 3:1, 4:3, 5:2}
  queries = [(1, 1), (2, 4)]
Output:
  [1, 2]
```

**Explanation:**
- Path `1 → 1` is the single node `1` with value `1` → `1` distinct value.
- Path `2 → 4` visits nodes `2, 4` with values `2, 3` → distinct `{2, 3}` → `2`.

## Hint

Flatten the tree with an **Euler tour** recording each node's entry (`st`) and exit
(`en`) time so that any root-to-node path corresponds to a contiguous range, then run
**Mo's Algorithm** on that Euler array. A node that appears **twice** in the current
window is "in then out" and should be treated as *absent*; use an LCA to stitch the
two subtrees of a path together, adding the LCA's value separately.
