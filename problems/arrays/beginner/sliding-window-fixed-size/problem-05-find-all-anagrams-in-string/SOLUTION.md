# Solution — Find All Anagrams in a String

## Brute Force

Let `m = len(p)`. For each start index `i` in `s`, take the length-`m` substring, build
its character-count table (or sort it), and compare against `p`.

```python
from collections import Counter
m = len(p)
target = Counter(p)
res = []
for i in range(len(s) - m + 1):
    if Counter(s[i:i + m]) == target:
        res.append(i)
return res
```

Building a fresh `Counter` for each of ~`n` windows costs O(m) each.

- **Time:** O(n·m)
- **Space:** O(1) — at most 26 distinct letters per table.

## Optimal Approach (Sliding Window, Fixed Size)

Maintain **one** count table for the current window and slide it. Two adjacent windows
differ by only one character in and one out, so the table update is O(1), and we compare
it to `p`'s table each step.

1. If `len(p) > len(s)`, return `[]`.
2. Build `need = Counter(p)` and `window = Counter(s[0..m-1])` where `m = len(p)`.
3. If `window == need`, record start index `0`.
4. For `right` from `m` to `n - 1` (let `left = right - m`):
   - Add entering char: `window[s[right]] += 1`.
   - Remove leaving char: decrement `window[s[left]]`, deleting the key if it hits `0`
     (so equality comparison ignores absent letters).
   - If `window == need`, record start index `left + 1`.
5. Return the recorded indices.

```python
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(p), len(s)
        if m > n:
            return []
        need = Counter(p)
        window = Counter(s[:m])
        res = [0] if window == need else []
        for right in range(m, n):
            window[s[right]] += 1
            left_char = s[right - m]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if window == need:
                res.append(right - m + 1)
        return res
```

**Why it is correct:** A substring is an anagram of `p` iff it has the identical
character multiset, i.e. `window == need`. The window always represents exactly the
current length-`m` substring because each entering char is added and each leaving char
removed. Deleting zero-count keys keeps `window` a canonical multiset so `==` is a true
multiset comparison. Every length-`m` window is checked once.

**Step by step** on `s = "cbaebabacd", p = "abc"` (`m = 3`, `need = {a:1,b:1,c:1}`):

1. First window `"cba"` → `{c:1,b:1,a:1}` == need → record `0`.
2. `right=3` (`e` in, `c` out): window `"bae"` = `{b:1,a:1,e:1}` ≠ need.
3. `right=4` (`b` in, `b` out): window `"aeb"` = `{a:1,e:1,b:1}` ≠ need.
4. ... windows `"eba"`, `"bab"`, `"aba"` all differ ...
5. `right=8` (`c` in, `a` out): window `"bac"` = `{b:1,a:1,c:1}` == need → record `6`.

Answer: `[0, 6]`.

## Key Insights & Edge Cases

- **`p` longer than `s`:** no window exists — return `[]` immediately.
- **Delete zero counts** (or use a fixed 26-length array and compare arrays). If you
  leave `letter: 0` entries in the dict, `window == need` will fail even for true
  anagrams. Using a length-26 array of counts avoids this pitfall entirely and makes
  each comparison a fixed O(26) = O(1).
- **Complexity:** O(n) slides, each with an O(1)/O(26) update and comparison, giving
  O(n) overall with O(1) extra space (bounded alphabet).
- **Overlapping matches are allowed** (Example 2 returns `0`, `1`, `2`), which the
  index-by-index sliding naturally captures.
