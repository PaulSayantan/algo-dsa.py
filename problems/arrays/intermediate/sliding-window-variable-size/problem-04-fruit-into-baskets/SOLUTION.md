# Solution — Fruit Into Baskets

## Brute Force

For every start `l`, extend `r` while the set of distinct types in `fruits[l..r]`
stays `<= 2`; track the longest window.

```python
def totalFruit(fruits):
    n = len(fruits)
    best = 0
    for l in range(n):
        types = set()
        for r in range(l, n):
            types.add(fruits[r])
            if len(types) > 2:
                break
            best = max(best, r - l + 1)
    return best
```

- **Time:** `O(n^2)`.
- **Space:** `O(1)` (at most a few distinct types tracked).

## Optimal Approach (Sliding Window, variable size)

This is the "**at most 2 distinct**" special case of the general "at most `k`
distinct" window. Track a `count` map from fruit type to how many copies are
currently in the window; the number of keys is the number of distinct types.

**Algorithm (longest-window flavor):**

1. Keep `left = 0` and an empty `count` map.
2. For each `right`, increment `count[fruits[right]]` (grow the window).
3. **While** `len(count) > 2` (a 3rd type is present), decrement
   `count[fruits[left]]`; if it hits `0`, delete the key; then advance `left`
   (shrink).
4. The window `[left, right]` now has `<= 2` types; update
   `best = max(best, right - left + 1)`.

```python
from collections import defaultdict

def totalFruit(fruits):
    count = defaultdict(int)
    left = 0
    best = 0
    for right, f in enumerate(fruits):
        count[f] += 1
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
```

**Why it is correct.** The invariant "window has at most 2 distinct types" models
the two baskets exactly. When a third type enters, we evict from the left until
one of the existing types is exhausted (its count drops to 0 and the key is
removed), which is the minimal shrink that restores validity. Recording the width
at each valid `right` covers every candidate window.

**Trace of Example 3** (`fruits = [1,2,3,2,2]`):

| right | f | count after add | shrink? | window `[l,r]` | length | best |
|------:|--:|-----------------|---------|----------------|-------:|-----:|
| 0 | 1 | {1:1} | no | [0,0] | 1 | 1 |
| 1 | 2 | {1:1, 2:1} | no | [0,1] | 2 | 2 |
| 2 | 3 | {1:1, 2:1, 3:1} | yes -> drop idx0 (type 1) -> {2:1,3:1}, l=1 | [1,2] | 2 | 2 |
| 3 | 2 | {2:2, 3:1} | no | [1,3] | 3 | 3 |
| 4 | 2 | {2:3, 3:1} | no | [1,4] | 4 | 4 |

Result: `4`.

- **Time:** `O(n)` — each index is added once and removed at most once; map ops are
  `O(1)` on average.
- **Space:** `O(1)` — the map holds at most 3 keys at any moment (2 valid + 1 that
  triggers the shrink).

## Key Insights & Edge Cases

- **Single type / whole array valid:** if there are `<= 2` distinct types overall,
  the whole array is the answer.
- Deleting the key when its count reaches `0` is essential — otherwise `len(count)`
  overcounts distinct types and the window never shrinks correctly.
- Generalizes directly to "at most `k` distinct" by replacing `2` with `k` (see
  Problem 5).
- Because `fruits[i]` are small non-negative ints, a fixed-size array can replace
  the hash map with an explicit distinct-count counter for a constant-factor speedup.
