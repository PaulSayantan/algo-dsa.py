# Solution — XOR and Favorite Number

## Brute Force

For each query, enumerate every subarray of `a[l..r]` and test its XOR.

```python
def brute(a, k, queries):
    out = []
    for l, r in queries:            # 1-indexed inclusive
        cnt = 0
        for i in range(l - 1, r):
            x = 0
            for j in range(i, r):
                x ^= a[j]
                if x == k:
                    cnt += 1
        out.append(cnt)
    return out
```

- **Time:** `O(q * n^2)` — with `n, q = 10^5` this is astronomically slow.
- **Space:** `O(1)` extra.

Even an `O(n)` scan per query (`O(q*n)`) is `10^10` and too slow. We need the
prefix-XOR reformulation plus Mo's.

## Optimal Approach — Prefix XOR + Mo's Algorithm

### Step 1: reformulate

Let `pre[0] = 0` and `pre[t] = a[1] XOR ... XOR a[t]`. The XOR of `a[i..j]` is
`pre[j] XOR pre[i-1]`. So counting subarrays of `a[l..r]` with XOR `= k` is the
same as counting **prefix-index pairs** `(x, y)` with `l-1 <= x < y <= r` and

```
pre[x] XOR pre[y] = k    ⟺    pre[y] = pre[x] XOR k.
```

Thus each query `(l, r)` becomes: "how many value-pairs equal to `(p, p XOR k)`
lie in the prefix window `[l-1, r]`?" — a Mo's-friendly window over the prefix
array of length `n + 1`.

### Step 2: incremental pair counting

Keep `cnt[value]` = number of times a prefix value appears in the current window,
and a running `answer`.

- **Add** prefix value `pv`: it pairs with every already-present value equal to
  `pv XOR k`. So `answer += cnt[pv XOR k]`, then `cnt[pv] += 1`.
- **Remove** prefix value `pv`: reverse the add. First `cnt[pv] -= 1`, then
  `answer -= cnt[pv XOR k]`.

The asymmetric ordering (increment *after* adding to the answer; decrement
*before* subtracting) is what makes `k = 0` correct: when `k = 0`,
`pv XOR k = pv`, and `cnt[pv]` must exclude the element being added/removed
itself so we never pair an element with itself.

Each op is `O(1)`, giving **`O((n + q) · sqrt(n))`** overall.

### Why it is correct

`answer` is maintained as the exact number of unordered pairs `(x, y)`, `x != y`,
inside the current prefix window with `pre[x] XOR pre[y] = k`. Every single
insertion/deletion adjusts `answer` by precisely the pairs created/destroyed with
the element being moved (and never counts an element against itself thanks to the
ordering). When `[curL, curR] == [l-1, r]`, `answer` equals the query result.

### Reference implementation

```python
from typing import List, Tuple


def xor_favorite_number(a: List[int], k: int,
                        queries: List[Tuple[int, int]]) -> List[int]:
    n = len(a)
    q = len(queries)
    if q == 0:
        return []

    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] ^ a[i - 1]

    m = n + 1                       # number of prefix indices (0..n)
    block = max(1, int(m / (q ** 0.5)))

    # window over prefix indices: query (l, r) -> [l-1, r]
    qs = [(l - 1, r) for (l, r) in queries]
    order = sorted(
        range(q),
        key=lambda t: (qs[t][0] // block,
                       qs[t][1] if (qs[t][0] // block) % 2 == 0 else -qs[t][1]),
    )

    max_pv = max(pre) if pre else 0
    size = 1
    while size <= (max_pv | k):
        size <<= 1                  # table big enough for every pv and pv^k
    cnt = [0] * size
    answer = 0
    ans = [0] * q
    cur_l, cur_r = 0, -1

    def add(i: int) -> None:
        nonlocal answer
        pv = pre[i]
        answer += cnt[pv ^ k]
        cnt[pv] += 1

    def remove(i: int) -> None:
        nonlocal answer
        pv = pre[i]
        cnt[pv] -= 1
        answer -= cnt[pv ^ k]

    for t in order:
        l, r = qs[t]
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
        ans[t] = answer
    return ans
```

## Key Insights & Edge Cases

- **The window is over prefix indices `0..n`, not over `a`'s indices.** Note the
  window for `(l, r)` is `[l-1, r]` (both endpoints are prefix indices), so the
  Mo's array effectively has `n + 1` positions.
- **`k = 0` special case:** `pv XOR 0 = pv`. The add-then-increment /
  decrement-then-subtract ordering guarantees an element is never paired with
  itself; getting this order wrong overcounts by exactly the window size.
- **Count-table size:** prefix values and `pv XOR k` are all `< 2^20` for
  `a[i], k <= 10^6`, so a table of size `2^20` (or the next power of two above
  `max(pre) | k`) covers every index safely.
- **64-bit answers:** worst case ~`10^10` pairs in one query, which overflows
  32-bit. Use `long long` in C++; Python is fine.
- **Even/odd `r` alternation** in the sort key is optional but roughly halves
  the right-pointer travel constant.
