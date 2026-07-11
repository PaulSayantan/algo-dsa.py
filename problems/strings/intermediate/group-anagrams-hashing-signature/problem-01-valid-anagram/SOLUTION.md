# Valid Anagram — Solution

## Brute Force

Sort both strings and compare the results. Two strings are anagrams if and only
if their sorted forms are identical, because sorting turns the character
*multiset* into a unique canonical string.

```python
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

- **Time:** `O(k log k)` where `k = max(len(s), len(t))` — dominated by sorting.
- **Space:** `O(k)` for the sorted character lists.

This is already correct and is the "sorted-string signature." The only downside
is the `log k` factor from sorting.

## Optimal Approach (Hashing Signature)

Use the **count signature**: two strings are anagrams exactly when they have the
same frequency for every character. Build a frequency map (a length-26 array or
a `Counter`) for each string and compare them.

Correctness argument: an anagram is a permutation of the characters. A
permutation never changes *which* characters appear or *how many* times each
appears — it only reorders them. The multiset of characters is therefore an
invariant of the anagram relation, and the frequency table is a faithful
encoding of that multiset. Equal tables `<=>` equal multisets `<=>` anagram.

Step by step:

1. If `len(s) != len(t)`, return `False` immediately — different lengths can
   never share a multiset.
2. Build `count[c] += 1` for each character `c` in `s`.
3. For each character `c` in `t`, do `count[c] -= 1`; if it ever goes negative,
   `t` has a character `s` lacks, so return `False`.
4. All counts end at zero `<=>` the tables matched `<=>` return `True`.

```python
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
```

Or the single-array variant that avoids building two maps:

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    for cs, ct in zip(s, t):
        count[ord(cs) - 97] += 1
        count[ord(ct) - 97] -= 1
    return all(v == 0 for v in count)
```

- **Time:** `O(k)` — one pass to build counts, one pass to compare.
- **Space:** `O(1)` for the fixed 26-length array (or `O(A)` for alphabet size
  `A` in the `Counter` version).

## Key Insights & Edge Cases

- **Length check first** is a cheap early exit and also guarantees the
  decrement-based approach is fully correct.
- **Unicode / larger alphabet:** the fixed `[0]*26` array assumes lowercase
  ASCII. For arbitrary Unicode, use a `Counter`/hash map instead; the follow-up
  in the LeetCode prompt explicitly asks about this.
- **Equal strings** (`s == t`) are trivially anagrams — the signatures match.
- **Empty vs. non-empty:** constraints forbid empty strings here, but the count
  approach handles them correctly anyway (two empty strings -> equal empty
  signatures -> `True`).
- The count signature is the same primitive reused across every problem in this
  folder; internalize it.
