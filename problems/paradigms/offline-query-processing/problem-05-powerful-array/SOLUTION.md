# Solution - Powerful Array

## Brute Force

For each query, count occurrences within the range and sum `count^2 * value`.

```python
from collections import Counter

def powerful_array(a, queries):
    ans = []
    for (l, r) in queries:
        c = Counter(a[l - 1:r])
        ans.append(sum(cnt * cnt * v for v, cnt in c.items()))
    return ans
```

- **Time:** `O(n * q)`. With `n = q = 2*10^5` that is `4*10^10` — far too slow.
- **Space:** `O(n)` for the per-query counter.

## Optimal Approach (Offline Query Processing — Mo's Algorithm)

The answer depends on the whole multiset of the range, so there is no simple
prefix decomposition. But there is a crucial local property: if we currently know
`power(l, r)` and the frequency table `cnt[]`, we can adjust the answer in `O(1)`
when we **add or remove one element at an endpoint**.

When a value `v` currently has count `c` and we add one more occurrence, its
contribution changes from `c^2 * v` to `(c+1)^2 * v`, a delta of
`((c+1)^2 - c^2) * v = (2c + 1) * v`. Removing an occurrence changes count `c` to
`c-1`, a delta of `((c-1)^2 - c^2) * v = -(2c - 1) * v`.

```python
add(pos):    cur += (2 * cnt[v] + 1) * v;  cnt[v] += 1     # v = a[pos]
remove(pos): cur -= (2 * cnt[v] - 1) * v;  cnt[v] -= 1
```

**Mo's algorithm** exploits this by ordering queries so that the two endpoints
`(curL, curR)` move as little as possible in total:

1. Pick a block size `B ≈ sqrt(n)`.
2. **Sort queries** by the key `(l // B, r)` — group by which block `l` falls in,
   and within a block by `r`.
3. Maintain a current window `[curL, curR]` and the running answer `cur`. For each
   query in sorted order, move `curR`/`curL` to the target `r`/`l` one step at a
   time, calling `add`/`remove` on each step.
4. Record `cur` at the query's original index.

```python
def powerful_array(a, queries):
    n = len(a)
    B = max(1, int(n ** 0.5))
    order = sorted(range(len(queries)),
                   key=lambda t: (queries[t][0] // B, queries[t][1]))
    cnt = [0] * (max(a) + 1)
    cur = 0

    def add(pos):
        nonlocal cur
        v = a[pos - 1]
        cur += (2 * cnt[v] + 1) * v
        cnt[v] += 1

    def remove(pos):
        nonlocal cur
        v = a[pos - 1]
        cur -= (2 * cnt[v] - 1) * v
        cnt[v] -= 1

    ans = [0] * len(queries)
    curL, curR = 1, 0                    # empty window
    for t in order:
        l, r = queries[t]
        while curR < r: curR += 1; add(curR)
        while curL > l: curL -= 1; add(curL)
        while curR > r: remove(curR); curR -= 1
        while curL < l: remove(curL); curL += 1
        ans[t] = cur
    return ans
```

### Why it is correct

`cur` always equals `power(curL, curR)` because every `add`/`remove` applies the
exact delta derived above, and the four `while` loops transform the window from
its previous `(curL, curR)` to the query's `(l, r)` by unit steps. The **order**
does not affect correctness — only speed — since each transition preserves the
invariant `cur == power(curL, curR)`. When the loops finish, `curL == l` and
`curR == r`, so `cur` is the requested power. Note the loop ordering (expand
before shrink) is chosen so the window is never inverted into an invalid state.

**Complexity of the ordering.** With queries sorted by `(l // B, r)`:

- Across all queries in one block, `r` only increases (queries are sorted by `r`
  within a block), so `curR` moves `O(n)` per block; with `n / B` blocks the total
  right-pointer movement is `O(n^2 / B)`.
- The left pointer stays within a block plus jumps between queries, costing
  `O(B)` per query, i.e. `O(q * B)` total.

Choosing `B = n / sqrt(q)` (or simply `B ≈ sqrt(n)`) balances these to
`O((n + q) * sqrt(n))` pointer moves, each `O(1)`.

### Step-by-step (Example 1)

`a = [1, 2, 1]`, `n = 3`, `B = 1`. Queries `(1,2)` and `(1,3)`.
Sort key `(l // 1, r)`: `(1,2)->(1,2)`, `(1,3)->(1,3)` — order stays `(1,2)`,
then `(1,3)`.

Start `curL=1, curR=0`, `cur=0`.

| query   | pointer moves                        | cnt after            | cur |
|---------|--------------------------------------|----------------------|-----|
| `(1,2)` | add r=1 (v1): +1; add r=2 (v2): +2   | {1:1, 2:1}           | 3   |
| `(1,3)` | add r=3 (v1): +(2*1+1)*1 = +3        | {1:2, 2:1}           | 6   |

Answers in original order: `[3, 6]`.

- **Time:** `O((n + q) * sqrt(n))` pointer moves plus `O(q log q)` to sort.
- **Space:** `O(n + q + V)` where `V = max value` for the frequency table (a hash
  map or coordinate compression avoids the `V` term when values are sparse).

## Key Insights & Edge Cases

- **`O(1)` incremental update is the prerequisite** for Mo's. If add/remove could
  not be done cheaply, Mo's would not help. The `(2c ± 1) * v` deltas are the
  telescoping difference of consecutive squares.
- **Block size trade-off.** `B ≈ sqrt(n)` is the standard choice; the tighter
  `B = n / sqrt(q)` minimizes moves when `q` differs a lot from `n`. Either gives
  the `sqrt` bound.
- **Even/odd `r` sorting optimization:** sorting `r` ascending in even blocks and
  descending in odd blocks (a "snake" order) roughly halves right-pointer travel
  and is a common constant-factor speedup.
- **Pointer-move ordering matters.** Do all *expansions* (`curR++`, `curL--`)
  before *shrinks* (`curR--`, `curL++`) so the window never becomes inverted
  (e.g. `curL > curR + 1`), which could make `cnt` go negative.
- **Large values:** with values up to `10^6`, a size-`(max+1)` array works;
  otherwise compress coordinates. Answers can exceed 32 bits, so use 64-bit
  integers (automatic in Python).
- **Mo's is inherently offline:** it must see all queries to sort them, and it
  cannot handle updates interleaved with queries (that needs the more advanced
  "Mo's with updates" / 3D variant).
