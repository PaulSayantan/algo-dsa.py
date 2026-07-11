# Solution — Count Distinct Palindromic Substrings

## Brute Force

Enumerate all `O(n²)` substrings, test each for the palindrome property, and add
palindromes to a set to deduplicate.

```python
def countDistinctPalindromes(s):
    seen = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j + 1]
            if sub == sub[::-1]:
                seen.add(sub)
    return len(seen)
```

- **Time:** `O(n³)` (verifying each of `O(n²)` substrings costs `O(n)`), plus
  the cost of hashing substrings.
- **Space:** `O(n²)` in the worst case for the set of distinct palindromes.

## Optimal Approach — Expand Around Center + Set

**Key idea.** We still need to *discover* every palindromic substring, and
expand-around-center does that in `O(n²)` total work instead of `O(n³)`. For
each of the `2n - 1` centers, every successful expansion step yields one
palindrome; we insert its string into a set so duplicates collapse.

```python
class Solution:
    def countDistinctPalindromes(self, s: str) -> int:
        n = len(s)
        seen: set[str] = set()

        def collect(left: int, right: int) -> None:
            while left >= 0 and right < n and s[left] == s[right]:
                seen.add(s[left:right + 1])
                left -= 1
                right += 1

        for i in range(n):
            collect(i, i)      # odd-length centers
            collect(i, i + 1)  # even-length centers

        return len(seen)
```

**Why it is correct.** Expand-around-center enumerates *all* palindromic
substrings (each has a unique center and is reached exactly once during that
center's expansion). Inserting each into a hash set removes duplicates by
content, so the final set size equals the count of distinct palindromes.

**Step by step on `s = "abaaa"`:**

| Center | Palindromes discovered |
|--------|------------------------|
| i=0 (`a`) | `"a"` |
| 0,1 | none (`a != b`) |
| i=1 (`b`) | `"b"` |
| 1,2 | none (`b != a`) |
| i=2 (`a`) | `"a"`, then `"aba"` |
| 2,3 | `"aa"` |
| i=3 (`a`) | `"a"`, then `"aaa"` |
| 3,4 | `"aa"` |
| i=4 (`a`) | `"a"` |

Distinct set = `{"a", "b", "aba", "aa", "aaa"}` → size `5`. ✅

- **Time:** `O(n²)` expansions, but each `seen.add(s[left:right+1])` builds a
  substring of length up to `O(n)`, giving `O(n³)` worst-case for the slicing/
  hashing. This still beats the naive `O(n³)` with a much smaller constant, and
  for the given constraints (`n ≤ 1000`) it runs comfortably.
- **Space:** `O(n²)` for stored distinct palindromes in the worst case.

> For a strict `O(n log n)` / `O(n)` distinct-palindrome count, use a
> **palindromic tree (eertree)**, whose node count equals the number of distinct
> palindromic substrings. Expand-around-center is the simplest correct approach
> and is ideal for interview-scale inputs.

## Key Insights & Edge Cases

- **Distinct vs. positional counting.** This is the deduplicated cousin of
  Problem 2. The only change to the expansion loop is `seen.add(...)` instead of
  `count += 1`.
- **The set collapses duplicates automatically**, so palindromes like `"aa"` and
  `"a"` appearing at multiple positions are stored once.
- **Slicing cost.** Adding the substring itself (not just its length) is what
  pushes the worst case toward `O(n³)`; for tighter bounds, hash incrementally or
  use an eertree.
- **Single character / all-distinct input** (`"abc"`) yields exactly `n` distinct
  palindromes (each single letter).
- **All-identical input** (`"aaaa"`) yields exactly `n` distinct palindromes
  (`"a"`, `"aa"`, ..., the whole string) — a good sanity check.
