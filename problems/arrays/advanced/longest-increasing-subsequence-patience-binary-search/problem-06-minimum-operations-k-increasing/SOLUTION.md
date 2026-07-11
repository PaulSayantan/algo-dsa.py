# Solution — Minimum Operations to Make the Array K-Increasing

## Decompose into k independent chains

The K-increasing condition `arr[i - k] <= arr[i]` only ever compares indices
that differ by a multiple of `k`. So indices with the same remainder `r = i
mod k` form one chain that must be non-decreasing **among themselves**, and
different chains never interact:

```
chain r = [ arr[r], arr[r + k], arr[r + 2k], ... ]   for r = 0 .. k-1
```

Every element belongs to exactly one chain, so the total answer is the sum,
over all `k` chains, of the minimum changes needed to make that chain
non-decreasing.

## The per-chain subproblem

**Minimum changes to make a sequence non-decreasing** (where a change can set
an element to any value) equals

```
len(chain) - LNDS(chain)
```

where `LNDS` is the **Longest Non-Decreasing Subsequence**. Intuition: keep a
longest non-decreasing subsequence untouched; every other element can be
rewritten to fit between its kept neighbors (values are unbounded positive
integers, so there is always room). You can never keep more than `LNDS`
elements, because the kept ones must themselves already be non-decreasing.

## Brute Force

For each chain, compute `LNDS` with the `O(m^2)` dynamic program (`m` = chain
length). Summed over all chains this is `O(n^2)` in the worst case (e.g.
`k = 1`, one chain of length `n`) — too slow for `n = 10^5`.

## Optimal Approach (patience LNDS per chain)

Compute each chain's `LNDS` with the `O(m log m)` patience / binary-search
method. Because it is **non-decreasing** (`<=` allowed), use the upper-bound
search `bisect_right` (not `bisect_left`, which is for strict increase).

For each chain, maintain `tails` where `tails[L]` is the smallest tail of a
non-decreasing subsequence of length `L + 1`. For each value `x`:

- `pos = bisect_right(tails, x)`.
- If `pos == len(tails)`, append `x`; else set `tails[pos] = x`.

`LNDS = len(tails)`; the chain contributes `len(chain) - len(tails)`
operations.

### Reference implementation

```python
import bisect

def kIncreasing(self, arr: List[int], k: int) -> int:
    total_ops = 0
    for r in range(k):
        tails = []
        length = 0
        for i in range(r, len(arr), k):     # walk chain r without building a new list
            x = arr[i]
            length += 1
            pos = bisect.bisect_right(tails, x)   # non-decreasing => upper bound
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
        total_ops += length - len(tails)
    return total_ops
```

### Why it is correct

- **Chain independence:** the only constraints are between indices `k` apart,
  which lie in the same residue class, so optimizing each chain separately is
  globally optimal.
- **`len - LNDS` is optimal per chain:** the kept elements must form a
  non-decreasing subsequence, so at most `LNDS` can stay; and exactly `LNDS`
  can stay because any non-kept element can be reassigned to a legal value
  (positive integers are unbounded, so a value between its surviving neighbors
  always exists). Hence min changes `= len - LNDS`.
- **`bisect_right` for non-decreasing:** equal values are allowed on the same
  chain, so an equal element should *extend* a run, which upper-bound
  insertion achieves.

### Complexity

- **Time:** `O(n log n)`. Across all chains the total number of processed
  elements is exactly `n`, and each does one `O(log m)` binary search.
- **Space:** `O(n)` worst case for the `tails` buffer (when `k = 1`).

## Key Insights & Edge Cases

- **`k = 1`** means the entire array must be non-decreasing — a single chain.
  Example 1 `[5,4,3,2,1]` has `LNDS = 1`, so `5 - 1 = 4` changes.
- **Non-decreasing, not strictly increasing** — the classic `bisect_right`
  vs `bisect_left` decision. Getting this wrong is the most common mistake.
- **Iterate chains by stride** (`range(r, n, k)`) instead of materializing `k`
  sublists to keep memory tidy, though building sublists is also fine.
- **Already K-increasing** → every chain is non-decreasing → `LNDS = len` for
  each → 0 operations (example 2).
- **`k >= n`** makes every chain length 0 or 1, which is trivially
  non-decreasing → answer 0.
