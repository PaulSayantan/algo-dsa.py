# Group Anagrams — Solution

## Brute Force

Compare every string against every group's representative. To test if two strings
are anagrams, sort both (or compare letter counts). Start with no groups; for each
string, scan existing groups and drop it into the first matching one, else start a
new group.

```python
groups = []
for s in strs:
    key = sorted(s)
    for g in groups:
        if sorted(g[0]) == key:
            g.append(s)
            break
    else:
        groups.append([s])
```

- **Time:** O(n^2 * k log k) where n = number of strings, k = max length — for each
  of n strings we may compare against up to n groups, each comparison sorting a
  length-k string.
- **Space:** O(n * k) for the output.

The inner scan is a repeated *search*: "which existing group matches my canonical
form?" A hash map answers that directly.

## Optimal Approach (Hashing)

The defining property: **two strings are anagrams iff they share a canonical key.**
Pick a key that is invariant under reordering letters, then bucket by it.

Two standard keys:

1. **Sorted string** — `"".join(sorted(s))`. `"eat"`, `"tea"`, `"ate"` all map to
   `"aet"`. Cost per string O(k log k).
2. **Letter-count signature** — a tuple of 26 counts (one per lowercase letter).
   `"eat"` -> `(1,0,...,1(for e),...,1(for t),...)`. Cost per string O(k).

Bucket every string into a `dict` from key to list, then return the lists.

```python
from collections import defaultdict

def groupAnagrams(strs):
    buckets = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))          # or the 26-count signature below
        buckets[key].append(s)
    return list(buckets.values())
```

Letter-count variant (avoids the log factor):

```python
def groupAnagrams(strs):
    buckets = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        buckets[tuple(count)].append(s)  # tuple so it is hashable
    return list(buckets.values())
```

**Why it is correct.** Two strings hash to the same bucket iff their canonical keys
are equal. Sorting yields identical multiset-ordered strings exactly for anagrams;
a per-letter count tuple is equal exactly when the two strings use each letter the
same number of times — which is the definition of being anagrams. So each bucket
contains precisely one anagram class, and distinct classes land in distinct
buckets.

- **Time:** O(n * k log k) with the sorted key, or O(n * k) with the count key.
- **Space:** O(n * k) for the map and the output.

## Key Insights & Edge Cases

- **The map key must be hashable.** Use a string (`"".join(sorted(s))`) or a
  `tuple(...)`; a `list` cannot be a dict key.
- **`defaultdict(list)`** removes the "create the list on first insert" boilerplate.
- **Empty string** (`[""]`): its key is `""` / an all-zero tuple, forming its own
  single-element group -> `[[""]]`.
- **Single string** trivially forms one group.
- **Choosing the key:** the count signature is asymptotically faster and shines
  when strings are long; the sorted key is shorter to write. Both are correct.
- Beyond lowercase letters, widen the alphabet (use a `dict`/`Counter` frozen into
  a `frozenset` of items, or sort) rather than a fixed size-26 array.
