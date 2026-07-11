# Solution — Distinct Elements in Range

## Brute Force

For each query, scan `a[l..r]` and count distinct values using a hash set.

```python
def brute(a, queries):
    out = []
    for l, r in queries:
        out.append(len(set(a[l:r + 1])))
    return out
```

- **Time:** `O(q * n)` — each of `q` queries scans up to `n` elements. With
  `n = 3*10^4` and `q = 2*10^5` this is ~`6*10^9` operations — too slow.
- **Space:** `O(n)` for the per-query set.

A prefix-sum / segment-tree "count distinct" is possible but requires the
*offline BIT* trick (sort by `r`, keep last occurrence). Mo's algorithm is the
most direct and generalizes to statistics that prefix sums cannot express.

## Optimal Approach — Mo's Algorithm (offline sqrt decomposition)

### Key operations

Maintain a window `[curL, curR]`, a frequency array `freq[value]`, and a running
counter `distinct`:

- `add(i)`: `freq[a[i]] += 1`; if it became `1`, `distinct += 1`.
- `remove(i)`: `freq[a[i]] -= 1`; if it became `0`, `distinct -= 1`.

Both are `O(1)`, so `f = O(1)`.

### Query ordering

Let `B = max(1, int(n / sqrt(q)))` (or `sqrt(n)`). Sort query indices by the key
`(l // B, r if (l // B) even else -r)`. The even/odd alternation of the `r` key
makes the right pointer sweep forward in even blocks and backward in odd blocks,
avoiding a full reset each block (a constant-factor win).

### Why it is correct

The window statistic is *exactly* determined by the multiset of elements
currently inside `[curL, curR]`. `add`/`remove` maintain `freq` and `distinct`
as the true invariant "`distinct` = number of values with `freq > 0` in the
current window". Since we always move `curL`/`curR` one step at a time to reach
each query's `[l, r]`, when the pointers match the query bounds, `distinct` is
the correct answer. Reordering does not change any answer because each answer is
recorded against its **original index**.

### Why it is fast

- **Right pointer:** within a fixed left-block, queries are sorted by `r`, so
  `curR` moves monotonically — `O(n)` per block, `O(n / B)` blocks → `O(n^2/B)`.
- **Left pointer:** stays inside one block of width `B` between consecutive
  queries → `O(B)` per query → `O(q*B)`.
- Total `O(n^2/B + q*B)`, minimized near `B = n/sqrt(q)` giving
  **`O((n + q) * sqrt(n))`**.

### Reference implementation

```python
from math import isqrt
from typing import List, Tuple


def distinct_in_ranges(a: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    n = len(a)
    q = len(queries)
    if q == 0:
        return []
    block = max(1, int(n / (q ** 0.5))) if q else isqrt(n) or 1

    order = sorted(
        range(q),
        key=lambda k: (queries[k][0] // block,
                       queries[k][1] if (queries[k][0] // block) % 2 == 0
                       else -queries[k][1]),
    )

    max_val = max(a) if a else 0
    freq = [0] * (max_val + 1)
    distinct = 0
    ans = [0] * q
    cur_l, cur_r = 0, -1   # empty window

    def add(i: int) -> None:
        nonlocal distinct
        freq[a[i]] += 1
        if freq[a[i]] == 1:
            distinct += 1

    def remove(i: int) -> None:
        nonlocal distinct
        freq[a[i]] -= 1
        if freq[a[i]] == 0:
            distinct -= 1

    for k in order:
        l, r = queries[k]
        while cur_r < r:
            cur_r += 1
            add(cur_r)
        while cur_l > l:
            cur_l -= 1
            add(cur_l)
        while cur_r > r:
            remove(cur_r)
            cur_r -= 1
        while cur_l < l:
            remove(cur_l)
            cur_l += 1
        ans[k] = distinct
    return ans
```

## Key Insights & Edge Cases

- **Pointer-move order matters.** Always *expand* before you *shrink*
  (grow `curR` up / `curL` down first, then contract). Shrinking first can make
  `curL > curR + 1` and momentarily produce a negative-width window with
  frequencies driven below zero. The order above (`cur_r` up, `cur_l` down,
  `cur_r` down, `cur_l` up) is a safe canonical sequence.
- **Empty initial window:** start `cur_l = 0`, `cur_r = -1` so the window is
  genuinely empty and `add(0)` is the first real insertion.
- **Value range:** values up to `10^6` fit in a direct frequency array; if values
  were unbounded you would coordinate-compress them first.
- **Duplicate handling:** the `0→1` / `1→0` transitions are precisely what make
  duplicates free — repeated values never double-count distinctness.
- **q = 0 or single-element ranges** are handled naturally (`l == r` just adds
  one element).
