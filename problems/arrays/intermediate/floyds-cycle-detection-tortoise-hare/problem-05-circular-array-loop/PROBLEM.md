# Circular Array Loop

**Difficulty:** Medium

**Source:** LeetCode 457 — Circular Array Loop

## Description

You are playing a game involving a **circular** array of non-zero integers
`nums`. Each `nums[i]` denotes the number of indices forward/backward you must
move from index `i`:

- If `nums[i]` is positive, move `nums[i]` steps **forward**.
- If `nums[i]` is negative, move `nums[i]` steps **backward**.

Because the array is circular, moving forward from the last element lands you on
the first element, and moving backward from the first element lands you on the
last element (use modular arithmetic).

A **cycle** in the array consists of a sequence of indices `seq` of length `k`
where:

- Following the movement rules results in a repeating index sequence
  `seq[0] -> seq[1] -> ... -> seq[k-1] -> seq[0] -> ...`
- Every `nums[seq[j]]` is **either all positive or all negative** (the whole
  cycle moves in a single direction).
- `k > 1` — a cycle of length 1 (an index that points to itself) does **not**
  count.

Return `true` if there is a cycle in `nums`, or `false` otherwise.

Follow-up: can you solve it in **O(n)** time and **O(1)** extra space?

## Constraints

- `1 <= nums.length <= 5000`
- `-1000 <= nums[i] <= 1000`
- `nums[i] != 0`

## Examples

### Example 1

```
Input: nums = [2, -1, 1, 2, 2]
Output: true
Explanation: Starting at index 0, move 2 forward to index 2, then move 1 forward
to index 3, then move 2 forward to index 0 (wrapping). The indices 0 -> 2 -> 3
-> 0 form a cycle of length 3, and every step used a positive value (all one
direction), so the answer is true.
```

### Example 2

```
Input: nums = [-1, 2]
Output: false
Explanation: Starting at index 0 (value -1) moves back to index 1; from index 1
(value 2) moving forward 2 steps wraps back to index 1 itself — a self-loop of
length 1, which does not count. Also the directions are mixed. No valid cycle
of length > 1 exists.
```

### Example 3

```
Input: nums = [-2, 1, -1, -2, -2]
Output: false
Explanation: From index 0 (value -2) you reach index 3; from index 3 (value -2)
you reach index 1 (value 1, positive). Any candidate cycle mixes positive and
negative moves, so no single-direction cycle of length > 1 exists.
```

## Hint

For each starting index run **Floyd's Cycle Detection (Tortoise & Hare)** over
the "next index" function `next(i) = (i + nums[i]) mod n`. Add two guards
specific to this problem: abort a search the moment the movement direction
changes sign, and reject a meeting point that is a self-loop of length 1
(`next(i) == i`).
