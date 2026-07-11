# Valid Anagram — Solution

## Brute Force

Sort both strings and compare the sorted results. If `sorted(s) == sorted(t)`
the strings are anagrams because anagrams share the same sorted character
sequence.

```python
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

- **Time:** O(n log n) for the sort (`n = len(s)`).
- **Space:** O(n) for the sorted lists (or O(log n) to O(n) depending on the sort
  implementation's buffers).

This is short and correct, but the `log n` factor is avoidable.

## Optimal Approach (Character Frequency Count)

Anagrams are precisely two strings with identical character multisets, so we can
compare their **counts** directly without ever sorting.

Steps:

1. If `len(s) != len(t)`, return `False` immediately — different lengths can never
   be anagrams. This also lets the rest of the logic assume equal lengths.
2. Allocate a fixed array `counts` of 26 integers, one per lowercase letter.
3. Walk `s` and **increment** `counts[ord(ch) - ord('a')]` for each character.
4. Walk `t` and **decrement** the same buckets.
5. If `t` is an anagram of `s`, every increment is cancelled by a matching
   decrement, so every bucket returns to `0`. If any bucket is non-zero, the
   multisets differ, so return `False`. (With the length check in place, "all
   zero" is guaranteed if and only if the strings are anagrams.)

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - ord('a')] += 1
    for ch in t:
        counts[ord(ch) - ord('a')] -= 1
    return all(c == 0 for c in counts)
```

**Why it is correct:** Incrementing on `s` and decrementing on `t` computes the
element-wise difference of the two frequency vectors. Two strings are anagrams if
and only if their frequency vectors are equal, i.e. their difference is the zero
vector. The length guard rules out the case where one string is a strict superset
of the other.

- **Time:** O(n) — two linear passes plus a constant 26-element check.
- **Space:** O(1) — the 26-slot array does not depend on `n`.

A one-liner with the same complexity: `return Counter(s) == Counter(t)`.

## Key Insights & Edge Cases

- **Length mismatch** is the cheapest possible early exit; always check it first.
- **Unicode / larger alphabet:** if the problem allowed arbitrary Unicode, replace
  the size-26 array with `collections.Counter`, which is the hash-map form of the
  same tally and handles an unbounded alphabet in O(n) time.
- **Case sensitivity / spaces:** classic "sentence anagram" variants require
  normalizing case and stripping non-letters before counting. The LeetCode version
  here is already lowercase-only, so no normalization is needed.
- **Single decrement pass alternative:** you can decrement while iterating `t` and
  bail out early the moment a count goes negative — a micro-optimization that keeps
  the same asymptotic complexity.
