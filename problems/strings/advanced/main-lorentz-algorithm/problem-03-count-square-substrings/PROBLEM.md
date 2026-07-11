# Count Square Substrings

**Difficulty:** Medium

Source: Classic competitive-programming counting problem (count all squares with multiplicity).

## Description

A **tandem repeat** (**square**) is a substring of the form `XX`. Two squares are
considered *different occurrences* if they start at different indices **or** have
different lengths — that is, we count squares by their `(start, length)` position,
**with multiplicity**, not by distinct string content.

Given a string `s`, return the total number of positions `(i, len)` such that the
substring `s[i : i+len]` is a square.

## Constraints

- `1 <= len(s) <= 200_000`
- `s` consists of lowercase English letters.
- The count can be large (up to Θ(n²) in the worst case, e.g. `"aaaa...a"`), so use
  a 64-bit integer. Python integers are unbounded, so no overflow concerns there.

## Examples

### Example 1
```
Input:  s = "aabb"
Output: 2
Explanation: "aa" (index 0) and "bb" (index 2) are squares — 2 occurrences.
```

### Example 2
```
Input:  s = "abcabcabc"
Output: 4
Explanation: Length-6 squares start at indices 0, 1, 2, and 3
             ("abcabc", "bcabca", "cabcab", "abcabc"). No other squares exist,
             so the total is 4.
```

### Example 3
```
Input:  s = "aaaa"
Output: 4
Explanation: The squares are "aa"@0, "aa"@1, "aa"@2 (length 2) and "aaaa"@0
             (length 4) — 4 occurrences in total. Note "aaaa"@0 and "aa"@0 are
             counted separately because they have different lengths.
```

## Hint

The **Main–Lorentz Algorithm** emits squares as O(n log n) contiguous ranges of
start indices, each range covering `(hi - lo + 1)` squares of a fixed length; sum
those range sizes instead of listing squares one by one.
