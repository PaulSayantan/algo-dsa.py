# Check if the Sentence Is Pangram — Solution

## Optimal Approach

The set of characters deduplicates automatically; since the input is all lowercase letters, a size of exactly 26 means every letter appeared.

### Reference implementation

```python
class Solution:
    def checkIfPangram(self, sentence):
        return len(set(sentence)) == 26
```

### Complexity

Time O(n), space O(1) (at most 26 distinct letters).
