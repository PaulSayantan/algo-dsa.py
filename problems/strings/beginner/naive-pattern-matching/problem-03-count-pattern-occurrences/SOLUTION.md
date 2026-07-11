# Solution — Count Pattern Occurrences (Including Overlaps)

## Brute Force

Slice a window at every start index and compare it to the pattern with `==`.

```python
def count_occurrences(text, pattern):
    n, m = len(text), len(pattern)
    count = 0
    for start in range(n - m + 1):
        if text[start:start + m] == pattern:
            count += 1
    return count
```

- **Time:** `O(n · m)` — one `O(m)` slice + compare per alignment.
- **Space:** `O(m)` for each temporary slice.

> A tempting one-liner `text.count(pattern)` is **wrong** here: Python's `str.count`
> counts only *non-overlapping* occurrences, so `"aaaa".count("aa")` returns `2`, not
> `3`. That is exactly why we do the search ourselves.

## Optimal Approach (Naive Pattern Matching)

Slide the pattern across the text one index at a time. At each alignment compare
character by character, bailing out on the first mismatch. When an alignment matches
fully, increment the counter — and then still advance by just **one** position, because
overlapping matches must be counted.

```python
def count_occurrences(text: str, pattern: str) -> int:
    n, m = len(text), len(pattern)
    count = 0
    for start in range(n - m + 1):           # every valid alignment
        j = 0
        while j < m and text[start + j] == pattern[j]:
            j += 1
        if j == m:                           # full match at this start
            count += 1
    return count
```

**Why it is correct.** Every occurrence of `pattern` is uniquely identified by its
starting index `start` in `0 .. n - m`. The loop visits each such `start` exactly once,
tests whether all `m` characters match, and counts it when they do. Because the loop
increments `start` by one regardless of whether a match occurred, an occurrence that
overlaps the previous one (its start is only one or a few positions later) is still
visited and counted. No index is skipped, so the count is exact.

**Step-by-step** on `text = "aaaa"`, `pattern = "aa"` (`n = 4`, `m = 2`,
`start` in `0..2`):

| start | window | match? | count |
|-------|--------|--------|-------|
| 0 | `aa` | yes | 1 |
| 1 | `aa` | yes | 2 |
| 2 | `aa` | yes | 3 |

Result: `3`.

- **Time:** `O(n · m)` worst case (all-equal text and pattern), `O(n)` typical.
- **Space:** `O(1)` — just `count`, `start`, and `j`.

## Key Insights & Edge Cases

- **Slide by one, not by `m`.** Advancing by the pattern length would only count
  non-overlapping matches (and undercount cases like `"aaaa"`/`"aa"`).
- **`pattern` longer than `text`.** `range(n - m + 1)` is empty, so the function returns
  `0` with no special-casing.
- **Single-character pattern.** Reduces to "count how many times this character appears";
  the algorithm handles it naturally.
- **No match anywhere** returns `0`, as in Example 3.
- If you needed only *non-overlapping* counts, you would jump `start += m` after a match
  instead of `start += 1` — a one-line change that highlights how the sliding step
  encodes the overlap policy.
