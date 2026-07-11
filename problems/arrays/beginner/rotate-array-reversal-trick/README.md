# Rotate Array — The Reversal Trick

The **reversal trick** is a clean, in-place technique for rotating (or otherwise
"re-blocking") a sequence. The core idea:

> To rotate an array right by `k`, reverse the whole array, then reverse the
> first `k` elements, then reverse the remaining `n - k` elements.

That's it — three reversals and the array is rotated, using **O(1) extra space**
and **O(n) time**. Each element is touched a constant number of times.

## Why it works

Reversing the whole array puts the elements that belong at the front (the last
`k`) at the front — but in reversed order. Reversing each of the two resulting
blocks restores the correct internal order of each block. Formally, if the array
is the concatenation `A · B`, then:

```
reverse(A · B)              = reverse(B) · reverse(A)
reverse(reverse(B))         = B
reverse(reverse(A))         = A
=> we obtain B · A          (exactly a rotation)
```

So rotating `[A][B]` into `[B][A]` — the definition of a rotation — is achieved
by three reversals.

## When to reach for it

- Rotating an array/string left or right by `k` positions in place.
- "Swap two adjacent blocks" of a sequence without a temp buffer.
- Word-level manipulations: reverse the whole string, then reverse each word
  (or vice versa) to reverse word order in place.
- Matrix rotation: transpose + reverse-each-row is the 2-D cousin of the trick.

## Complexity

| Metric | Cost |
| ------ | ---- |
| Time   | O(n) — three linear passes |
| Space  | O(1) — reversals are done in place with two pointers |

The building block is a **two-pointer in-place reverse**: swap `arr[lo]` and
`arr[hi]`, move `lo` right and `hi` left until they meet.

## Problems

| # | Problem | Summary | Difficulty |
| - | ------- | ------- | ---------- |
| 1 | [Reverse String](problem-01-reverse-string/PROBLEM.md) | The fundamental in-place two-pointer reverse that powers the trick. | Easy |
| 2 | [Rotate Array](problem-02-rotate-array/PROBLEM.md) | The canonical problem: rotate right by `k` via three reversals. | Medium |
| 3 | [Reverse Words in a String II](problem-03-reverse-words-in-a-string-ii/PROBLEM.md) | Reverse word order in a char array: reverse all, then reverse each word. | Medium |
| 4 | [Reverse Words in a String](problem-04-reverse-words-in-a-string/PROBLEM.md) | Same word-reversal idea plus whitespace normalization. | Medium |
| 5 | [Rotate Image](problem-05-rotate-image/PROBLEM.md) | Rotate an n×n matrix 90° in place using transpose + reverse-each-row. | Medium |
