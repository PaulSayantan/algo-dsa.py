# Reverse In-Place

**Reverse In-Place** is the technique of reversing a sequence (array, string buffer,
or a sub-range of one) *without allocating a second buffer*. You keep two pointers —
one at the left end, one at the right end — swap the elements they point to, then move
the pointers toward each other. When they meet (or cross) in the middle, the range is
reversed.

```
left = 0, right = n - 1
while left < right:
    swap(a[left], a[right])
    left  += 1
    right -= 1
```

Because every element is touched at most once and only a constant number of index
variables are used, the reversal runs in **O(n) time** and **O(1) extra space**.

## When to reach for it

- You need to reverse a collection **in place** (the problem says "do not allocate
  another array" or "modify the input directly").
- You need to reverse only a **sub-range** (a segment, a word, a suffix) — the same
  two-pointer swap works on any `[lo, hi]` window.
- A rotation / word-reordering problem can be decomposed into a few reversals
  (the classic "reverse the whole thing, then reverse the pieces" trick).
- You need to selectively swap **symmetric** matching elements (e.g. only vowels).

## Why it works

Swapping position `i` with position `n-1-i` places each element into its mirrored slot.
Doing this for every `i` in the first half moves every element to its final reversed
position exactly once; the middle element (for odd length) is already in place.

## Complexity

| Aspect | Cost |
| --- | --- |
| Time | O(n) — each element visited once |
| Extra space | O(1) — only two indices and a temp swap variable |

## Problems

| # | Problem | Technique focus | Difficulty |
| --- | --- | --- | --- |
| 1 | [Reverse String](problem-01-reverse-string/PROBLEM.md) | The canonical two-pointer swap on a char array | Easy |
| 2 | [Reverse Vowels of a String](problem-02-reverse-vowels-of-a-string/PROBLEM.md) | Swap only symmetric matching (vowel) elements | Easy |
| 3 | [Reverse String II](problem-03-reverse-string-ii/PROBLEM.md) | Reverse fixed-size segments of a string | Easy |
| 4 | [Rotate Array](problem-04-rotate-array/PROBLEM.md) | Rotation via three in-place reversals | Medium |
| 5 | [Reverse Words in a String](problem-05-reverse-words-in-a-string/PROBLEM.md) | Global reverse + per-word reverse | Medium |
| 6 | [Rotate Image](problem-06-rotate-image/PROBLEM.md) | Transpose + reverse each row to rotate a matrix | Medium |
