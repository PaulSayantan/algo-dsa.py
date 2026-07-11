# Determine if Two Strings Are Close — Solution

## Brute Force

Simulating the operations (BFS/DFS over reachable strings) is hopeless — the
state space of a length-`10^5` string is astronomically large. Even a "smarter"
brute force that tries all `<= 26!` relabelings is far too slow. So the naive
route is not viable; the value here is recognizing which invariants the two
operations preserve and comparing those directly.

- **Time (naive simulation):** exponential — infeasible.
- **Space:** exponential — infeasible.

## Optimal Approach (Hashing Signature)

Figure out what each operation can and cannot change, then compare the invariants.

- **Operation 1 (swap two existing characters)** freely permutes positions. So
  *order never matters* — only the multiset of characters matters.
- **Operation 2 (turn all of char X into Y and all of Y into X)** relabels
  characters. It can move a *count* from one letter to another, but it can
  neither create a brand-new letter nor delete a letter's presence, and it
  never changes the *collection of counts*, only which letter owns which count.

From these, two strings are close **iff**:

1. **They use exactly the same set of distinct characters.** Operation 2 only
   swaps labels *among characters that already exist* (both must be "existing"),
   so a letter present in one string but absent in the other can never be
   created or removed. Sets must match.
2. **Their multisets of character counts are equal (compare sorted count
   lists).** Operation 1 doesn't change counts at all; Operation 2 can reassign
   a count from one letter to another but preserves the overall multiset of
   counts. So the sorted list of nonzero frequencies must be identical.

Correctness: both conditions are clearly *necessary* (neither operation can
violate them). They are also *sufficient*: given equal character sets and equal
sorted count multisets, pair up letters that should carry each count and use
Operation 2 to relabel each letter of `word1` to the `word2` letter holding the
matching count, then Operation 1 to reorder into `word2` exactly. Hence the
biconditional holds, and comparing the two signatures decides the problem.

Step by step:

1. Build frequency maps `c1` and `c2` (length-26 arrays or `Counter`s).
2. **Character-set check:** `set(chars in word1) == set(chars in word2)`.
   Equivalently, for each letter, `c1[i] > 0` iff `c2[i] > 0`.
3. **Count-multiset check:** `sorted(c1.values()) == sorted(c2.values())`
   (over present letters).
4. Return `True` only if both checks pass.

```python
from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    c1, c2 = Counter(word1), Counter(word2)
    return (set(c1) == set(c2)                       # same distinct characters
            and sorted(c1.values()) == sorted(c2.values()))  # same count multiset
```

Fixed-array variant (alphabet of 26, avoids sorting a hash map):

```python
def closeStrings(word1: str, word2: str) -> bool:
    a = [0] * 26
    b = [0] * 26
    for ch in word1:
        a[ord(ch) - 97] += 1
    for ch in word2:
        b[ord(ch) - 97] += 1
    # same set of present characters
    for i in range(26):
        if (a[i] == 0) != (b[i] == 0):
            return False
    # same multiset of counts
    return sorted(a) == sorted(b)
```

- **Time:** `O(n + A log A)` where `n = len(word1) + len(word2)` and `A = 26`;
  building counts is `O(n)`, sorting the length-26 count arrays is `O(A log A)`,
  i.e. effectively `O(n)`.
- **Space:** `O(A) = O(1)` for the fixed alphabet.

## Key Insights & Edge Cases

- **Both conditions are required.** Same set but different count multiset
  (`"a"` vs `"aa"`) is *not* close. Same count multiset but different set
  (`"aacbb"` counts `[1,2,2]` vs `"ddeff"` counts `[1,2,2]`) is also *not* close
  because the character sets differ.
- **Different lengths** are handled automatically: if lengths differ the sorted
  count multisets cannot be equal (their sums differ), so the second check fails.
- **Operation 2 requires both characters to exist** — that is exactly why the
  set-equality check is the right necessary condition, not a mere "subset."
- **In the fixed-array version, sort the *full* length-26 arrays**; zeros line up
  with zeros, so comparing `sorted(a) == sorted(b)` simultaneously reflects the
  count multiset (and, combined with the presence check, is consistent).
- This problem shows the signature idea at its most abstract: the signature is a
  *pair* — a set plus a sorted multiset — chosen to be exactly the invariants of
  the allowed operations.
