# Sum of Subarray Minimums — Solution

## Optimal Approach

Every element `arr[mid]` is the minimum of exactly `left * right` subarrays,
where `left` is the number of choices for a starting index (how far left it
stays the strict/weak minimum) and `right` is the number of choices for an
ending index. A monotonic increasing stack of indices finds these spans in one
pass: when the incoming element is smaller-or-equal, the popped index `mid` has
its right boundary at `i` and its left boundary at the new stack top. A sentinel
iteration at `i == n` flushes the stack. Time and space are O(n).

We use `>=` when popping so that equal values are attributed to the leftmost
occurrence only, avoiding double counting.

### Reference implementation

```python
class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10 ** 9 + 7
        n = len(arr)
        res = 0
        stack = []  # indices of a non-decreasing run
        for i in range(n + 1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                res += arr[mid] * (mid - left) * (i - mid)
            stack.append(i)
        return res % MOD
```
