# Solution — Sort Fixed-Length Strings

## Brute Force

Compare strings directly with an `O(n log n)` comparison sort. Each comparison
costs up to `O(L)` character comparisons, so the total is `O(L · n log n)`.
Correct, but not optimal for a fixed, small alphabet.

- **Time:** `O(L · n log n)`
- **Space:** `O(n)` (or `O(log n)` extra for an in-place comparison sort)

## Optimal Approach (LSD Radix Sort)

Because a lexicographic comparison gives the **leftmost** character the most
weight, the leftmost column is the *most significant digit* and the rightmost
column is the *least significant digit*. LSD radix sort processes least
significant first, so we iterate columns from `L - 1` down to `0`, running a
**stable counting sort** on each column over the 26-letter alphabet.

```python
def sort_fixed_length_strings(words):
    if len(words) <= 1:
        return list(words)
    L = len(words[0])
    A = 26
    arr = list(words)
    for pos in range(L - 1, -1, -1):          # least significant column first
        count = [0] * (A + 1)
        for w in arr:
            count[ord(w[pos]) - ord('a') + 1] += 1
        for c in range(1, A + 1):              # prefix sums -> start offsets
            count[c] += count[c - 1]
        output = [None] * len(arr)
        for w in arr:                          # forward scan + start offsets = stable
            idx = ord(w[pos]) - ord('a')
            output[count[idx]] = w
            count[idx] += 1
        arr = output
    return arr
```

### Why it is correct

- **Stability of each pass:** using prefix sums as *start offsets* and scanning
  the array left to right places equal-column characters in their existing
  relative order. (The reverse-scan / end-offset formulation is equally valid;
  the important thing is that exactly one of the two conventions is used
  consistently so each pass is stable.)
- **Correctness across passes:** after sorting by column `pos`, ties on that
  column keep the order from the previous pass (which sorted the less
  significant, more-to-the-right columns). By induction, once we finish column
  `0` the strings are ordered by the full key, which is exactly lexicographic
  order for equal-length strings.

### Complexity

- **Time:** `O(L · (n + A))` with `A = 26`. Since `A` is a constant and `L <= 50`,
  this is effectively `O(L · n)`.
- **Space:** `O(n + A)` for the output buffer and count array.

## Key Insights & Edge Cases

- **Column direction matters:** you must go right-to-left for LSD radix sort.
  Left-to-right would require the recursive MSD variant instead.
- **Equal lengths are essential** for this simple LSD form. If lengths differed,
  you would pad shorter strings with a sentinel that sorts before `'a'` (so
  `"ab"` < `"abc"`), or switch to MSD radix sort.
- **Single element / empty list:** return as-is; the loop body would be a no-op.
- **Duplicates:** preserved and grouped, thanks to stability.
- **Alphabet size:** widen `A` (e.g. 128 or 256) to support other character
  sets; the algorithm is unchanged.
