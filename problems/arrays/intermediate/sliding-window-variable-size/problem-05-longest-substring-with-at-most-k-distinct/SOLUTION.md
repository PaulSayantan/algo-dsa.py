# Solution — Longest Substring with At Most K Distinct Characters

## Brute Force

For each start `l`, extend `r` while the count of distinct characters in
`s[l..r]` stays `<= k`; track the longest window.

```python
def lengthOfLongestSubstringKDistinct(s, k):
    n = len(s)
    best = 0
    for l in range(n):
        seen = set()
        for r in range(l, n):
            seen.add(s[r])
            if len(seen) > k:
                break
            best = max(best, r - l + 1)
    return best
```

- **Time:** `O(n^2)`.
- **Space:** `O(k)` for the set.

## Optimal Approach (Sliding Window, variable size)

Identical shape to "Fruit Into Baskets," just with a parameter `k` instead of the
constant `2`. Maintain a `count` map from character to its frequency inside the
window; `len(count)` is the number of distinct characters currently in the window.

**Algorithm (longest-window flavor):**

1. Handle `k == 0` up front: no characters allowed, answer is `0`.
2. Keep `left = 0` and an empty `count` map.
3. For each `right`, increment `count[s[right]]` (grow the window).
4. **While** `len(count) > k`, decrement `count[s[left]]`; if it reaches `0`,
   delete the key; then advance `left` (shrink).
5. The window `[left, right]` now has `<= k` distinct characters; update
   `best = max(best, right - left + 1)`.

```python
from collections import defaultdict

def lengthOfLongestSubstringKDistinct(s, k):
    if k == 0:
        return 0
    count = defaultdict(int)
    left = 0
    best = 0
    for right, c in enumerate(s):
        count[c] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
```

**Why it is correct.** The invariant is "the window holds at most `k` distinct
characters." Each new character raises the distinct count by at most 1 (to `k+1`);
the `while` loop evicts from the left exactly until some character's frequency
falls to `0` and its key is removed, bringing the distinct count back to `k`. That
is the smallest shrink that restores validity, so the window is the widest valid
one ending at each `right`.

**Trace of Example 1** (`s = "eceba"`, `k = 2`):

| right | c | count after add | shrink? | window `[l,r]` | length | best |
|------:|---|-----------------|---------|----------------|-------:|-----:|
| 0 | e | {e:1} | no | [0,0] | 1 | 1 |
| 1 | c | {e:1, c:1} | no | [0,1] | 2 | 2 |
| 2 | e | {e:2, c:1} | no | [0,2] | 3 | 3 |
| 3 | b | {e:2, c:1, b:1} | yes -> drop idx0 e -> {e:1,c:1,b:1} still 3 -> drop idx1 c -> {e:1,b:1}, l=2 | [2,3] | 2 | 3 |
| 4 | a | {e:1, b:1, a:1} | yes -> drop idx2 e -> {b:1,a:1}, l=3 | [3,4] | 2 | 3 |

Result: `3`.

- **Time:** `O(n)` — each character is inserted once and removed at most once; map
  operations are `O(1)` on average.
- **Space:** `O(k)` — the map holds at most `k + 1` keys during a shrink.

## Key Insights & Edge Cases

- **`k == 0`** must return `0` (no character can be included). The explicit guard
  avoids `len(count) > 0` shrinking the window to nothing and mis-handling.
- **`k >= number of distinct chars in `s`** means the whole string qualifies.
- Deleting a key when its count hits `0` is what keeps `len(count)` an accurate
  distinct-count — the single most common bug in this pattern.
- Setting `k = 2` recovers Problem 4; the two problems share one implementation.
