# Reverse String — Solution

## Brute Force

Allocate a new array, copy the characters from `s` in reverse order, then copy
them back into `s`. Or, in Python, `s[:] = s[::-1]`.

- **Time:** O(n) — one pass to build the reversed copy.
- **Space:** O(n) — the extra array defeats the point of an in-place reversal.

This is disallowed by the problem's O(1)-memory requirement, but it is the
obvious first idea.

## Optimal Approach — Reversal (Two Pointers)

Reverse the array in place with two pointers converging from the ends. This is
*the* primitive that the whole "reversal trick" is built on, so it must be O(1)
space.

```python
def reverseString(self, s: List[str]) -> None:
    lo, hi = 0, len(s) - 1
    while lo < hi:
        s[lo], s[hi] = s[hi], s[lo]
        lo += 1
        hi -= 1
```

### Why it is correct

- **Invariant:** everything strictly outside the window `[lo, hi]` is already in
  its final, reversed position, and elements `s[lo]` and `s[hi]` are the next
  pair that must trade places.
- Each iteration swaps the outermost unfixed pair, then shrinks the window by
  one on each side, preserving the invariant.
- The loop ends when `lo >= hi`. If `lo == hi` (odd length) the middle element is
  already correct; if `lo > hi` (even length) all pairs are placed. Either way
  the array is fully reversed.

### Complexity

- **Time:** O(n) — the pointers together traverse the array once; roughly `n/2`
  swaps.
- **Space:** O(1) — only two index variables.

## Key Insights & Edge Cases

- **Single element (`n == 1`):** `lo == hi` immediately, loop body never runs,
  array unchanged — correct.
- **Two elements (`n == 2`):** exactly one swap, then `lo > hi` — correct.
- **Even vs. odd length:** the `lo < hi` guard handles both without special
  casing the middle element.
- **This is the reusable core.** Rotate Array, Reverse Words, and Rotate Image
  all call an in-place reverse like this on subranges — the only difference is
  which `[lo, hi]` bounds you feed it.
