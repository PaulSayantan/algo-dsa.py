# Find the Duplicate Number

**Difficulty:** Medium

**Source:** LeetCode 287 — Find the Duplicate Number

## Description

Given an array of integers `nums` containing `n + 1` integers where each
integer is in the range `[1, n]` inclusive, there is only **one repeated
number** in `nums`. Return this repeated number.

You must solve the problem **without modifying the array** `nums` and use only
**constant extra space**.

The elegant insight: because every value is in `[1, n]` and there are `n + 1`
slots, you can treat the array as a function `f(i) = nums[i]` mapping an index
to another index. Starting from index `0` and repeatedly jumping `i -> nums[i]`
produces a sequence that must eventually revisit an index — i.e. it forms a
cycle — and the entrance to that cycle is precisely the duplicated value.

## Constraints

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only once **except for one integer** which
  appears **two or more times**.

## Examples

### Example 1

```
Input: nums = [1, 3, 4, 2, 2]
Output: 2
Explanation: The value 2 appears at indices 3 and 4. Following the jumps
0 -> nums[0]=1 -> nums[1]=3 -> nums[3]=2 -> nums[2]=4 -> nums[4]=2 -> ...
the sequence enters a cycle whose entry value is 2.
```

### Example 2

```
Input: nums = [3, 1, 3, 4, 2]
Output: 3
Explanation: The value 3 appears at indices 0 and 2, and it is the repeated
number.
```

### Example 3

```
Input: nums = [2, 2, 2, 2, 2]
Output: 2
Explanation: The only value present is 2, which repeats. Following jumps from
index 0 immediately loops on 2.
```

## Hint

Read each value as a "next index" pointer, turning the array into an implicit
linked list with a cycle (guaranteed by the pigeonhole principle). Apply
**Floyd's Cycle Detection (Tortoise & Hare)** to find the meeting point, then
run the second phase to locate the cycle's **entrance**, which is the duplicated
number.
