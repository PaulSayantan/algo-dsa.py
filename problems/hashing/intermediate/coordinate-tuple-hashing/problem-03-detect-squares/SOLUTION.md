# Detect Squares — Solution

## Optimal Approach

Multiply the counts of the three companion corners for each valid diagonal.

### Reference implementation

```python
class DetectSquares:
    def __init__(self):
        self.cnt = defaultdict(int)

    def add(self, point):
        self.cnt[(point[0], point[1])] += 1

    def count(self, point):
        px, py = point
        total = 0
        for (x, y), c in list(self.cnt.items()):
            if x == px or abs(x - px) != abs(y - py):
                continue
            total += c * self.cnt[(px, y)] * self.cnt[(x, py)]
        return total
```

### Complexity

add O(1); count O(#distinct points).

## Key Insights & Edge Cases

Duplicate points multiply the square count — that's why the second count is 2.
