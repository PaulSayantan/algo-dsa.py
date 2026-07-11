# Distinct Substrings in a Collection — Solution

## Brute Force

Enumerate every substring of every string and drop them into a hash set, then
return its size. With total length `L = sum(len(w_i))`, there are `O(L^2)`
substrings and each is up to `O(L)` long, so materializing and hashing them all
costs `O(L^3)` time (or `O(L^2)` with rolling hashes, accepting collision risk)
and `O(L^2)` space. Acceptable for a few thousand total characters, hopeless at
`L = 2 * 10^5`.

- **Time:** `O(L^3)` naive / `O(L^2)` with rolling hashes.
- **Space:** `O(L^2)`.

## Optimal Approach (Generalized Suffix Automaton)

### Why it works

Build **one** suffix automaton and insert the strings one after another. A
suffix automaton recognizes exactly the set of substrings of the strings it was
built from, and it merges identical substrings automatically — so a generalized
SAM recognizes exactly the **union** of substrings over all input strings, each
distinct substring appearing as exactly one path from the initial state.

Just like a single-string SAM, every state `v` groups substrings that share an
`endpos` set, and it is responsible for exactly

```
len[v] - len[link[v]]
```

distinct substrings (the suffixes of its longest member whose lengths fall in
`(len[link[v]], len[v]]`). These intervals partition all distinct substrings of
the union with no overlap, so summing over every non-initial state counts each
distinct substring of the collection exactly once.

### Building a generalized SAM correctly

The subtlety versus a single-string SAM: when we reset `last = root` for a new
string, the character we are about to add **may already have a transition** from
`last`. A naive `extend` would create a duplicate state and corrupt the
automaton. The fixed `extend` handles this case up front:

1. Reset `last = 0` (root) before each new string.
2. In `extend(c, last)`:
   - If `next[last][c]` already exists as state `q`:
     - If `len[last] + 1 == len[q]`, no new state is needed — just return `q`.
     - Otherwise **clone** `q` (a partial-transition clone) and return the clone.
   - Else create a new state `cur` and run the ordinary SAM `extend` logic.

### Steps

1. Create the GSA with a single root state (`len=0`, `link=-1`).
2. For each word, set `last = 0` and feed its characters through `extend`.
3. Sum `len[v] - len[link[v]]` over all states `v != 0`.

### Reference implementation

```python
class GSA:
    def __init__(self):
        self.nxt = [dict()]   # transitions
        self.link = [-1]      # suffix links (root -> -1)
        self.length = [0]     # longest substring length in the state

    def _new(self, length, link, trans=None):
        self.nxt.append(dict(trans) if trans else dict())
        self.link.append(link)
        self.length.append(length)
        return len(self.nxt) - 1

    def extend(self, c, last):
        # Transition already present: reuse or clone, do not add a fresh state.
        if c in self.nxt[last]:
            q = self.nxt[last][c]
            if self.length[last] + 1 == self.length[q]:
                return q
            clone = self._new(self.length[last] + 1, self.link[q], self.nxt[q])
            self.link[q] = clone
            p = last
            while p != -1 and self.nxt[p].get(c) == q:
                self.nxt[p][c] = clone
                p = self.link[p]
            return clone

        cur = self._new(self.length[last] + 1, -1)
        p = last
        while p != -1 and c not in self.nxt[p]:
            self.nxt[p][c] = cur
            p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.nxt[p][c]
            if self.length[p] + 1 == self.length[q]:
                self.link[cur] = q
            else:
                clone = self._new(self.length[p] + 1, self.link[q], self.nxt[q])
                self.link[q] = clone
                self.link[cur] = clone
                while p != -1 and self.nxt[p].get(c) == q:
                    self.nxt[p][c] = clone
                    p = self.link[p]
        return cur


def count_distinct_substrings(words):
    g = GSA()
    for w in words:
        last = 0
        for ch in w:
            last = g.extend(ch, last)
    return sum(g.length[v] - g.length[g.link[v]]
               for v in range(1, len(g.length)))
```

### Complexity

- **Build:** `O(L)` states and transitions (`<= 2L` states); `O(L)` for a fixed
  alphabet, `O(L log |Sigma|)` with hash-map transitions. `L = sum(len(w_i))`.
- **Counting pass:** `O(#states) = O(L)`.
- **Space:** `O(L)` states + `O(L * |Sigma|)` transitions worst case.

## Key Insights & Edge Cases

- **Reset `last = 0` before each string.** Forgetting this glues the strings
  together and counts substrings that straddle two words — a classic bug.
- **Handle the "transition already exists" case** in `extend`; otherwise the
  automaton gains duplicate states and the count is wrong. This is the single
  difference from a one-string SAM.
- The formula `len[v] - len[link[v]]` is always positive for non-root states,
  since a suffix link points to a strictly shorter class.
- Duplicate words in the input do not change the answer — the union is
  idempotent, and the GSA naturally reuses existing states.
- Single string collection reduces to the ordinary distinct-substring count.
- The same states, summing a length contribution instead of a count, give the
  total *length* of all distinct substrings across the collection.
