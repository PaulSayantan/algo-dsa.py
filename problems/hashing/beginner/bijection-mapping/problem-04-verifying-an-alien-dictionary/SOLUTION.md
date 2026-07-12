# Verifying an Alien Dictionary — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def isAlienSorted(self, words, order):
        rank = {c: i for i, c in enumerate(order)}

        def key(w):
            return [rank[c] for c in w]

        return all(key(words[i]) <= key(words[i + 1]) for i in range(len(words) - 1))
```
