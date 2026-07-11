# Dutch National Flag (3-way Partition)

The **Dutch National Flag (DNF)** algorithm, proposed by Edsger W. Dijkstra, rearranges
an array containing three distinct categories of elements — conventionally "less than",
"equal to", and "greater than" a chosen pivot — into three contiguous groups in a
**single left-to-right pass** using only **O(1) extra space**.

The name comes from the Dutch flag's three colored bands (red, white, blue). The classic
motivating task is sorting an array of 0s, 1s, and 2s in place.

## Core Idea

Maintain three regions with three pointers over the array `a`:

```
[ 0 .. low-1 ]  -> confirmed "< pivot"   (the low region)
[ low .. mid-1] -> confirmed "== pivot"  (the mid / equal region)
[ mid .. high ] -> UNKNOWN, not yet seen
[ high+1 .. n-1]-> confirmed "> pivot"   (the high region)
```

Scan with `mid`. Compare `a[mid]` to the pivot:

- **`a[mid] < pivot`**: swap `a[low]` and `a[mid]`; advance both `low` and `mid`.
- **`a[mid] == pivot`**: it is already in place; advance `mid` only.
- **`a[mid] > pivot`**: swap `a[mid]` and `a[high]`; decrement `high` (do **not** move `mid`,
  because the value swapped in from `high` is unexamined).

The loop runs while `mid <= high`. When it ends, the three regions are correctly ordered.

## When to Reach for It

- Sorting / partitioning around **three** categories (0-1-2 sort, sort colors).
- Partitioning an array around a **range** `[lo, hi]` (`< lo`, in-range, `> hi`).
- The **partition step of 3-way quicksort / quickselect**, which is dramatically faster than
  2-way partitioning when the input has **many duplicate keys** (avoids O(n^2) on equal keys).
- Any in-place, single-pass grouping into "below / at / above" a threshold.

## Complexity

| Metric | Cost |
|--------|------|
| Time   | **O(n)** — each element is examined a constant number of times |
| Space  | **O(1)** — in-place swaps, no auxiliary array |

Note: DNF is **not stable** (relative order within a group is not preserved), which is fine
for the problems below since they only require the group ordering.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Sort Colors](problem-01-sort-colors/PROBLEM.md) | Sort an array of 0s, 1s, 2s in place in one pass — the canonical DNF task. | Medium |
| 2 | [Three-Way Partition Around a Range](problem-02-three-way-partition-range/PROBLEM.md) | Partition around a range `[lowVal, highVal]` into `<`, in-range, `>`. | Medium |
| 3 | [Sort an Array (3-way Quicksort)](problem-03-sort-an-array-3way-quicksort/PROBLEM.md) | Sort integers using quicksort whose partition step is DNF, handling duplicates well. | Medium |
| 4 | [Kth Largest Element (3-way Quickselect)](problem-04-kth-largest-element/PROBLEM.md) | Find the kth largest value using quickselect with a 3-way partition. | Medium |
| 5 | [Wiggle Sort II](problem-05-wiggle-sort-ii/PROBLEM.md) | Reorder so `nums[0] < nums[1] > nums[2] < ...` using DNF around the median. | Hard |
