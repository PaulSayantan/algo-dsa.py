# Count Triplets That Can Form Two Arrays of Equal XOR

**Difficulty:** Medium

**Source:** LeetCode 1442 — Count Triplets That Can Form Two Arrays of Equal XOR

## Description

Given an integer array `arr`, count index triplets `(i, j, k)` with `0 <= i < j <= k < n` such that `XOR(arr[i..j-1]) == XOR(arr[j..k])`. Because both sides equal `k` iff the whole span `arr[i..k]` XORs to 0, each span with `prefix[i] == prefix[k+1]` contributes `k - i` valid split points `j`.

## Examples

### Example 1

```
Input:  arr = [2,3,1,6,7]
Output: 4
```

**Explanation:** The 4 triplets are (0,1,2),(0,2,2),(2,3,4),(2,4,4).

### Example 2

```
Input:  arr = [1,1,1,1,1]
Output: 10
```

## Hint

a == b (two XORs) iff their XOR is 0 iff prefix[i] == prefix[k+1]; then any j in (i, k] works, giving k - i triplets.
