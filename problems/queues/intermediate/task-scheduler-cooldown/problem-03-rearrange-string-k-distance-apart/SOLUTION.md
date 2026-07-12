# Rearrange String k Distance Apart — Solution

## Optimal Approach

Count each character and load a max-heap keyed by remaining frequency. Repeatedly pop the most frequent available character, append it, and push it onto a FIFO cooldown queue holding `(remaining_count, char)`. Once the queue length reaches `k`, the oldest entry has waited the required `k` slots, so pop it and, if it still has occurrences left, return it to the heap. If at any point the heap is empty but characters remain, no arrangement exists and we return `""`. When `k == 0` the string is trivially valid.

### Reference implementation

```python
class Solution:
    def rearrangeString(self, s, k):
        if k == 0:
            return s
        counts = Counter(s)
        heap = [(-cnt, ch) for ch, cnt in counts.items()]
        heapq.heapify(heap)
        result = []
        queue = deque()  # (remaining_count, char) cooling down, oldest first
        while heap:
            cnt, ch = heapq.heappop(heap)
            result.append(ch)
            queue.append((cnt + 1, ch))  # one occurrence used (counts negated)
            if len(queue) >= k:
                front_cnt, front_ch = queue.popleft()
                if front_cnt < 0:  # still has occurrences left
                    heapq.heappush(heap, (front_cnt, front_ch))
        return "".join(result) if len(result) == len(s) else ""
```

### Complexity

O(n log a) time where a is the alphabet size, O(a) extra space.
