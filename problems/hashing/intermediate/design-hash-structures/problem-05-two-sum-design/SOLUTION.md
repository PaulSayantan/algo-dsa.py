# Two Sum III — Data Structure Design — Solution

## Optimal Approach

Scan keys; complement lookup with the doubles-need-two guard.

### Reference implementation

```python
class TwoSum:
    def __init__(self):
        self._cnt = defaultdict(int)

    def add(self, number):
        self._cnt[number] += 1

    def find(self, value):
        for x in list(self._cnt):
            y = value - x
            if y == x:
                if self._cnt[x] >= 2:
                    return True
            elif y in self._cnt:
                return True
        return False
```

### Complexity

add O(1); find O(#distinct).

## Key Insights & Edge Cases

find(6) is True via 1+5; after adding a second 3, 3+3=6 also works.
