# Jump Game

**Difficulty:** Medium

**Source:** LeetCode 55 (Jump Game)

## Description

You are given an integer array `nums`. You are initially positioned at the array's
**first index**, and each element `nums[i]` represents your **maximum jump length**
at that position.

From index `i` you may jump to any index `j` with `i < j <= i + nums[i]`.

Return `true` if you can reach the **last index**, and `false` otherwise.

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Examples

### Example 1

```
Input:  nums = [2, 3, 1, 1, 4]
Output: true
```

Explanation: Jump 1 step from index 0 to index 1, then 3 steps to the last index (4).
Reaching the end is possible, so return **true**.

### Example 2

```
Input:  nums = [3, 2, 1, 0, 4]
Output: false
```

Explanation: No matter how you jump, you always arrive at index 3, whose value is 0.
From index 3 you cannot move, and index 4 is unreachable, so return **false**.

### Example 3

```
Input:  nums = [0]
Output: true
```

Explanation: You start already on the last index (index 0), so no jump is needed and
the answer is **true**.

## Hint

Use a **Greedy** scan: track the farthest index reachable so far. If your current
position ever exceeds that reach, you are stuck. You never need to decide *which*
jump to take — only how far you *could* get.
