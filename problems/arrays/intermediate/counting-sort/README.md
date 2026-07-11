# Counting Sort

**Counting Sort** is a non-comparison, integer sorting algorithm. Instead of comparing
elements against each other, it counts how many times each distinct key appears and then
uses those counts to place every element directly into its final position.

It works only when the keys are integers (or map cleanly to integers) drawn from a small,
known range `[0, k]`. Given `n` elements whose keys fall in that range, counting sort runs
in **O(n + k)** time and **O(n + k)** space — beating the `O(n log n)` lower bound of
comparison sorts whenever `k = O(n)`.

## When to reach for it

- The values are integers in a **bounded, reasonably small range** (ages, heights, grades,
  ASCII characters, digits, colors 0/1/2, etc.).
- You want linear-time sorting and can afford `O(k)` extra memory.
- You need a **stable** sort as a building block (counting sort is the stable subroutine
  inside Radix Sort).
- You only need frequencies or a "cheapest / most frequent first" ordering, not a full
  comparison sort.

## When NOT to use it

- The range `k` is huge relative to `n` (e.g., sorting arbitrary 64-bit integers), where the
  count array dwarfs the input.
- The keys are floating point, strings without a bounded alphabet, or otherwise not mappable
  to a compact integer range.

## Core idea (three phases)

1. **Count** — tally occurrences of each key into `count[0..k]`.
2. **Prefix sum** (for the stable, index-computing variant) — turn counts into starting
   positions so each key knows where its block lands in the output.
3. **Place** — walk the input (right-to-left for stability) and drop each element into its
   computed slot.

For many interview problems you don't even need the output array: the count array alone is
enough to reconstruct sorted order or answer the question.

## Complexity

| Metric | Cost |
|--------|------|
| Time   | `O(n + k)` |
| Space  | `O(n + k)` (or `O(k)` when writing back in place) |
| Stable | Yes (with the prefix-sum + right-to-left placement variant) |

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Height Checker](problem-01-height-checker/PROBLEM.md) | Count values in `[1,100]`, rebuild sorted order, compare | Easy |
| 2 | [Relative Sort Array](problem-02-relative-sort-array/PROBLEM.md) | Count values in `[0,1000]`, emit in a custom priority order | Easy |
| 3 | [Sort Colors](problem-03-sort-colors/PROBLEM.md) | Counting sort with `k = 3`, overwrite in place | Medium |
| 4 | [Maximum Ice Cream Bars](problem-04-maximum-ice-cream-bars/PROBLEM.md) | Counting sort as a linear-time greedy subroutine | Medium |
| 5 | [H-Index](problem-05-h-index/PROBLEM.md) | Bucket + cap counting sort, scan from the top | Medium |
