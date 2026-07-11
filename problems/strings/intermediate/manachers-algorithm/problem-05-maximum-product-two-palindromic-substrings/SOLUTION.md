# Maximum Product of Two Palindromic Substrings — Solution

## Brute Force

Enumerate all odd-length palindromic substrings, then try every non-overlapping
pair and track the maximum product of lengths.

- Collecting palindromes and pairing them is O(n^2) candidates with O(n) checks.
- **Time:** O(n^3) (or O(n^2) with a DP palindrome table, still too slow for
  n = 10^5). **Space:** O(n^2).

With `n` up to 100000 anything worse than roughly O(n log n) or O(n) will TLE.

## Optimal Approach (Manacher + prefix/suffix sweeps)

Split the choice at a boundary: the first palindrome ends at some index `i`, and
the second starts at `i + 1` or later. If we know, for every `i`:

- `left[i]`  = length of the longest odd palindrome contained in `s[0..i]`, and
- `right[i]` = length of the longest odd palindrome contained in `s[i..n-1]`,

then the answer is `max over i of left[i] * right[i+1]`. Both arrays are built from
Manacher's radii.

### Step 1 — Odd-palindrome radii (Manacher, odd variant)

Because we only need odd-length palindromes, use the direct odd-only Manacher that
avoids the `#` transform. `d1[c]` = radius so that the longest odd palindrome
centered at `c` has length `2 * d1[c] - 1` and spans `[c - d1[c] + 1, c + d1[c] - 1]`.

```python
d1 = [0] * n
l = 0
r = -1
for i in range(n):
    k = 1 if i > r else min(d1[l + r - i], r - i + 1)
    while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
        k += 1
    d1[i] = k
    if i + k - 1 > r:
        l, r = i - k + 1, i + k - 1
```

### Step 2 — Longest palindrome ending exactly at each index

For each center `c`, its longest palindrome ends at `c + d1[c] - 1`; record that
length there. Crucially, a palindrome ending at `i` with length `L` implies a
palindrome ending at `i - 1` with length `L - 2` (peel one character off each end).
Propagate this **right to left**:

```python
end_here = [0] * n
for c in range(n):
    end = c + d1[c] - 1
    end_here[end] = max(end_here[end], 2 * d1[c] - 1)
for i in range(n - 1, 0, -1):
    end_here[i - 1] = max(end_here[i - 1], end_here[i] - 2)
```

Then `left[i]` is a running max of `end_here` (best palindrome whose right endpoint
is at most `i`):

```python
left = end_here[:]
for i in range(1, n):
    left[i] = max(left[i], left[i - 1])
```

### Step 3 — Symmetric arrays for the right side

For each center, its longest palindrome starts at `c - d1[c] + 1`. A palindrome
starting at `i` with length `L` implies one starting at `i + 1` with length `L - 2`;
propagate **left to right**, then take a suffix running max:

```python
start_here = [0] * n
for c in range(n):
    start = c - d1[c] + 1
    start_here[start] = max(start_here[start], 2 * d1[c] - 1)
for i in range(0, n - 1):
    start_here[i + 1] = max(start_here[i + 1], start_here[i] - 2)
right = start_here[:]
for i in range(n - 2, -1, -1):
    right[i] = max(right[i], right[i + 1])
```

### Step 4 — Combine at every split

```python
ans = 0
for i in range(n - 1):
    ans = max(ans, left[i] * right[i + 1])
return ans
```

### Full reference implementation

```python
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        d1 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1

        end_here = [0] * n
        for c in range(n):
            end = c + d1[c] - 1
            end_here[end] = max(end_here[end], 2 * d1[c] - 1)
        for i in range(n - 1, 0, -1):
            end_here[i - 1] = max(end_here[i - 1], end_here[i] - 2)
        left = end_here[:]
        for i in range(1, n):
            left[i] = max(left[i], left[i - 1])

        start_here = [0] * n
        for c in range(n):
            start = c - d1[c] + 1
            start_here[start] = max(start_here[start], 2 * d1[c] - 1)
        for i in range(0, n - 1):
            start_here[i + 1] = max(start_here[i + 1], start_here[i] - 2)
        right = start_here[:]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i], right[i + 1])

        return max(left[i] * right[i + 1] for i in range(n - 1))
```

- **Time:** O(n) (Manacher plus a constant number of linear sweeps).
- **Space:** O(n).

### Why it is correct

Manacher gives the true maximal odd radius at every center, so `end_here` /
`start_here` capture every attainable palindrome length before the shrink step. The
shrink step (`-2` per index) is valid because trimming one matching character from
each end of an odd palindrome yields a shorter odd palindrome that ends/starts one
position inward, so every shorter length that fits under a boundary is represented.
The prefix/suffix running maxima then give the best palindrome fully on each side of
any split, and scanning all splits `i | i+1` covers every way to place two
non-overlapping substrings. Enforcing `right[i + 1]` (strictly after the split)
guarantees non-overlap.

## Key Insights & Edge Cases

- **The shrink step is the subtle part:** without propagating `L -> L - 2` in the
  correct direction (right-to-left for `end_here`, left-to-right for `start_here`),
  a long palindrome would not be counted as the shorter palindrome that actually
  fits within a boundary, producing wrong (too-large) products. This is exactly the
  bug to avoid.
- **Odd-only Manacher:** since the problem restricts to odd-length palindromes, the
  `d1` variant is cleaner than the `#`-transform; palindrome length is
  `2 * d1[c] - 1`.
- **Guaranteed answer >= 1:** two single characters at opposite ends are always
  valid, so the maximum product is at least 1 for `n >= 2` (e.g. `"aba"` -> 1).
- **Non-overlap:** pairing `left[i]` with `right[i + 1]` (not `right[i]`) ensures the
  two substrings occupy disjoint index ranges.
- **Large n (10^5):** the whole pipeline is linear, so it runs well within limits;
  products can reach ~(n/2)^2, so use 64-bit integers in fixed-width languages.
