# Maximum XOR of Two Numbers in an Array

**Difficulty:** Medium

**Source:** LeetCode 421 — Maximum XOR of Two Numbers in an Array

## Description

Given an integer array `nums`, return the **maximum result** of `nums[i] XOR nums[j]`,
where `0 <= i <= j < n`.

Although the values are numbers, the idiomatic efficient solution treats each number as a
fixed-length **string of bits** and stores those bit-strings in a prefix tree (a *binary*
Trie). This lets you greedily choose, bit by bit from the most significant end, the path
that maximizes the XOR.

## Constraints

- `1 <= nums.length <= 2 * 10^5`
- `0 <= nums[i] <= 2^31 - 1`

## Examples

### Example 1

```
Input:  nums = [3, 10, 5, 25, 2, 8]
Output: 28
```

**Explanation:** The maximum XOR is `5 XOR 25 = 28`.
In binary, `5 = 00101` and `25 = 11001`, so `5 XOR 25 = 11100 = 28`. No other pair produces
a larger value.

### Example 2

```
Input:  nums = [8, 10, 2]
Output: 10
```

**Explanation:** The maximum XOR is `8 XOR 2 = 10`.
In binary, `8 = 1000` and `2 = 0010`, so `8 XOR 2 = 1010 = 10`. The pair `8 XOR 10 = 2` and
`10 XOR 2 = 8` are both smaller.

## Hint

Insert the bits of each number (most-significant first) into a **binary Trie (Prefix Tree)**
with two children per node (bit `0` and bit `1`). To maximize the XOR of a query number,
greedily walk toward the **opposite** bit at every level when it exists.
