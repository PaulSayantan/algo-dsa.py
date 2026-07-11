# Group Anagrams — Solution

## Brute Force

For each string, scan all previously formed groups and check whether it is an
anagram of the group's representative (e.g. compare sorted forms or counts). If
it matches an existing group, append it there; otherwise start a new group.

```python
def groupAnagrams(strs):
    groups = []            # list of (representative_sorted, [members])
    for w in strs:
        key = sorted(w)
        for g in groups:
            if g[0] == key:
                g[1].append(w)
                break
        else:
            groups.append((key, [w]))
    return [g[1] for g in groups]
```

- **Time:** `O(n^2 * k log k)` — for each of `n` words we may compare against up
  to `n` groups, each comparison costing `O(k log k)` (or `O(k)` after
  precomputing keys). Quadratic in the number of words.
- **Space:** `O(n * k)` for the stored groups.

The inefficiency is the linear scan over groups for every word. A hash map turns
that scan into an `O(1)` lookup.

## Optimal Approach (Hashing Signature)

Give each word a **canonical signature** that is identical for anagrams and
distinct for non-anagrams, then use a dictionary `signature -> list of words`.
Everything that hashes to the same bucket is automatically a complete anagram
group.

Two standard signatures:

1. **Sorted string** — `sorted(word)` joined back into a string. `"eat"` and
   `"tea"` both become `"aet"`. Building it costs `O(k log k)`.
2. **Count tuple** — a length-26 tuple of letter frequencies, e.g.
   `"eat" -> (1,0,...,1,...,1,...)`. Building it costs `O(k)`, and tuples are
   hashable so they work directly as dict keys. This beats sorting when words
   are long.

Why it is correct: anagrams are permutations of each other, and a permutation
preserves the character multiset. The sorted string and the count tuple are both
faithful encodings of that multiset, so `signature(a) == signature(b)` if and
only if `a` and `b` are anagrams. Grouping by an exact invariant therefore
produces exactly the anagram classes.

Step by step (count-tuple version):

1. Create `groups = defaultdict(list)`.
2. For each word `w`:
   - Build `count = [0]*26`; for each char, `count[ord(c) - 97] += 1`.
   - Use `tuple(count)` as the key and append `w`: `groups[tuple(count)].append(w)`.
3. Return `list(groups.values())`.

```python
from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for w in strs:
        count = [0] * 26
        for ch in w:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(w)
    return list(groups.values())
```

Sorted-key variant (shorter, slightly slower for long words):

```python
def groupAnagrams(strs):
    groups = defaultdict(list)
    for w in strs:
        groups["".join(sorted(w))].append(w)
    return list(groups.values())
```

- **Time:** `O(n * k)` with the count tuple, or `O(n * k log k)` with sorting,
  where `n` is the number of words and `k` the max word length.
- **Space:** `O(n * k)` to store all words in the map (plus `O(k)` or `O(26)`
  per-word signature scratch).

## Key Insights & Edge Cases

- **Empty string** — its signature is the empty sorted string `""` or the
  all-zero count tuple, so `[""]` correctly yields `[[""]]`.
- **Use a tuple, not a list, as the key** — Python lists are unhashable. Convert
  `count` with `tuple(...)` (or join the sorted chars into a `str`).
- **Count tuple vs. sorted string** — prefer the count tuple when words are long
  (`k log k` sorting dominates), prefer sorted keys for brevity when `k` is
  small. Both are `O(1)` per hash operation.
- **Larger / Unicode alphabet** — replace the fixed length-26 array with a
  `Counter` (then key on `tuple(sorted(counter.items()))`) or fall back to the
  sorted-string signature.
- **Output order is unconstrained** — do not waste effort sorting groups unless
  the judge requires it; `defaultdict` insertion order is fine.
