# Ransom Note — Solution

## Brute Force

For each character required by `ransomNote`, scan `magazine` for a matching,
not-yet-consumed letter and "cross it out" (e.g. rebuild the magazine string with
that occurrence removed). If any required character cannot be found, return
`False`.

```python
def canConstruct(ransomNote: str, magazine: str) -> bool:
    remaining = list(magazine)
    for ch in ransomNote:
        if ch in remaining:
            remaining.remove(ch)  # O(len(magazine)) each time
        else:
            return False
    return True
```

- **Time:** O(n * m) in the worst case, where `n = len(ransomNote)` and
  `m = len(magazine)` — each `remove`/`in` scans the remaining list.
- **Space:** O(m) for the mutable copy of the magazine.

## Optimal Approach (Character Frequency Count)

The only thing that matters is *how many* of each letter the magazine offers
versus how many the note demands. So tally the supply once, then spend it.

Steps:

1. Allocate a size-26 array `supply` and tally every character of `magazine`:
   `supply[ord(ch) - ord('a')] += 1`.
2. Walk `ransomNote`. For each character, **decrement** its bucket in `supply`.
3. If a bucket ever drops **below zero**, the note demanded more copies of that
   letter than the magazine had, so return `False`.
4. If the whole note is consumed without any bucket going negative, return `True`.

```python
def canConstruct(ransomNote: str, magazine: str) -> bool:
    supply = [0] * 26
    for ch in magazine:
        supply[ord(ch) - ord('a')] += 1
    for ch in ransomNote:
        idx = ord(ch) - ord('a')
        supply[idx] -= 1
        if supply[idx] < 0:
            return False
    return True
```

**Why it is correct:** `supply[c]` after step 1 is exactly the number of copies of
character `c` available. Each demand decrements it; the invariant "`supply[c]`
never goes negative" holds if and only if demand never exceeds supply for any
letter, which is precisely the condition for the note to be constructible.

- **Time:** O(n + m) — one pass over each string.
- **Space:** O(1) — the fixed 26-slot array.

Equivalent one-liner with `Counter`: the note is constructible iff
`Counter(ransomNote) - Counter(magazine)` is empty (subtraction keeps only
positive residuals, i.e. unmet demand).

## Key Insights & Edge Cases

- **Direction matters:** tally the *supply* (magazine) and subtract the *demand*
  (note). Doing it the other way still works but you must then compare
  `note[c] <= magazine[c]` for all `c`.
- **Early length check:** if `len(ransomNote) > len(magazine)` you can return
  `False` immediately — there simply are not enough letters overall.
- **Reusing letters:** the "each letter used once" rule is why we track counts,
  not mere presence. A boolean "seen" set would wrongly accept `"aa"` from `"a"`.
- **Larger alphabets:** switch the array for `collections.Counter` if inputs can
  contain arbitrary characters; the subtraction idea is identical.
