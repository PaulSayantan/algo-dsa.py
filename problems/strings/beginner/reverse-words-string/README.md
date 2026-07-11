# Reverse Words / String

**Reverse whole then per-word, or split-reverse-join.**

Reversing is one of the most fundamental string manipulations. It shows up in
two closely related flavors:

1. **In-place two-pointer reversal** — swap `s[left]` and `s[right]`, then move
   the pointers toward each other until they meet. This reverses a segment of a
   character array in `O(n)` time and `O(1)` extra space. It is the primitive
   that every other problem here is built on.

2. **Reverse-whole-then-per-word (a.k.a. the double reversal trick)** — to
   reorder the *words* of a sentence in place, reverse the entire buffer once
   (which flips both the word order and the letters inside each word), then
   reverse each individual word back to fix the letters. The net effect is that
   word order is reversed while each word reads correctly. The same idea, when
   applied to only two segments, rotates an array/string by `k` positions.

3. **Split-reverse-join** — when extra memory is allowed and the language has
   good string utilities, you can simply `split` on whitespace, `reverse` the
   list of tokens (or leave order, reversing each token), and `join`. This is
   the most readable approach and is often what interviewers accept first before
   asking for the `O(1)`-space in-place version.

## When to reach for it

- You need to reverse a string or a character array.
- You need to reverse the *order of words* in a sentence.
- You need to rotate an array/string by `k` positions in place.
- You need to reverse a *selected subset* of characters (e.g. only vowels) —
  the two-pointer skeleton generalizes cleanly.

## Typical complexity

| Approach | Time | Space |
|---|---|---|
| Two-pointer in-place reversal | `O(n)` | `O(1)` |
| Reverse-whole-then-per-word | `O(n)` | `O(1)` (on a mutable buffer) |
| Split-reverse-join | `O(n)` | `O(n)` (tokens + output) |

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Reverse String](problem-01-reverse-string/PROBLEM.md) | Reverse a char array in place with two pointers | Easy |
| 2 | [Reverse Words in a String III](problem-02-reverse-words-in-string-iii/PROBLEM.md) | Reverse each word's letters, keep word order | Easy |
| 3 | [Reverse Vowels of a String](problem-03-reverse-vowels-of-a-string/PROBLEM.md) | Two-pointer reversal restricted to vowels | Easy |
| 4 | [Reverse Words in a String](problem-04-reverse-words-in-a-string/PROBLEM.md) | Reverse word order, trimming extra spaces | Medium |
| 5 | [Reverse Words in a String II](problem-05-reverse-words-in-a-string-ii/PROBLEM.md) | Reverse word order in place (whole-then-per-word) | Medium |
| 6 | [Rotate Array](problem-06-rotate-array/PROBLEM.md) | Rotate by `k` using the triple-reversal identity | Medium |
