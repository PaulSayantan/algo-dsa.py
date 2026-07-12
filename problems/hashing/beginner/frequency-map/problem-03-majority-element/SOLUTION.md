# Majority Element — Solution

## Optimal Approach

A frequency map makes the majority explicit: `most_common(1)` returns the highest-count element, which — because the majority strictly exceeds n/2 — is unambiguous. (Boyer-Moore voting solves it in O(1) space as a follow-up.)

### Reference implementation

```python
class Solution:
    def majorityElement(self, nums):
        counts = Counter(nums)
        return counts.most_common(1)[0][0]
```

### Complexity

Time O(n), space O(n).
