# Reverse String II — Solution

## Brute Force

Break the string into `2k`-sized chunks, and for each chunk reverse its first `k`
characters using Python slicing, then stitch the pieces back together.

```python
result = []
for i in range(0, len(s), 2 * k):
    chunk = s[i:i + 2 * k]
    result.append(chunk[:k][::-1] + chunk[k:])
return "".join(result)
```

- **Time:** O(n) overall — every character is copied a constant number of times.
- **Space:** O(n) — slices and the `result` list create new strings. Concise, but it
  leans on slicing rather than an explicit in-place reversal.

## Optimal Approach (Reverse In-Place)

Convert to a mutable character list and iterate the start index in steps of `2k`. At
each block, reverse the sub-range `[i, min(i + k, n) - 1]` with a two-pointer swap:

```python
def reverseStr(self, s: str, k: int) -> str:
    chars = list(s)
    n = len(chars)
    for start in range(0, n, 2 * k):
        left, right = start, min(start + k - 1, n - 1)
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    return "".join(chars)
```

**Why it is correct:** Stepping `start` by `2k` visits exactly one "reverse the first
`k`" region per `2k` window and skips the second half of each window (which must stay
put). The right pointer is clamped with `min(start + k - 1, n - 1)`, which
automatically handles the two tail cases:
- Fewer than `k` characters left: `right` clamps to `n - 1`, so the entire remainder is
  reversed.
- Between `k` and `2k` characters left: `right = start + k - 1`, so exactly `k`
  characters are reversed and the rest are left alone.

- **Time:** O(n) — the total number of swaps across all blocks is at most n/2.
- **Space:** O(1) extra beyond the character-list copy Python requires for a mutable
  string.

## Key Insights & Edge Cases

- **The `min(...)` clamp is what encodes both remainder rules** — no special-case
  branching is needed.
- **`k >= n`:** the single block reverses the whole string (first `k` clamped to `n`).
- **`k == 1`:** each single-character "reversal" is a no-op, so the string is returned
  unchanged, which matches the specification.
- **Off-by-one:** use `start + k - 1` (inclusive right index), not `start + k`; the
  latter would swap one character too far into the "keep" region.
