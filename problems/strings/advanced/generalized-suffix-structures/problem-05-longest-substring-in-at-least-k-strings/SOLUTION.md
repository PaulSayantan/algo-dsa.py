# Longest Substring in At Least K Strings — Solution

## Brute Force

Binary-search the answer length `m`. For a candidate `m`, hash every length-`m`
window of every string; a substring qualifies if it appears (as a value) in at
least `k` distinct strings. Track distinct-string counts per hash. Each length
costs `O(L)` with rolling hashes and the binary search adds a `log` factor, so
`O(L log L)` expected — but it relies on hashing (collision risk) and is fiddly
to get right. A fully naive enumeration of all substrings is `O(L^2)` and far too
slow.

- **Time:** `O(L^2)` naive; `O(L log L)` expected with rolling hashes + binary
  search.
- **Space:** `O(L)`.

## Optimal Approach (Generalized Suffix Structure)

### Idea

Build **one** generalized suffix automaton over all `n` strings, tag each state
with a bitmask of the strings that occur there (propagated up the suffix-link
tree), then read off the answer: the largest `len[v]` among states whose mask has
**at least `k` bits set**.

This is Problem 3 with the acceptance test relaxed from "all `n` bits" to "at
least `k` bits". The `popcount` of a state's mask is exactly the number of
*distinct* strings that contain that state's substrings (a substring occurring
many times in one string still contributes a single bit — OR-ing is idempotent).

### Why it is correct

- After OR-ing string-`i`'s bit into every state it occupies during insertion and
  propagating up the suffix links, `mask[v]` equals the set of strings containing
  the substrings of state `v`. All substrings in `v` share one `endpos`, so they
  share ownership; `popcount(mask[v])` is the count of distinct strings that hold
  them.
- If `popcount(mask[v]) >= k`, then the longest substring of `v` (length
  `len[v]`) appears in at least `k` strings and is a candidate. Shorter substrings
  in the same state cannot exceed `len[v]`, so maximizing `len[v]` over qualifying
  states yields the answer.

### Steps

1. Build the GSA, inserting each of the `n` strings after resetting `last = root`.
   OR the current string's bit into every state returned by `extend`.
2. Propagate masks up the suffix links (states in decreasing `len`).
3. Answer = `max(len[v] for v with popcount(mask[v]) >= k)`, else `0`.

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

def longest_substring_in_at_least_k(strings, k):
    g = GSA()
    marks = defaultdict(int)
    for i, w in enumerate(strings):
        last = 0
        for ch in w:
            last = g.extend(ch, last)
            marks[last] |= (1 << i)
    S = len(g.link)
    mask = [marks.get(v, 0) for v in range(S)]
    for v in sorted(range(S), key=lambda v: -g.length[v]):
        p = g.link[v]
        if p != -1:
            mask[p] |= mask[v]
    return max((g.length[v] for v in range(S)
                if bin(mask[v]).count("1") >= k), default=0)
```

### Complexity

- **Build:** `O(L)` for a fixed alphabet (`L = sum of lengths`).
- **Mask propagation:** `O(L)` (counting sort by length) or `O(L log L)`.
- **Answer scan:** `O(L)`; `popcount` is `O(1)` for `n` within a machine word.
- **Space:** `O(L)`.

## Key Insights & Edge Cases

- **Bit OR is idempotent**, so a substring appearing many times inside one string
  still contributes only one bit — exactly the "distinct strings" semantics the
  problem wants. Using a counter that increments per occurrence would be wrong.
- The mask + `popcount` formulation subsumes several problems: `k = n` gives the
  longest common substring of all strings (Problem 3); `k = 2` gives the longest
  substring shared by any two.
- Process states by **decreasing `len`** so children precede parents in the
  suffix-link tree during propagation.
- If even single characters fail to reach `k` strings, no state qualifies and the
  answer is `0` (the `default=0`).
- For `n` beyond the machine word size, replace the integer bitmask with a
  small-to-large merge of *string-ID sets* along the suffix-link tree, tracking
  `|set|` for the `>= k` test; total `O(L log L)`.
- Swapping the `max(len[v])` for `sum(len[v] - len[link[v]])` counts the number of
  *distinct* substrings occurring in at least `k` strings — the "at least `k`"
  analogue of Problem 4.
