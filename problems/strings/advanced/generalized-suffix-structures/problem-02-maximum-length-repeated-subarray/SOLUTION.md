# Maximum Length of Repeated Subarray — Solution

## Brute Force

For every pair of start indices `(i, j)` extend a match as long as
`nums1[i+l] == nums2[j+l]`, tracking the longest run. There are `O(m*n)` starting
pairs and each match extends up to `O(min(m, n))`, giving `O(m*n*min(m,n))` time
and `O(1)` extra space. For the LeetCode limits (`<= 1000` each) this is up to
`10^9` operations — too slow in the worst case.

- **Time:** `O(m * n * min(m, n))`.
- **Space:** `O(1)`.

## Optimal Approach (Generalized Suffix Structure)

There are two clean optimal solutions. The DP is the usual interview answer; the
generalized suffix structure is the technique this folder teaches and scales to
*more than two* arrays without change.

### The standard DP (baseline, `O(m*n)`)

Let `dp[i][j]` be the length of the common suffix of `nums1[:i]` and `nums2[:j]`.
Then `dp[i][j] = dp[i-1][j-1] + 1` when `nums1[i-1] == nums2[j-1]`, else `0`. The
answer is `max(dp)`. Time `O(m*n)`, space `O(min(m,n))` with a rolling row.

### Generalized suffix automaton approach

Treat each array as a string over the integer alphabet (each distinct value is a
symbol). Build **one** generalized suffix automaton over both arrays, and label
each state with which arrays occur there:

1. Insert `nums1` (string id `0`) and `nums2` (string id `1`) into the GSA,
   resetting `last = root` before each. After appending a character, OR the
   current string's bit into the returned state's **primary mask** — that state
   represents a substring that genuinely ends at this position in this string.
2. `endpos(v)` is the union of the `endpos` of `v`'s suffix-link children, so
   propagate masks **up the suffix-link tree**. Processing states in order of
   **decreasing `len`** visits every child before its parent (a child's longest
   substring is longer than its parent's), so a single pass `mask[link[v]] |=
   mask[v]` computes, for each state, the set of arrays whose occurrences reach
   it.
3. A state `v` with `mask[v] == 0b11` represents substrings occurring in **both**
   arrays; every such substring has length up to `len[v]`. The answer is the
   maximum `len[v]` over all states with both bits set (0 if none).

### Why it is correct

Every substring inside state `v` shares the same `endpos`, and that `endpos` — 
once masks are propagated — tells you exactly which source arrays contain the
substring. If both bits are set, the *longest* substring of that state (`len[v]`)
is common to both arrays and is a candidate answer; shorter substrings in the
same state can never beat it. Maximizing `len[v]` over "both-bit" states
therefore yields the longest common subarray.

### Reference implementation

```python
from collections import defaultdict

class GSA:
    def __init__(self):
        self.nxt = [dict()]; self.link = [-1]; self.length = [0]
    def _new(self, length, link, trans=None):
        self.nxt.append(dict(trans) if trans else dict())
        self.link.append(link); self.length.append(length)
        return len(self.nxt) - 1
    def extend(self, c, last):
        if c in self.nxt[last]:
            q = self.nxt[last][c]
            if self.length[last] + 1 == self.length[q]:
                return q
            clone = self._new(self.length[last] + 1, self.link[q], self.nxt[q])
            self.link[q] = clone; p = last
            while p != -1 and self.nxt[p].get(c) == q:
                self.nxt[p][c] = clone; p = self.link[p]
            return clone
        cur = self._new(self.length[last] + 1, -1); p = last
        while p != -1 and c not in self.nxt[p]:
            self.nxt[p][c] = cur; p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.nxt[p][c]
            if self.length[p] + 1 == self.length[q]:
                self.link[cur] = q
            else:
                clone = self._new(self.length[p] + 1, self.link[q], self.nxt[q])
                self.link[q] = clone; self.link[cur] = clone
                while p != -1 and self.nxt[p].get(c) == q:
                    self.nxt[p][c] = clone; p = self.link[p]
        return cur

def findLength(nums1, nums2):
    g = GSA()
    marks = defaultdict(int)
    for i, arr in enumerate((nums1, nums2)):
        last = 0
        for x in arr:
            last = g.extend(x, last)      # ints work fine as symbols
            marks[last] |= (1 << i)
    S = len(g.link)
    mask = [marks.get(v, 0) for v in range(S)]
    for v in sorted(range(S), key=lambda v: -g.length[v]):
        p = g.link[v]
        if p != -1:
            mask[p] |= mask[v]
    return max((g.length[v] for v in range(S) if mask[v] == 0b11), default=0)
```

### Complexity

- **Build:** `O(L)` where `L = m + n` (fixed/small alphabet).
- **Mask propagation:** sort states by length `O(L log L)` (or radix/counting
  sort `O(L)`) plus one linear pass.
- **Answer scan:** `O(L)`.
- **Space:** `O(L)`.

## Key Insights & Edge Cases

- Integers are perfectly valid SAM symbols — no need to map them to characters,
  just use them as dictionary keys.
- The **primary mark** must be applied to the state returned by `extend`, which
  is the state of the longest suffix ending at the current position. Marking any
  other state would misattribute ownership.
- Process states in **decreasing `len`** for the propagation pass so children are
  always handled before parents in the suffix-link tree.
- No common element -> no both-bit state -> answer `0` (the `default=0`).
- This generalizes verbatim to `k` arrays: use a `k`-bit mask and look for
  `mask == (1<<k) - 1` (see Problem 3). The DP does not generalize as cleanly.
- If arrays are large and you only need two of them, the `O(m*n)` DP is simpler;
  reach for the GSA when there are several arrays or you need per-array
  attribution.
