# Solution — Find the Difference

## Brute Force

Count how many times each letter appears in `t` and in `s`, then return the letter
whose count in `t` exceeds its count in `s`. A `collections.Counter` (or a fixed
26-slot array indexed by `ord(c) - ord('a')`) makes this concrete:

```python
from collections import Counter

def findTheDifference(s, t):
    cs, ct = Counter(s), Counter(t)
    for ch in ct:
        if ct[ch] > cs.get(ch, 0):
            return ch
```

- **Time:** O(n) to build both counters and scan.
- **Space:** O(1) — at most 26 distinct letters, but it does allocate hash maps.

This is fine, but we can avoid the auxiliary structure entirely with ASCII
arithmetic.

## Optimal Approach (Case Conversion & ASCII Arithmetic)

Every matched character appears in both `s` and `t`. If we combine all code points
with a *reversible, order-independent* operation, the matched ones cancel out and
only the added character's code remains.

### Method A — sum of code points

Add up `ord(c)` for every character of `t`, subtract `ord(c)` for every character
of `s`. Each character shared by both contributes `+code` (from `t`) and `-code`
(from `s`), netting zero. Only the extra letter has no partner, so the running
total equals its code. Convert back with `chr`.

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        total = 0
        for c in t:
            total += ord(c)
        for c in s:
            total -= ord(c)
        return chr(total)
```

### Method B — XOR of code points

XOR is its own inverse (`x ^ x == 0`) and is commutative/associative, so XOR-ing
the codes of every character in both strings cancels each matched pair and leaves
the added character's code. This never overflows and needs no subtraction:

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        acc = 0
        for c in s + t:
            acc ^= ord(c)
        return chr(acc)
```

**Why it is correct:** `t` contains exactly the multiset of characters in `s` plus
one extra. Both sum-difference and XOR are order-independent (shuffling does not
matter) and pair up equal codes to cancel. Whatever is left after all pairs cancel
is precisely the code of the unmatched, added letter, and `chr` turns it back into
the character.

- **Time:** O(n) — a single pass over each string.
- **Space:** O(1) — just one integer accumulator.

## Key Insights & Edge Cases

- The shuffle is irrelevant: both techniques are commutative, so the order of
  characters never affects the result.
- The extra letter can be a duplicate of an existing letter (see Example 3:
  `"aab"` -> `"baaa"` adds another `'a'`). Counting-by-difference still isolates it
  because the *counts* differ by one.
- Empty `s`: `t` is a single character, and the accumulator ends equal to that
  character's code — handled with no special case.
- XOR is the safest choice in languages with fixed-width integers, since summing
  many code points could overflow; in Python integers are arbitrary precision so
  the sum method is also safe here.
- Both approaches assume the promised invariant `len(t) == len(s) + 1`; they are
  O(1) extra space, strictly better than the hash-map brute force.
