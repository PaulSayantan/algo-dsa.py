# Group Shifted Strings — Solution

## Brute Force

For each string, compare it against a representative of every existing group by
checking "is `a` a shift of `b`?" — that check requires equal length and a
constant offset `(b[i] - a[i]) mod 26` for all `i`. Create a new group when no
match is found.

```python
def is_shift(a, b):
    if len(a) != len(b):
        return False
    off = (ord(b[0]) - ord(a[0])) % 26
    return all((ord(bc) - ord(ac)) % 26 == off for ac, bc in zip(a, b))
```

- **Time:** `O(n^2 * k)` — up to `n` shift-checks per string, each `O(k)`.
- **Space:** `O(n * k)` for the groups.

The pairwise `is_shift` scan is the bottleneck; a canonical signature removes it.

## Optimal Approach (Hashing Signature)

The key observation: shifting a string adds the **same constant** to every
character (mod 26). That constant *cancels out* when you look at the **gap
between consecutive characters**:

```
diff[i] = (word[i+1] - word[i]) mod 26
```

If `t` is `s` shifted by `d`, then `t[i] = (s[i] + d) mod 26`, so
`t[i+1] - t[i] = (s[i+1] + d) - (s[i] + d) = s[i+1] - s[i]` (mod 26). The offset
`d` disappears. Therefore the tuple of consecutive differences is **invariant
under shifting**, and it is the canonical signature: two strings are shifts of
each other **iff** they have equal length and equal difference tuples (equal
tuples already force equal length).

Bucket every string by its difference tuple in a hash map; each bucket is exactly
one shifting sequence.

Step by step:

1. Create `groups = defaultdict(list)`.
2. For each `word`, compute
   `sig = tuple((ord(word[i+1]) - ord(word[i])) % 26 for i in range(len(word)-1))`.
   - A single character produces the empty tuple `()`.
3. Append `word` to `groups[sig]`.
4. Return `list(groups.values())`.

```python
from collections import defaultdict
from typing import List

def groupStrings(strings: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in strings:
        sig = tuple(
            (ord(word[i + 1]) - ord(word[i])) % 26
            for i in range(len(word) - 1)
        )
        groups[sig].append(word)
    return list(groups.values())
```

- **Time:** `O(n * k)` — one linear pass per string to build its signature.
- **Space:** `O(n * k)` for stored strings plus signature keys.

## Key Insights & Edge Cases

- **The `mod 26` is essential** — `"az" -> "ba"` is a valid shift (each letter
  advances by 1 with wraparound: `a->b`, `z->a`). Raw differences would give
  `"az": (25)` and `"ba": (-1)`, which only match after reducing mod 26 to
  `(25)`. Forgetting the modulus splits shift-equivalent strings into different
  buckets.
- **Single characters** — every length-1 string has the empty signature `()`, so
  `"a"`, `"z"`, and any other single letter all group together. This matches
  Example 2.
- **Length is encoded in the signature** — a length-`k` string yields a
  `(k-1)`-tuple, so different lengths can never collide; no separate length
  check is needed.
- **Difference direction must be consistent** — always compute
  `next - current` (or always `current - next`); mixing directions breaks the
  invariant.
- This is the same "map to a shift/relabel-invariant normal form, then hash"
  pattern as Find and Replace Pattern (Problem 5).
