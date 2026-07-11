# Solution — Count Distinct Palindromic Substrings

## Brute Force

Enumerate every substring `s[i:j]`, test whether it is a palindrome, and insert
the palindromic ones into a hash set; the answer is the set's size.

- There are `O(n^2)` substrings and each palindrome test / hashing costs `O(n)`,
  so time is `O(n^3)` naively, or `O(n^2)` with hashing / DP palindrome tables.
- Space is `O(n^2)` in the worst case for the set of distinct palindromes stored
  as strings (e.g. `"aaaa...a"` has `n` distinct palindromes but storing them by
  value costs `O(n^2)` characters).

This is fine for `n` up to a few thousand but blows up at `n = 10^5`.

## Optimal Approach — Palindromic Tree (Eertree)

### The key theorem

A string of length `n` has **at most `n` distinct palindromic substrings**.
(Proof sketch: when scanning left to right and appending `s[i]`, at most **one**
palindrome that did not appear before can become a suffix of the new prefix
`s[0..i]` — any new palindrome ending at `i` is the longest palindromic suffix,
and any shorter palindromic suffix of it already appeared earlier as a prefix of
that longest one, hence earlier in the string.)

The eertree builds a node for **each** distinct palindrome, so:

> **number of distinct palindromic substrings = (number of eertree nodes) − 2**

(the `−2` removes the two sentinel roots).

### Structure

- Node `0`: the **imaginary root** with length `-1`. Its purpose is that
  extending it by a character `c` gives `c` — a length-1 palindrome. Its suffix
  link points to itself.
- Node `1`: the **empty-string root** with length `0`. Extending it by `c` gives
  `cc`. Its suffix link points to node `0`.
- Every other node stores `length`, a map `edges[c] -> child` (child is the
  palindrome `c + P + c`), and a `suffix_link` to the longest proper palindromic
  suffix.
- `last` = the node for the longest palindromic suffix of the processed prefix.

### Insertion of `s[i]` (`add`)

1. From `last`, follow suffix links until reaching a node `X` such that the
   character just before the current palindrome occurrence
   (`s[i - len[X] - 1]`) equals `s[i]`. Because node `0` has length `-1`, the
   test `i - len - 1 >= 0` guarantees termination (it always matches the
   character `s[i]` against itself for a single new character).
2. If `X` already has an edge labeled `s[i]`, the palindrome `s[i] + P_X + s[i]`
   already exists — set `last` to that child and stop (nothing new created).
3. Otherwise create a new node with `length = len[X] + 2`. To find its suffix
   link, continue following suffix links **from `suffix_link[X]`** to find
   another node `Y` whose bordering character matches `s[i]`; the new node's
   suffix link is `edges[Y][s[i]]`. Special case: if the new length is `1`, its
   suffix link is the empty root (node `1`).

Each `add` follows suffix links, but the total number of suffix-link steps over
the whole build is `O(n)` amortized (the length of the longest palindromic
suffix increases by at most `1` per character and only decreases along links),
so construction is linear (times `O(log |Σ|)` for map edge lookups).

### Reference implementation

```python
class Solution:
    def countDistinctPalindromes(self, s: str) -> int:
        n = len(s)
        length = [-1, 0]          # node 0: len -1 ; node 1: len 0
        suffix = [0, 0]           # suffix links; root0 -> root0, root1 -> root0
        edges = [dict(), dict()]  # edges[node][char] -> child node
        last = 1                  # longest palindromic suffix so far

        def get_link(v: int, i: int) -> int:
            # climb suffix links until s[i] can extend the palindrome at v
            while i - length[v] - 1 < 0 or s[i - length[v] - 1] != s[i]:
                v = suffix[v]
            return v

        for i, c in enumerate(s):
            cur = get_link(last, i)
            if c in edges[cur]:
                last = edges[cur][c]      # palindrome already exists
                continue
            new = len(length)
            length.append(length[cur] + 2)
            edges.append(dict())
            if length[new] == 1:
                suffix.append(1)          # single char -> empty root
            else:
                link = get_link(suffix[cur], i)
                suffix.append(edges[link][c])
            edges[cur][c] = new
            last = new

        return len(length) - 2            # subtract the two roots
```

- **Time:** `O(n · log |Σ|)` (linear number of node creations and suffix-link
  hops; the log factor comes from dictionary edge lookups). With fixed-size
  arrays per node it is `O(n · |Σ|)` space but `O(n)` time.
- **Space:** `O(n)` nodes; `O(n)` total edges when stored in per-node maps.

## Key Insights & Edge Cases

- **Answer is just `#nodes − 2`.** No separate deduplication is needed — the
  eertree structurally guarantees one node per distinct palindrome.
- **The imaginary root (len `-1`)** is what lets single characters be created;
  do not forget the `i - len - 1 >= 0` guard, which is why length `-1` works.
- **Single character** (`"a"`): one node is created, answer `1`.
- **All-equal string** (`"aaaaa"`): distinct palindromes are `a, aa, aaa, aaaa,
  aaaaa` → answer `5 = n`, the theoretical maximum, and still only `n` nodes.
- **No repeats** (`"abc"`): only the 3 single letters are palindromes → `3`.
- If the problem instead asked for the **number of occurrences** (not distinct),
  you would additionally propagate an occurrence count along suffix links; see
  Problem 3.
