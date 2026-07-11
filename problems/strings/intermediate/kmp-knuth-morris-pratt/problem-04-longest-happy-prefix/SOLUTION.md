# Solution — Longest Happy Prefix

## Brute Force

Try every proper prefix length from longest to shortest and compare the prefix
of that length against the suffix of that length; return the first match.

```python
def longestPrefix(s):
    n = len(s)
    for L in range(n - 1, 0, -1):        # L = candidate length, proper => < n
        if s[:L] == s[n - L:]:
            return s[:L]
    return ""
```

- **Time:** `O(n^2)`. There are `n - 1` candidate lengths, and each prefix/suffix
  comparison is `O(L) = O(n)`. With `n` up to `10^5` this is `~10^10` operations
  in the worst case — too slow.
- **Space:** `O(n)` for the slices.

A rolling-hash approach can reach `O(n)` expected time, but it risks hash
collisions. KMP gives a clean, deterministic `O(n)`.

## Optimal Approach — KMP failure function

By definition, `lps[i]` is the length of the longest proper prefix of
`s[0..i]` that is also a suffix of `s[0..i]`. Evaluate it at the last index and
`lps[n-1]` is *exactly* the length of the longest happy prefix of the whole
string. The answer is then just `s[:lps[n-1]]`.

```python
def longestPrefix(s):
    n = len(s)
    lps = [0] * n
    k = 0                            # current longest prefix-suffix length
    for i in range(1, n):
        while k > 0 and s[i] != s[k]:
            k = lps[k - 1]           # fall back along shorter borders
        if s[i] == s[k]:
            k += 1
        lps[i] = k
    return s[:lps[n - 1]]
```

### Why it is correct

The LPS recurrence maintains the invariant that after processing index `i`,
`k = lps[i]` is the longest border (prefix = suffix) of `s[0..i]`. When we extend
to `i` and the characters `s[i]` and `s[k]` disagree, `lps[k-1]` gives the next
shorter border to try — and this chain of borders enumerates *all* prefix-suffix
matches in decreasing length. Hence at the end `lps[n-1]` is the single longest
proper border of the entire string, which is the definition of the happy prefix.

Trace `s = "ababab"`:

| i | s[i] | k after step | lps |
|---|------|--------------|-----|
| 0 | a    | 0            | 0   |
| 1 | b    | 0            | 0   |
| 2 | a    | 1            | 1   |
| 3 | b    | 2            | 2   |
| 4 | a    | 3            | 3   |
| 5 | b    | 4            | 4   |

`lps[5] = 4`, so the answer is `s[:4] = "abab"`. Correct.

### Complexity

- **Time:** **O(n)** — the amortized KMP bound; `k` increases at most `n` times
  and each `while` iteration decreases it.
- **Space:** **O(n)** for the LPS array (plus `O(n)` for the returned slice).

## Key Insights & Edge Cases

- **This problem *is* the failure function.** Recognizing that "longest proper
  prefix that is also a suffix" = `lps[n-1]` turns a Hard-tagged problem into two
  lines on top of the standard LPS build.
- **No happy prefix → `lps[n-1] = 0`**, and `s[:0] == ""`, so the empty-string
  case is handled automatically (e.g. `"abcde"`, or a single char `"a"`).
- **Proper prefix requirement** is baked in: the LPS never counts the whole
  substring as its own border, so the full string can never be returned.
- **Do not confuse with the longest prefix that is a suffix of some *other*
  string.** Here both prefix and suffix come from the same `s`, which is exactly
  what a self-referential LPS computes.
