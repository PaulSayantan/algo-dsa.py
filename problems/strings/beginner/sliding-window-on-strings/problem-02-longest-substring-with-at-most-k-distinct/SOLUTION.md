# Solution — Longest Substring with At Most K Distinct Characters

## Brute Force

Try every start index, extend to the right while the running set of distinct
characters stays `<= k`, and remember the longest length reached.

```python
def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            seen.add(s[j])
            if len(seen) > k:
                break
            best = max(best, j - i + 1)
    return best
```

- **Time:** O(n^2) — a start index and an extension index.
- **Space:** O(k) for the per-start `seen` set (at most `k + 1` characters
  before we break).

## Optimal Approach (Sliding Window)

Keep a window `[left, right]` and a hash map `count` from character to its
frequency *inside the window*. The number of distinct characters in the window
is simply `len(count)`. Extend `right` by one each step, incrementing the
entering character's count. Whenever `len(count) > k`, the window is invalid,
so shrink from the left: decrement `s[left]`'s count and delete the key when it
reaches zero, advancing `left`, until the window holds at most `k` distinct
characters again. After restoring validity, update the best length.

```python
def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    if k == 0:
        return 0
    count = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        count[ch] = count.get(ch, 0) + 1
        # Shrink until at most k distinct characters remain.
        while len(count) > k:
            left_ch = s[left]
            count[left_ch] -= 1
            if count[left_ch] == 0:
                del count[left_ch]
            left += 1
        best = max(best, right - left + 1)
    return best
```

### Why it is correct

The invariant maintained at the end of each iteration is "the window
`s[left..right]` has at most `k` distinct characters." Adding `s[right]` can
raise the distinct count by at most one; the `while` loop removes exactly
enough leftmost characters to restore the bound. Because "having at most `k`
distinct characters" is a *prefix-monotone* property — extending a window can
only increase (never decrease) its distinct count — for each fixed `right` the
smallest feasible `left` yields the longest valid window ending there, which is
exactly what the loop finds. `left` never moves backward, so the maximum over
all `right` is the global answer.

### Step-by-step on `"eceba", k = 2`

| right | ch | count map | distinct | action | window | best |
|---|---|---|---|---|---|---|
| 0 | e | `{e:1}` | 1 | ok | `e` | 1 |
| 1 | c | `{e:1,c:1}` | 2 | ok | `ec` | 2 |
| 2 | e | `{e:2,c:1}` | 2 | ok | `ece` | 3 |
| 3 | b | `{e:2,c:1,b:1}` | 3 | shrink: drop `e`(->1), still 3; drop `c`(del), left=2 | `eb` | 3 |
| 4 | a | `{e:1,b:1,a:1}` | 3 | shrink: drop `e`(del), left=3 | `ba` | 3 |

Result: `3`.

- **Time:** O(n) — each index enters the window once and leaves at most once.
- **Space:** O(k) — the map holds at most `k + 1` keys transiently.

## Key Insights & Edge Cases

- **`k == 0`:** no non-empty substring can have 0 distinct characters; return
  `0`. Handle it explicitly (or the loop naturally shrinks every window to
  empty, but the early return is clearer).
- **`k >= number of distinct chars in s`:** the whole string qualifies, so the
  answer is `len(s)` — the `while` loop simply never triggers.
- **Deleting zero-count keys is what keeps `len(count)` an accurate distinct
  count.** If you only decrement without deleting, `len(count)` overcounts and
  the window shrinks incorrectly.
- This is the general template behind LeetCode 159 (at most **2** distinct) and
  the "longest substring with at most k distinct" family — only `k` changes.
