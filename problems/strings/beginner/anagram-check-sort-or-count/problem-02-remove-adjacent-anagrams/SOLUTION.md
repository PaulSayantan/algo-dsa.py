# Remove Adjacent Anagrams — Solution

## Brute Force

Simulate the process literally: repeatedly scan the list for any index `i` where
`words[i]` is an anagram of `words[i-1]`, delete it, and restart the scan from the
beginning because a deletion can create a new adjacency.

- **Time:** `O(n^2 * L)` in the worst case (`n` = number of words, `L` = word length),
  since each deletion may trigger a full rescan and each anagram test costs `O(L)` (or
  `O(L log L)` with sorting).
- **Space:** `O(n)` for the mutated list.

Correct, but the restarts are unnecessary.

## Optimal Approach (Anagram Check — sort or count)

Key observation: after all deletions, a word survives **iff** it is not an anagram of
the previous *surviving* word. Because deleting an anagram never changes the surviving
representative of a run (they all share the same character multiset), a single
left-to-right pass suffices.

Algorithm:

1. Start with an empty result list `kept`.
2. For each word `w` in `words`:
   - If `kept` is empty, or `w` is **not** an anagram of `kept[-1]`, append `w`.
   - Otherwise skip `w` (it would be deleted).
3. Return `kept`.

For the anagram test, compare **canonical signatures**. The cleanest signature is the
sorted string (`sorted(w)` or `"".join(sorted(w))`); a character-count tuple works too.
You only ever compare `w` against the last kept word, so you can cache that word's
signature to avoid recomputing it.

```python
def removeAnagrams(self, words):
    kept = []
    last_sig = None
    for w in words:
        sig = tuple(sorted(w))            # or a 26-length count tuple
        if sig != last_sig:               # not an anagram of the last kept word
            kept.append(w)
            last_sig = sig
        # else: w is an anagram of the survivor -> drop it
    return kept
```

**Why it is correct:** all words in a maximal run of adjacent anagrams have identical
signatures. The first one is kept; each subsequent one matches `last_sig` and is
dropped. The first word of the next run has a different signature, so it is kept and
becomes the new representative. This is exactly the fixed point of the deletion process,
and since all deletions within a run are interchangeable, the outcome is order-independent
and unique.

- **Time:** `O(n * L log L)` using sorted signatures, or `O(n * L)` using count arrays.
- **Space:** `O(n)` for the output (plus `O(L)` for the cached signature).

## Key Insights & Edge Cases

- **Compare against the survivor, not the raw previous element.** With a single pass
  and `last_sig`, "previous surviving word" and "previous kept word" coincide, so this
  is automatic.
- **Signature caching** turns two anagram checks per step into one; only compute the
  new word's signature.
- **Single-element or all-distinct lists** return unchanged — no adjacent pair ever
  matches.
- **Duplicates** (identical strings) are anagrams of each other and collapse correctly,
  as in Example 1's two `"cd"` entries.
- **Non-adjacent anagrams are preserved** (Example 2: `"a", "b", "a"`), because only
  immediate neighbors are eligible for deletion.
