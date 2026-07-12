# Reorganize String — Solution

## Optimal Approach

Count each character. If any count exceeds `(n + 1) // 2` the answer is impossible. Otherwise push all `(-count, char)` onto a max-heap and repeatedly pop the most frequent character, appending it to the result. Park the just-used character on the side (its one-slot cooldown) and only push it back after the next character is emitted, guaranteeing no two adjacent characters are equal.

### Reference implementation

```python
class Solution:
    def reorganizeString(self, s):
        counts = Counter(s)
        n = len(s)
        if max(counts.values()) > (n + 1) // 2:
            return ""
        heap = [(-cnt, ch) for ch, cnt in counts.items()]
        heapq.heapify(heap)
        prev = None  # the char cooling down for one slot
        res = []
        while heap:
            cnt, ch = heapq.heappop(heap)
            res.append(ch)
            if prev is not None:
                heapq.heappush(heap, prev)
                prev = None
            cnt += 1  # used one occurrence (counts are negated)
            if cnt != 0:
                prev = (cnt, ch)
        return "".join(res)
```

### Complexity

O(n log k) time where k is the alphabet size, O(k) extra space.
