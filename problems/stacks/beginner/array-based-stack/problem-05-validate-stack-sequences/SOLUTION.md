# Validate Stack Sequences — Solution

## Optimal Approach

Simulate the process directly on an array-backed stack. Iterate over `pushed` in
order, appending each value. After each push, greedily pop while the stack is
non-empty and its top equals `popped[j]`, advancing the pointer `j` into
`popped`. Because the values are distinct, this greedy choice is forced: if the
current top is the next value that must be popped, it has to come off now (any
later push would bury it). Once all values are pushed, the sequence is valid iff
the stack is empty (equivalently, `j` reached the end of `popped`). O(n) time,
O(n) space.

### Reference implementation

```python
class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack
```
