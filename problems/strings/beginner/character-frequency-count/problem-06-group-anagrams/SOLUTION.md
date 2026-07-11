# Group Anagrams — Solution

## Brute Force

Compare every pair of strings and union those that are anagrams (for example by
checking `sorted(a) == sorted(b)`), forming groups by transitivity.

```python
def groupAnagrams(strs):
    groups = []
    for w in strs:
        for g in groups:
            if sorted(g[0]) == sorted(w):   # anagram of this group's representative
                g.append(w)
                break
        else:
            groups.append([w])
    return groups
```

- **Time:** O(G * n * k log k) where `n = len(strs)`, `G` is the number of groups,
  and `k` is the max word length — each new word is compared against a
  representative of every existing group, re-sorting each time. Worst case O(n^2 * k log k).
- **Space:** O(n * k) for the groups.

## Optimal Approach (Character Frequency Count)

Anagrams share the same character multiset, so give each word a **canonical
signature** derived from its frequency count and bucket words by that signature in
a hash map. Words with the same signature are anagrams and land in the same bucket.

Steps:

1. Create an empty hash map `groups` mapping a signature to a list of words.
2. For each word, build a size-26 count vector by tallying its letters.
3. Convert that vector to a hashable key — a `tuple` of the 26 counts (or a joined
   string like `"1#0#0#...#2"`). This tuple is identical for anagrams and distinct
   for non-anagrams.
4. Append the word to `groups[key]`.
5. Return `list(groups.values())`.

```python
from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in strs:
        counts = [0] * 26
        for ch in word:
            counts[ord(ch) - ord('a')] += 1
        groups[tuple(counts)].append(word)   # frequency vector as the key
    return list(groups.values())
```

**Why it is correct:** Two strings are anagrams iff their frequency vectors are
equal. Using the frequency vector (as a tuple) as the dictionary key guarantees
that anagrams collide into the same bucket and non-anagrams never do — the key *is*
the canonical form of the equivalence class "same multiset of letters".

- **Time:** O(n * k) — for each of `n` words we do O(k) work to build its
  size-26 count vector and O(26) to form the key. This beats the sorting-key variant
  (`tuple(sorted(word))`, which is O(n * k log k)).
- **Space:** O(n * k) to store all words across the buckets.

### Sorted-string key alternative

A common equivalent is to key by `"".join(sorted(word))`. It is simpler to write
but costs O(k log k) per word instead of O(k); for small `k` the difference is
minor, but the count-vector key is the asymptotically optimal choice.

## Key Insights & Edge Cases

- **The signature must be hashable:** a Python `list` cannot be a dict key, so
  convert the count vector to a `tuple` (or a string).
- **Empty string** produces the all-zero count vector and forms its own valid group
  `[""]`.
- **Duplicate words** (e.g. two `"eat"`s) both hash to the same bucket, which is the
  desired behavior — they are anagrams of each other.
- **Output order is free:** groups and within-group order may be anything, so no
  sorting of the final result is required.
- **Bigger alphabet:** for mixed case or Unicode, swap the fixed count vector for a
  `Counter`-derived key such as `tuple(sorted(Counter(word).items()))`.
