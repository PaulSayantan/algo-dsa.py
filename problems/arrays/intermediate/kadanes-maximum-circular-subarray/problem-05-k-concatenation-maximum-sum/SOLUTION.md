# Solution — K-Concatenation Maximum Sum

## Brute Force

Physically build `arr` repeated `k` times and run ordinary Kadane
(empty-subarray allowed, floor at 0) on the length-`n·k` array.

```python
MOD = 10**9 + 7
big = arr * k
cur = best = 0
for x in big:
    cur = max(0, cur + x)
    best = max(best, cur)
return best % MOD
```

- **Time:** O(n·k) — proportional to the full concatenated length.
- **Space:** O(n·k) for the materialized array.

With `n` and `k` each up to 10^5, `n·k` can be 10^10 — far too slow and too
much memory. We must avoid ever materializing more than a couple of copies.

## Optimal Approach — Kadane on 2 Copies + `(k − 2)·total`

Think of the concatenation as `k` identical blocks. An optimal subarray falls
into one of these regimes, and the case split hinges on `total = sum(arr)`:

1. **Best inside a single copy (or spanning one boundary).** The best subarray
   that touches at most **two** adjacent copies is captured by running Kadane
   over `arr + arr` (two copies). Call it `two`. This already covers `k == 1`
   (use just `arr`) and any answer that does not benefit from repeating the
   middle.

2. **Middle copies add value only when `total > 0`.** If `sum(arr) > 0`, then
   the ideal subarray takes a good **suffix** of the first copy, then **every
   full middle copy** (there are `k - 2` of them, each contributing `total`),
   then a good **prefix** of the last copy. The suffix-plus-prefix join across
   a boundary is exactly what `two` (Kadane over two copies) measures, so:

   ```
   answer = two + (k - 2) * total        # when total > 0 and k >= 2
   ```

   If `total <= 0`, extra middle copies never help (they would only lower the
   sum, and the empty subarray floors us at 0), so `answer = two`.

```python
def kConcatenationMaxSum(arr, k):
    MOD = 10**9 + 7

    def kadane(seq):            # empty subarray allowed -> never below 0
        cur = best = 0
        for x in seq:
            cur = max(0, cur + x)
            best = max(best, cur)
        return best

    total = sum(arr)
    if k == 1:
        return kadane(arr) % MOD
    two = kadane(arr + arr)
    if total > 0:
        return (two + (k - 2) * total) % MOD
    return two % MOD
```

### Why two copies are enough

Any optimal subarray uses at most one *partial* copy on each end plus some
number of *whole* copies in the middle. The two-copy Kadane already sees every
possible "partial-suffix + partial-prefix" combination that straddles a
boundary (and every fully-internal subarray). The only thing two copies cannot
represent is the value of the **whole** middle copies — and that value is simply
`(k - 2) * total`, added in closed form. When `total <= 0`, no whole copy is
ever worth including, so `two` alone is optimal.

### Apply the modulo only at the end

`two` and `total` are bounded (`|two| <= n · 10^4`, `|total| <= n · 10^4`), and
`(k - 2) * total` fits comfortably in 64-bit range, so compute the full integer
answer first and take `% MOD` once. Taking the modulo mid-computation can turn a
`max` comparison wrong.

### Step by step on the examples

- `arr = [1, 2], k = 3`: `total = 3 > 0`, `two = kadane([1,2,1,2]) = 6`.
  Answer = `6 + (3 - 2) * 3 = 9` ✓.
- `arr = [1, -2, 1], k = 5`: `total = 0` (not `> 0`), `two = kadane([1,-2,1,1,-2,1]) = 2`.
  Answer = `2` ✓ (the join `...1 | 1...` across the boundary).
- `arr = [-1, -2], k = 7`: `total = -3`, `two = kadane([-1,-2,-1,-2]) = 0`
  (empty subarray wins). Answer = `0` ✓.

- **Time:** O(n) — Kadane over at most two copies plus a sum; independent of `k`.
- **Space:** O(n) to hold `arr + arr` (or O(1) if you index modulo `n` instead
  of materializing).

## Key Insights & Edge Cases

- **`total` sign drives everything.** Positive total => stack full middle
  copies via `(k - 2)·total`. Non-positive total => extra copies never help;
  the two-copy scan is the whole answer.
- **`k == 1`** must be handled separately — there is no boundary to cross, so
  run Kadane on a single copy.
- **Empty subarray allowed** means Kadane floors at `0`; an all-negative `arr`
  correctly yields `0` (Example 3).
- **Modulo timing:** apply `% MOD` only to the final result. Because the answer
  can be negative-free but large, a single final modulo is both correct and
  sufficient.
- **Connection to circular Kadane:** the "suffix + prefix across a copy
  boundary" is the same wrap-around join as the circular problem — here the
  wrap happens between adjacent copies, and `(k - 2)·total` accounts for the
  copies in between.
