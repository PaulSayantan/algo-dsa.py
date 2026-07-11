# Versioned Range Sum (Time-Travel Array)

**Difficulty:** Medium

Source: Classic persistent-data-structures exercise (persistent array / "fully
persistent" segment tree; appears in many competitive-programming tutorials).

## Description

You are given an integer array `initial` of length `n`. This is **version 0**
of the array. You must then process a list of operations, where each operation
is one of the following two kinds:

- `("update", prev_version, index, value)` — take the array as it looked in
  version `prev_version`, set position `index` to `value`, and store the result
  as a **new version**. The new version's id is the next integer in creation
  order: the first update creates version `1`, the second creates version `2`,
  and so on. **The base version `prev_version` is left untouched** and can still
  be updated or queried later.
- `("query", version, l, r)` — return the sum of the elements from index `l` to
  index `r` (both inclusive) **as they appeared in `version`**.

Return a list containing the answer to every `query` operation, in the order the
queries appear.

Because updates can branch off *any* earlier version (not just the latest), the
history forms a tree of versions, not a single line — you truly need
persistence, not just an undo stack.

## Constraints

- `1 ≤ n ≤ 10^5`
- `-10^9 ≤ initial[i], value ≤ 10^9`
- `0 ≤ index < n`
- `0 ≤ l ≤ r < n`
- `1 ≤ number of operations ≤ 2 × 10^5`
- For every operation, `prev_version` / `version` refers to a version that has
  already been created (an id in `[0, current_max_version]`).

## Examples

### Example 1

```
Input:
  n = 5
  initial = [1, 2, 3, 4, 5]          # version 0
  operations = [
    ("query",  0, 0, 4),             # sum of version 0 over [0,4]
    ("update", 0, 2, 10),            # version 1 = [1,2,10,4,5]
    ("query",  1, 0, 4),             # sum of version 1 over [0,4]
    ("query",  0, 0, 4),             # version 0 is unchanged
  ]

Output: [15, 22, 15]
```

Explanation: Version 0 sums to `1+2+3+4+5 = 15`. Version 1 replaces `A[2]=3`
with `10`, giving `1+2+10+4+5 = 22`. The final query re-reads version 0, which
was never modified, so it is still `15`.

### Example 2

```
Input:
  n = 3
  initial = [5, 5, 5]                # version 0
  operations = [
    ("update", 0, 0, 1),             # version 1 = [1,5,5]
    ("update", 1, 2, 9),             # version 2 = [1,5,9]
    ("query",  2, 0, 2),             # sum of version 2
    ("query",  1, 0, 1),             # sum of version 1 over [0,1]
    ("query",  0, 1, 2),             # sum of version 0 over [1,2]
  ]

Output: [15, 6, 10]
```

Explanation: Version 2 is `[1,5,9]` → `1+5+9 = 15`. Version 1 is `[1,5,5]`, and
`[0,1]` sums to `1+5 = 6`. Version 0 is still `[5,5,5]`, and `[1,2]` sums to
`5+5 = 10`.

## Hint

Do not copy the whole array on each update — that costs `O(n)` per version. Use
a **Persistent Segment Tree**: an update rebuilds only the `O(log n)` nodes on
the root-to-leaf path and shares the rest with the parent version. Keep the root
of every version so any past version is queryable in `O(log n)`.
