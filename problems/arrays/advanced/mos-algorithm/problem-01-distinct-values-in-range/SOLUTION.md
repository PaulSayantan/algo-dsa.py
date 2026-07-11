# Distinct Values in a Range — Solution

## Brute Force

For each query independently, scan `a[l..r]` and count distinct values with a hash
set (or a per-query boolean array).

- Time: `O(q * n)` — with `n = 3*10^4` and `q = 2*10^5` that is `~6*10^9`, far too slow.
- Space: `O(n)` for the set per query.

A prefix-based idea (`answer[r] - answer[l-1]`) does **not** work for "distinct
count", because distinctness is not additive: a value present in both halves must be
counted once, and prefix sums cannot know about overlaps. This lack of a clean
`merge` is exactly the situation Mo's Algorithm is built for.

## Optimal Approach — Mo's Algorithm

Maintain a sliding window `[curL, curR]` together with:

- `cnt[v]` — how many times value `v` currently appears in the window,
- `distinct` — the current number of values with `cnt[v] > 0`.

Two `O(1)` primitives:

```
add(i):    if cnt[a[i]] == 0: distinct += 1
           cnt[a[i]] += 1
remove(i): cnt[a[i]] -= 1
           if cnt[a[i]] == 0: distinct -= 1
```

### Why it is correct

The window's `distinct` value is an *exact* function of which indices are inside the
window. `add`/`remove` change the multiset by exactly one element and keep both
`cnt` and `distinct` consistent by construction (the invariant "`distinct` = number
of `v` with `cnt[v] > 0`" is preserved at every step). Therefore, whenever the
window equals a query's `[l, r]`, `distinct` is that query's answer. Reordering
queries does not change any individual answer because the array is static; we simply
record each answer against its original index.

### Step by step

1. **Precompute block size** `B = max(1, int(n / sqrt(q)))` (using `n/√q` is optimal
   when `q` differs from `n`; plain `√n` is fine too).
2. **Sort queries** by `(l // B, r)`. Use the even/odd trick: for queries whose block
   index is even, sort by `r` ascending; for odd blocks, sort by `r` descending.
   This makes `r` sweep back and forth instead of jumping from the far right back to
   the left at every block boundary, roughly halving pointer movement.
3. **Initialize** `curL = 0`, `curR = -1` (empty window), `distinct = 0`.
4. **For each sorted query `(l, r, id)`** move the pointers in a "grow-first" order so
   the window is never invalid:
   ```
   while curR < r:  curR += 1; add(curR)
   while curL > l:  curL -= 1; add(curL)
   while curR > r:  remove(curR); curR -= 1
   while curL < l:  remove(curL); curL += 1
   ans[id] = distinct
   ```
5. **Output** `ans` in original order.

### Reference implementation

```python
from math import isqrt
from typing import List, Tuple


def distinct_in_ranges(a: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    n, q = len(a), len(queries)
    ans = [0] * q
    if n == 0 or q == 0:
        return ans

    block = max(1, int(n / max(1, isqrt(q))))  # n / sqrt(q)

    order = sorted(
        range(q),
        key=lambda i: (
            queries[i][0] // block,
            queries[i][1] if (queries[i][0] // block) % 2 == 0 else -queries[i][1],
        ),
    )

    max_val = max(a) + 1
    cnt = [0] * max_val
    distinct = 0
    curL, curR = 0, -1

    def add(i: int) -> None:
        nonlocal distinct
        v = a[i]
        if cnt[v] == 0:
            distinct += 1
        cnt[v] += 1

    def remove(i: int) -> None:
        nonlocal distinct
        v = a[i]
        cnt[v] -= 1
        if cnt[v] == 0:
            distinct -= 1

    for i in order:
        l, r = queries[i]
        while curR < r:
            curR += 1
            add(curR)
        while curL > l:
            curL -= 1
            add(curL)
        while curR > r:
            remove(curR)
            curR -= 1
        while curL < l:
            remove(curL)
            curL += 1
        ans[i] = distinct
    return ans
```

For large value domains (`a[i]` up to `10^6` but few distinct), compress coordinates
first or use a dict instead of a list for `cnt`.

### Complexity

- Sorting: `O(q log q)`.
- Pointer movement: `O((n + q) * √n)` total `add`/`remove` calls, each `O(1)`.
- Overall: `O((n + q) * √n)`. Space: `O(n + q + V)` where `V` is the value range.

## Key Insights & Edge Cases

- **The correct pointer order matters.** Grow both ends *before* shrinking so `curL`
  never exceeds `curR + 1`. A naive order can produce a temporarily invalid window
  and negative counts.
- **`curL = 0, curR = -1` means an empty window.** The first `add` is index 0.
- **Even/odd `r` sorting** is a constant-factor optimization, not a correctness
  requirement — but it is the difference between AC and TLE on tight limits.
- **Block size.** `√n` is the textbook choice; `n/√q` is provably better when
  `q ≪ n`. Never let it be `0` — clamp with `max(1, ...)`.
- **Single-element query** (`l == r`) yields `1` distinct value — the window has
  exactly one element after the pointers converge.
- **Large `a[i]`** (up to `10^6`) — a plain `cnt` list of that size is acceptable in
  memory; otherwise compress values to `[0, #distinct)` first.
- Mo's is **offline only** here: it must see all queries up front. If updates were
  interleaved you would need "Mo's with updates" (`O(n^{2/3})` per operation).
