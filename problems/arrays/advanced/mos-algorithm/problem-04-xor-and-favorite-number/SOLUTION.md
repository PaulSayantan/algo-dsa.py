# XOR and Favorite Number — Solution

## Brute Force

For each query, enumerate every subarray of `a[l..r]`, track its running XOR, and
count those equal to `k`.

- Time: `O(q * len²)`, up to `O(q * n²)` — with `n = q = 10^5` this is astronomically
  slow.
- Space: `O(1)` extra per query.

## Optimal Approach — Mo's Algorithm on prefix XORs

### The reduction

Define prefix XOR `P[0] = 0` and `P[t] = a[0] ⊕ a[1] ⊕ ... ⊕ a[t-1]`. Then for a
0-indexed inclusive subarray `a[i..j]`:

```
a[i] ⊕ ... ⊕ a[j] = P[i] ⊕ P[j+1]
```

So `a[i..j] = k` **iff** `P[i] ⊕ P[j+1] = k`, i.e. `P[j+1] = P[i] ⊕ k`.

Counting subarrays with XOR `k` inside `a[l..r]` is therefore counting **pairs of
prefix indices** `(i, j+1)` with `l <= i <= j+1 <= r+1` whose values XOR to `k`. That
is exactly a query over the **prefix window** of `P` from index `l` to index `r+1`
(inclusive on both ends). We run Mo's Algorithm over these prefix indices.

### Maintaining the window

Keep a frequency array `freq[v]` = how many prefix values equal `v` are in the
current window, and `cur` = number of unordered pairs currently XOR-ing to `k`.

```
add(idx):    p = P[idx]
             cur += freq[p ^ k]     # pair p with every already-present partner
             freq[p] += 1

remove(idx): p = P[idx]
             freq[p] -= 1           # remove p first...
             cur -= freq[p ^ k]     # ...then discount its pairs with remaining partners
```

The **order of operations differs between add and remove**: on add, count partners
*before* inserting `p` (so we do not pair `p` with itself); on remove, delete `p`
*before* subtracting (same reason). This correctly handles the `k = 0` case, where
`p ^ k == p` and a value would otherwise be paired with itself.

### Why it is correct

`cur` equals the number of pairs `{x, y}` in the window with `P[x] ⊕ P[y] = k`. When
we add index `idx`, the new pairs created are exactly those between `p = P[idx]` and
every partner already in the window whose value is `p ⊕ k` — there are `freq[p ⊕ k]`
of them, which is what we add. Removal is the exact inverse. So the invariant holds
after every step, and when the window equals `[l, r+1]` the value `cur` is the
query's answer. The array and prefix values are static, so reordering queries is
safe.

### Reference implementation

```python
from math import isqrt
from typing import List, Tuple


def xor_favorite_number(a: List[int], k: int, queries: List[Tuple[int, int]]) -> List[int]:
    n, q = len(a), len(queries)
    ans = [0] * q
    if n == 0 or q == 0:
        return ans

    P = [0] * (n + 1)
    for i in range(n):
        P[i + 1] = P[i] ^ a[i]

    # Each a-query [l, r] (0-indexed inclusive) -> prefix window [l, r+1] inclusive.
    qs = [(l, r + 1) for (l, r) in queries]
    m = n + 1
    block = max(1, int(m / max(1, isqrt(q))))
    order = sorted(
        range(q),
        key=lambda i: (
            qs[i][0] // block,
            qs[i][1] if (qs[i][0] // block) % 2 == 0 else -qs[i][1],
        ),
    )

    # freq indexed by prefix value; size = next power of two > all values so p^k stays in range.
    size = 1 << max(max(P), k).bit_length()
    if size == 0:
        size = 1
    freq = [0] * size
    cur = 0
    curL, curR = 0, -1

    def add(idx: int) -> None:
        nonlocal cur
        p = P[idx]
        cur += freq[p ^ k]
        freq[p] += 1

    def remove(idx: int) -> None:
        nonlocal cur
        p = P[idx]
        freq[p] -= 1
        cur -= freq[p ^ k]

    for i in order:
        l, r = qs[i]
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
        ans[i] = cur
    return ans
```

### Complexity

- Building prefix XOR: `O(n)`. Sorting: `O(q log q)`.
- Pointer movement over `n + 1` prefix indices: `O((n + q) * √n)` `O(1)` steps.
- Overall: `O((n + q) * √n)`. Space: `O(n + q + V)` where `V` is the value-domain
  size (bounded by the next power of two above `max prefix / k`, `< 2^20` here).

## Key Insights & Edge Cases

- **The `±1` index shift is the whole trick.** A subarray query on `a[l..r]` maps to
  a *prefix* window `[l, r+1]` that is one longer. Getting this boundary right is the
  most common bug.
- **`k = 0`.** Then `p ⊕ k == p`, so an element could pair with itself. The add/remove
  ordering (count-before-insert, delete-before-count) prevents self-pairing and gives
  the correct "pairs of equal prefix values" count.
- **freq array sizing.** `p ⊕ k` can exceed `max(P)`. Size `freq` to a power of two
  strictly greater than every value so no XOR index goes out of bounds (or use a
  dict).
- **64-bit answers.** A window can contain up to `~10^5` pairs per prefix value; the
  total count exceeds 32 bits. Python is fine; C++ needs `long long`.
- **Single-element query** `(l, l)` maps to prefix window `[l, l+1]` (two indices);
  the answer is `1` iff `a[l] == k`.
- Offline & static, as always for plain Mo's.
