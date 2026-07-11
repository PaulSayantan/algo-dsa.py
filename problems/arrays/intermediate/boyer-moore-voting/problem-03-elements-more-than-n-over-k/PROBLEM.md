# Elements That Appear More Than ⌊n/k⌋ Times

**Difficulty:** Medium

**Source:** Classic generalization of Majority Element (Misra–Gries frequent-items /
GeeksforGeeks "Given an array of size n, find all elements that appear more than n/k times")

## Description

Given an integer array `nums` of size `n` and an integer `k >= 2`, return **all** distinct
elements that appear **more than ⌊n/k⌋ times**.

There can be **at most k−1** such elements (k values each appearing more than n/k times would
exceed n total). A qualifying element is **not** guaranteed to exist, so an empty result is
possible. The order of the returned values does not matter, but each qualifying value should
appear once.

Aim for **O(n·k)** time and **O(k)** extra space — independent of the value range.

## Constraints

- `1 <= n <= 5 * 10^4`
- `2 <= k <= 100`
- `-10^9 <= nums[i] <= 10^9`

## Examples

### Example 1

```
Input:  nums = [3, 1, 2, 2, 1, 2, 3, 3], k = 4
Output: [2, 3]
```

Explanation: `n = 8`, threshold is ⌊8/4⌋ = 2, so a value must appear at least 3 times. `2`
appears 3 times and `3` appears 3 times (both > 2); `1` appears only twice. Answer: `[2, 3]`.

### Example 2

```
Input:  nums = [1, 1, 1, 1], k = 3
Output: [1]
```

Explanation: `n = 4`, threshold is ⌊4/3⌋ = 1. `1` appears 4 times (> 1), so it qualifies. It
is the only distinct value.

### Example 3

```
Input:  nums = [1, 2, 3, 4, 5], k = 2
Output: []
```

Explanation: `n = 5`, threshold is ⌊5/2⌋ = 2, so a value must appear at least 3 times. Every
value appears once, so no element qualifies and the result is empty.

## Hint

Generalize **Boyer–Moore Voting**: instead of one or two candidates, keep up to **k−1**
candidate/count slots (this is the Misra–Gries algorithm). After the voting pass, verify each
surviving candidate with an actual count, since existence is not guaranteed.
