# Jump Game III

**Difficulty:** Medium

**Source:** LeetCode 1306 — Jump Game III

## Description

Given an array of non-negative integers `arr` and a starting index `start`, at any index `i` you may jump to either `i + arr[i]` or `i - arr[i]` (staying within bounds). Return `True` if you can reach ANY index whose value is `0`, otherwise `False`.

Constraints: `1 <= arr.length <= 5 * 10^4`; `0 <= arr[i] < arr.length`; `0 <= start < arr.length`.

## Examples

### Example 1

```
Input:  arr = [4,2,3,0,3,1,2], start = 5
Output: True
```

**Explanation:** From index `5` one path is `5 -> 4 -> 1 -> 3`, and `arr[3] == 0`.

## Hint

Indices are nodes; each index `i` has edges to `i + arr[i]` and `i - arr[i]`. BFS from `start` over reachable indices and stop when you land on a zero.
