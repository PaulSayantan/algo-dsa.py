# Bubble Sort Swap Count

**Difficulty:** Easy

*Source: HackerRank "Sorting: Bubble Sort" (classic bubble-sort instrumentation problem).*

## Description

You are given an array `arr` of integers. Sort it in ascending order using **Bubble Sort**,
and report how many **adjacent swaps** the algorithm performs in total.

A swap happens every time bubble sort exchanges two neighboring elements because they are out
of order. Do **not** short-circuit with the early-exit optimization here — count the swaps a
full bubble sort makes. (The total swap count is independent of the early-exit optimization
anyway, but you must count every individual exchange.)

Return the total number of swaps.

## Constraints

- `1 <= arr.length <= 600`
- `1 <= arr[i] <= 2 * 10^6`

## Examples

**Example 1**

```
Input:  arr = [3, 2, 1]
Output: 3
```
Explanation: One valid trace — swap (3,2) → `[2,3,1]`, swap (3,1) → `[2,1,3]`, then swap
(2,1) → `[1,2,3]`. That is 3 swaps total. (This equals the number of inversions in `[3,2,1]`.)

**Example 2**

```
Input:  arr = [1, 2, 3]
Output: 0
```
Explanation: The array is already sorted, so no adjacent pair is ever out of order and no
swap occurs.

**Example 3**

```
Input:  arr = [3, 1, 2]
Output: 2
```
Explanation: Pass 1: swap (3,1) → `[1,3,2]`, then swap (3,2) → `[1,2,3]`. Pass 2 makes no
swaps. Total 2 swaps, matching the 2 inversions: the pairs (3,1) and (3,2).

## Hint

Run **Bubble Sort** as usual, but increment a counter every time you exchange an adjacent
pair. The final counter equals the number of inversions in the array.
