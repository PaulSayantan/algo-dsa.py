# Little Elephant and Array — Solution

## Brute Force

For each query, build a frequency map of `a[l..r]` and count values `x` with
`freq[x] == x`.

- Time: `O(q * n)` — with `n = q = 10^5` that is `10^10`, far too slow.
- Space: `O(n)` per query.

There is no clean prefix/segment-tree decomposition either: "number of values whose
frequency equals themselves" is a nonlinear function of the frequency histogram and
does not merge across sub-ranges. This is a textbook fit for Mo's Algorithm.

## Optimal Approach — Mo's Algorithm

Maintain the sliding window `[curL, curR]` with:

- `cnt[v]` — occurrences of value `v` in the window,
- `answer` — number of values `v` currently satisfying `cnt[v] == v`.

The crucial observation is that when we change `cnt[v]` by `±1`, **only `v`** can
gain or lose the "`cnt == v`" property, so we can update `answer` in `O(1)` by
checking `v` before and after the change.

```
add(i):    v = a[i]
           if cnt[v] == v: answer -= 1      # v was matching, now it won't be
           cnt[v] += 1
           if cnt[v] == v: answer += 1      # v now matches

remove(i): v = a[i]
           if cnt[v] == v: answer -= 1
           cnt[v] -= 1
           if cnt[v] == v: answer += 1
```

### Why it is correct

`answer` is defined as `|{ v : cnt[v] == v }|`. A single `add`/`remove` changes
exactly one `cnt[v]`; every other value's membership in that set is untouched. By
subtracting `v`'s old contribution and adding its new contribution around the
`cnt[v]` change, `answer` stays exactly equal to the size of the set at every step.
Hence when the window equals a query's `[l, r]`, `answer` is that query's result.
Reordering queries is safe because the array is static.

### Value range reduction

`a[i]` can be up to `10^9`, but any value `v > n` can never occur `v` times in a
window of size `<= n`, so it can never contribute. Two clean options:

- **Coordinate-compress** the values to `[0, #distinct)` and store, alongside each
  compressed id, its *original* value so the `cnt[v] == v` test uses the real value.
- Or keep `cnt` in a dictionary keyed by the original value.

The compression version is fastest and keeps `cnt` a flat list.

### Reference implementation

```python
from math import isqrt
from typing import List, Tuple


def count_values_equal_frequency(a: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    n, q = len(a), len(queries)
    ans = [0] * q
    if n == 0 or q == 0:
        return ans

    # Compress values -> ids; remember the real value behind each id.
    uniq = sorted(set(a))
    comp = {v: i for i, v in enumerate(uniq)}
    ca = [comp[v] for v in a]
    real = uniq  # real[id] == original value

    block = max(1, int(n / max(1, isqrt(q))))
    order = sorted(
        range(q),
        key=lambda i: (
            queries[i][0] // block,
            queries[i][1] if (queries[i][0] // block) % 2 == 0 else -queries[i][1],
        ),
    )

    cnt = [0] * len(uniq)
    answer = 0
    curL, curR = 0, -1

    def add(i: int) -> None:
        nonlocal answer
        v = ca[i]
        if cnt[v] == real[v]:
            answer -= 1
        cnt[v] += 1
        if cnt[v] == real[v]:
            answer += 1

    def remove(i: int) -> None:
        nonlocal answer
        v = ca[i]
        if cnt[v] == real[v]:
            answer -= 1
        cnt[v] -= 1
        if cnt[v] == real[v]:
            answer += 1

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
        ans[i] = answer
    return ans
```

### Complexity

- Sorting: `O(q log q)`; compression: `O(n log n)`.
- Pointer movement: `O((n + q) * √n)`, each step `O(1)`.
- Overall: `O((n + q) * √n)`. Space: `O(n + q)`.

## Key Insights & Edge Cases

- **Only one value can flip per step.** That is what makes the `O(1)` update valid;
  do the "subtract old / add new" dance around *every* `cnt` change, both add and
  remove.
- **Compare against the real value, not the compressed id.** After compression the
  `cnt == value` test must use `real[id]`, never the id itself.
- **Values `> n` are harmless** once you compare against the real value — their
  `cnt` will never reach that value, so they never add to `answer`.
- **Empty-window init** `curL = 0, curR = -1`, `answer = 0`.
- **Single-element query**: value `v` has `cnt == 1`, so it counts iff `v == 1`.
  Check the examples: `(0,1)` on `[1,1]` gives `0` because `1` occurs twice.
- Same offline/static caveat as all Mo's problems: all queries must be known up
  front and the array must not change between them.
