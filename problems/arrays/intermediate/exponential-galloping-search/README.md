# Exponential (Galloping) Search

**Category:** arrays / intermediate

## What it is

**Exponential search** (also called **galloping search** or **doubling search**)
finds a target in a sorted sequence in two phases:

1. **Gallop / doubling phase.** Start at index `1` and keep doubling the probe
   index — `1, 2, 4, 8, 16, ...` — until the value at the probe **overshoots**
   the target (or the probe runs off the end of the array). This locates a
   window `[bound / 2, bound]` that is guaranteed to contain the target if it
   exists.
2. **Binary search phase.** Run an ordinary binary search inside that window.

If the target lives at position `p`, the doubling phase stops after about
`log2(p)` steps, and the binary search over a window of size `~p` takes another
`O(log p)` steps — so the whole search is `O(log p)`, where `p` is the distance
to the answer, **not** the full array length `n`.

## When to reach for it

- **Unbounded / "infinite" sorted arrays** where you cannot ask for the length
  up front — e.g. a stream, or an API/`ArrayReader` that returns a sentinel
  (like `2^31 - 1`) when you index past the end. Plain binary search needs `hi`,
  and exponential search *manufactures* a valid `hi` for it.
- **Target is expected near the front.** Because the cost is `O(log p)` in the
  answer position `p`, galloping beats a full `O(log n)` binary search when the
  answer sits close to the start of a huge array.
- **Merging / intersecting two sorted arrays of very different sizes.** For each
  element of the small array, gallop forward in the large array instead of
  scanning linearly. This is exactly the "galloping mode" that powers Timsort's
  merge step.
- Signals in a prompt: "unknown size", "infinite array", "`ArrayReader`",
  "reading out of bounds returns a large sentinel", "one array is much larger
  than the other", "sorted, find target faster than O(log n) when it's early".

## Typical complexity

| Phase | Time | Space |
|-------|------|-------|
| Doubling to find the range | `O(log p)` | `O(1)` |
| Binary search inside the range | `O(log p)` | `O(1)` |
| **Total** | **`O(log p)`** (`p` = index of the answer; `<= O(log n)`) | `O(1)` |

For intersecting arrays of sizes `m <= n`, galloping gives
`O(m * log(n / m))`, which is far better than `O(m log n)` when `m` is close to
`n` and better than the `O(m + n)` linear merge when `m << n`.

## Core idea / invariant

Maintain a probe `bound`. **Invariant:** every index strictly below the current
`bound` holds a value `< target` (the doubling phase only advances while
`arr[bound] < target`). So when the loop stops, the answer — if present — is in
`[bound // 2, min(bound, n - 1)]`, and a standard binary search finishes the
job. Doubling guarantees the window we hand to binary search is at most twice
the distance to the answer, which is what keeps the range logarithmic.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Exponential Search in a Sorted Array](problem-01-exponential-search-bounded-array/PROBLEM.md) | Classic exponential search: find a target's index in a normal sorted array | Easy |
| 2 | [Search in a Sorted Array of Unknown Size](problem-02-search-in-sorted-array-unknown-size/PROBLEM.md) | LeetCode 702 — search via an `ArrayReader` whose length is hidden and returns a sentinel out of bounds | Medium |
| 3 | [First 1 in an Infinite Sorted Binary Array](problem-03-first-one-in-infinite-binary-array/PROBLEM.md) | Unbounded array of `0`s followed by `1`s — return the index of the first `1` | Medium |
| 4 | [First and Last Position in an Unbounded Sorted Array](problem-04-first-last-position-unbounded-array/PROBLEM.md) | Find the first and last index of a target in an unknown-size sorted reader | Medium |
| 5 | [Intersection of Two Sorted Arrays (Galloping)](problem-05-intersection-two-sorted-arrays-galloping/PROBLEM.md) | Intersect two sorted arrays of very different sizes using galloping search | Hard |
