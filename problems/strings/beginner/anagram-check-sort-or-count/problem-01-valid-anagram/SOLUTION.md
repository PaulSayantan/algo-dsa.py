# Valid Anagram — Solution

## Brute Force

Check, for each distinct character in `s`, whether `s` and `t` contain it the same
number of times by scanning `t` from scratch each time (e.g. `t.count(c)`), and also
verify `len(s) == len(t)`.

- **Time:** `O(n^2)` in the worst case — for each of up to `n` characters you rescan
  the whole string.
- **Space:** `O(1)` extra (ignoring the input).

This works but the repeated rescans are wasteful.

## Optimal Approach (Anagram Check — sort or count)

Two strings are anagrams **iff** they have the same length and identical character
frequencies. There are two clean ways to test this.

### Option A — Sort and compare

```python
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

Sorting normalizes each string to a canonical order; two anagrams sort to the exact
same sequence. (Note `sorted` returns lists, and unequal lengths simply produce
unequal lists, so the length check is handled automatically.)

- **Time:** `O(n log n)` from the sort.
- **Space:** `O(n)` for the sorted lists.

### Option B — Count and compare (fastest)

1. If `len(s) != len(t)`, return `False` immediately (different lengths can never be
   anagrams).
2. Build a frequency table of `s`. For lowercase English letters an array of size 26
   indexed by `ord(c) - ord('a')` is ideal; a hash map works for arbitrary
   characters.
3. Walk `t`, decrementing each character's count. If any count goes negative (or a
   character is missing), `t` has a char `s` lacks → return `False`.
4. Since the lengths are equal and no count went negative, all counts end at zero.
   Return `True`.

```python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = [0] * 26
    for cs, ct in zip(s, t):
        counts[ord(cs) - ord('a')] += 1
        counts[ord(ct) - ord('a')] -= 1
    return all(c == 0 for c in counts)
```

A one-liner equivalent is `Counter(s) == Counter(t)`.

- **Time:** `O(n)` — a constant number of linear passes.
- **Space:** `O(1)` for the fixed 26-slot array (or `O(k)` for a map over an alphabet
  of size `k`).

**Why it is correct:** equal length rules out one string being a strict superset; a
zeroed-out (or matching) frequency table means every character appears the same number
of times in both. Those two facts together are exactly the definition of an anagram.

## Key Insights & Edge Cases

- **Length check first.** It's an `O(1)` early exit that also guarantees the
  count-based logic is sound (if lengths match and no count is negative, every count
  must be zero).
- **Equal strings** are anagrams of themselves — the method returns `True`, which is
  correct.
- **Unicode follow-up:** replace the fixed-size array with a hash map keyed on the
  characters (or code points). `Counter(s) == Counter(t)` handles this transparently.
  Be careful if "characters" should mean user-perceived graphemes — combining marks
  and normalization (NFC/NFD) can change the code-point multiset.
- **Case / whitespace:** the problem restricts input to lowercase letters. For general
  text, decide up front whether to lowercase and strip spaces before comparing.
