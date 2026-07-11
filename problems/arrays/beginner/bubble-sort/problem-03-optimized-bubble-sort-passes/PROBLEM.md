# Optimized Bubble Sort Passes

**Difficulty:** Medium

*Source: Classic bubble-sort variant (early-exit / "optimized bubble sort" instrumentation).*

## Description

Bubble sort can be sped up on nearly-sorted data with an **early-exit flag**: after each full
left-to-right sweep, if that sweep performed **zero** swaps, the array is already sorted and we
can stop.

Given an array `arr`, sort it ascending with this optimized bubble sort and return the
**number of passes** performed.

Definitions used here:

- A **pass** is one complete left-to-right sweep that compares adjacent pairs (over the still-
  unsorted prefix) and swaps any that are out of order.
- Keep making passes until a pass completes with **no swaps**.
- **Count every pass you perform, including the final pass that detects the array is already
  sorted.** (So a fully sorted input costs exactly 1 pass — the one that confirms it.)

## Constraints

- `1 <= arr.length <= 1000`
- `-10^9 <= arr[i] <= 10^9`

## Examples

**Example 1**

```
Input:  arr = [1, 2, 3, 4]
Output: 1
```
Explanation: The very first pass makes no swaps, so we immediately detect the array is sorted
and stop. That single confirming pass is counted → 1.

**Example 2**

```
Input:  arr = [5, 1, 4, 2, 8]
Output: 3
```
Explanation:
- Pass 1: `[5,1,4,2,8] → [1,4,2,5,8]` (swaps occurred).
- Pass 2: `[1,4,2,5,8] → [1,2,4,5,8]` (one swap occurred).
- Pass 3: no swaps — array confirmed sorted, stop.

Three passes were performed.

**Example 3**

```
Input:  arr = [4, 3, 2, 1]
Output: 4
```
Explanation: Reverse-sorted input needs the maximum work. Passes 1–3 each perform swaps
(`[4,3,2,1] → [3,2,1,4] → [2,1,3,4] → [1,2,3,4]`), and pass 4 confirms no swaps → 4 passes.

## Hint

Add a boolean `swapped` flag to **Bubble Sort**. Reset it at the start of each pass; if it is
still false at the end of a pass, break. Count how many passes you started.
