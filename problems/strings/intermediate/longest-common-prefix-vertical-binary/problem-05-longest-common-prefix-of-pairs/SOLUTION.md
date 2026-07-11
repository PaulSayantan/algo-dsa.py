# Solution — Find the Length of the Longest Common Prefix (LeetCode 3043)

Let `n = len(arr1)`, `m = len(arr2)`, and `D` = maximum number of digits (`<= 9`, since
values are `<= 10^8`).

## Brute Force

Try every pair `(x, y)`, convert both to digit strings, and take the vertical LCP length
of the two strings; keep the maximum.

```python
def lcp_len(a: str, b: str) -> int:
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i

class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        best = 0
        for x in arr1:
            sx = str(x)
            for y in arr2:
                best = max(best, lcp_len(sx, str(y)))
        return best
```

The inner `lcp_len` is the two-string vertical scan from Problem 1.

**Time:** `O(n * m * D)` — up to `2.5 * 10^9` character comparisons for the largest inputs,
which is **too slow** for the constraints. **Space:** `O(1)` extra.

## Optimal Approach — Prefix Set (digit-prefix LCP)

The pairwise scan repeats enormous work. Instead, **precompute the set of all
digit-prefixes** of the `arr1` numbers, then for each `arr2` number scan its own digit
prefixes from shortest to longest and record the longest one that appears in the set. A
prefix present in the set means *some* `arr1` number begins with those digits — exactly a
cross-pair common prefix.

```python
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for x in arr1:
            s = str(x)
            for j in range(1, len(s) + 1):     # all prefixes "1", "12", "123", ...
                prefixes.add(s[:j])

        best = 0
        for y in arr2:
            s = str(y)
            for j in range(1, len(s) + 1):     # extend the prefix one digit at a time
                if s[:j] in prefixes:
                    best = max(best, j)
                else:
                    break                      # if s[:j] absent, no longer prefix exists
        return best
```

**Why it is correct.** `prefixes` holds every string that is a prefix of at least one
`arr1` number. For a given `y`, `s[:j] in prefixes` is true exactly when some `x` in
`arr1` shares the first `j` digits with `y` — i.e. there is a pair with common prefix
length at least `j`. Scanning `j` upward, the membership predicate is **monotonic**: if
`s[:j]` is not a prefix of any `arr1` number, then no longer prefix `s[:j+1]` can be
either (a longer string that shares a prefix would require the shorter one to also be
present). So we can `break` at the first miss, and the last hit is the longest common
prefix achievable with `y`. Taking the max over all `y` gives the global answer.

**Step by step for Example 1** (`arr1 = [1, 10, 100]`, `arr2 = [1000]`):
- `prefixes = {"1", "10", "100"}` (from `1`, `10`, `100`).
- For `y = 1000` (`"1000"`): `"1"` in set (best=1), `"10"` in set (best=2), `"100"` in set
  (best=3), `"1000"` not in set -> break. Answer `3`.

**Time:** `O((n + m) * D)` — each number contributes `O(D)` prefixes/lookups, and hash-set
operations on strings of length `<= D` are `O(D)`. Well within limits. **Space:**
`O(n * D)` for the prefix set.

## Trie Alternative

Insert every `arr1` digit string into a **trie** (prefix tree), one node per digit. For
each `arr2` number, walk the trie digit by digit; the depth you reach before falling off
is the longest common prefix length with some `arr1` number. Same `O((n + m) * D)` time,
`O(n * D)` nodes, and it avoids building many substring keys (often faster and lower
constant-factor memory than the set of string prefixes). The trie walk is the vertical LCP
scan generalized to "prefix against a whole collection at once."

## Key Insights & Edge Cases

- **Digits, read left to right, are the comparison unit** — convert each integer to
  `str(...)` and compare character (digit) columns.
- **Monotonic membership enables the early `break`** in the `arr2` scan — this is the LCP
  monotonicity property that also underlies binary search on prefix length.
- **No common prefix anywhere:** returns `0` (e.g. all first digits differ).
- **Leading zeros never appear** because the inputs are positive integers with no leading
  zeros, so digit strings compare cleanly.
- **Do not brute-force all pairs** — the prefix-set/trie reduction is what turns an
  `O(n*m*D)` blowup into `O((n+m)*D)`.
- The longest possible answer is `9` digits (values `<= 10^8` have at most 9 digits).
