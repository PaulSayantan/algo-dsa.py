# Solution — Longest Common Binary Prefix

Let `n = len(nums)` and `w = width`.

## Brute Force

Render every value as its `w`-bit left-zero-padded binary string
(`format(v, f"0{w}b")`) and take the longest common prefix of those `n` strings with the
LeetCode-14 vertical scan, then report its length.

```python
def longest_common_binary_prefix(nums, width):
    bins = [format(v, f"0{width}b") for v in nums]
    ref = bins[0]
    for j in range(width):                    # bit column j (MSB first)
        bit = ref[j]
        if any(b[j] != bit for b in bins):
            return j
    return width
```

**Time:** `O(n * w)` — build `n` strings of length `w`, then a column scan touching each
bit once (with early termination). **Space:** `O(n * w)` for the string forms.

This is a perfectly good, readable answer. Because all strings have equal length `w`,
there is no "short string" case to worry about — only bit mismatches stop the scan.

## Optimal Approach — Vertical Scan (and a closed form)

The string version above already runs in `O(n * w)` time. We can make it `O(n * w)` time
with `O(1)` extra space by comparing bits arithmetically instead of materializing
strings: for bit column `j` (0 = most significant), the bit of value `v` is
`(v >> (w - 1 - j)) & 1`.

```python
def longest_common_binary_prefix(nums, width):
    for j in range(width):                    # MSB-first columns
        shift = width - 1 - j
        bit = (nums[0] >> shift) & 1
        if any(((v >> shift) & 1) != bit for v in nums):
            return j                          # first differing column
    return width
```

**Why it is correct.** Reading bits from the most significant, the common prefix extends
exactly as long as every value shares the same bit in the current column. The first
column with any disagreement ends the prefix at length `j`; if no column disagrees, all
values are identical across all `w` bits and the prefix length is `w`.

**Closed form via XOR.** All values share a leading bit iff that bit is equal in the
minimum and maximum (equivalently, in every value). Let `lo = min(nums)`,
`hi = max(nums)`. The positions where the values can *possibly* differ are exactly the
set bits of `hi ^ lo` — and more strongly, any bit where some pair differs shows up in
`hi ^ lo` only if it is at or below the top differing bit. The number of shared leading
bits is:

```python
def longest_common_binary_prefix(nums, width):
    x = min(nums) ^ max(nums)                 # 0 iff all equal
    if x == 0:
        return width
    highest_diff = x.bit_length()             # position (1-indexed) of top set bit
    return width - highest_diff
```

`x = min ^ max` is 0 exactly when all values are equal (min == max). Otherwise
`x.bit_length()` gives the index (1-based from the LSB) of the highest bit where min and
max differ; every bit above it is identical in min and max, hence identical in *all*
values (any value lies between min and max, so it agrees on every leading bit those two
agree on). Those shared high bits number `width - x.bit_length()`.

**Step by step for Example 3** (`[5, 6, 7]`, `width = 4`): `lo = 5 = 0101`,
`hi = 7 = 0111`, `x = 0101 ^ 0111 = 0010`, `x.bit_length() = 2`, answer
`= 4 - 2 = 2`. Matches the column scan (`01` shared).

**Time:** `O(n)` for the min/max, `O(1)` for the arithmetic. **Space:** `O(1)`.

## Binary Search on Prefix Length

`shared(L) = ` "do all values agree on their top `L` bits?" is monotonic, so binary
search over `L in [0, w]`. Checking a candidate `L` means masking off the top `L` bits of
each value and testing they are all equal:

```python
def shared(nums, width, L):
    if L == 0:
        return True
    mask = ((1 << L) - 1) << (width - L)      # top L bits
    target = nums[0] & mask
    return all((v & mask) == target for v in nums)
```

`O(log w)` guesses, each an `O(n)` check -> `O(n * log w)`. This mirrors the general
binary-search-on-prefix-length pattern and is worthwhile when the check is vectorizable.

## Key Insights & Edge Cases

- **All equal:** `min == max`, so `x == 0` and the answer is the full `width` (also the
  scan finishes without a mismatch).
- **Differ at the MSB:** e.g. `[0, 15]` at width 4 -> answer `0`.
- **Single value:** trivially shares all `width` bits with itself.
- **Left zero-padding matters:** the shared *leading zeros* of small numbers count toward
  the prefix (that is why `[12, 13]` at width 8 gives 7, not just the bits within the
  significant portion).
- The XOR closed form is the fastest and cleanest, but the vertical scan is the direct
  application of the LCP technique and generalizes to non-uniform-length strings.
