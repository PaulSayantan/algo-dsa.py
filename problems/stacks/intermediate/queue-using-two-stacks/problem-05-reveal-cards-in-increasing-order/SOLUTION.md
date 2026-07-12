# Reveal Cards in Increasing Order — Solution

## Optimal Approach

Run the reveal procedure in reverse using the *positions* of the deck. Keep a FIFO queue of the index slots `0..n-1`, built from two stacks. Walk the cards in sorted order: pop the front slot and assign the current (smallest remaining) card there — that slot is the next one that would be revealed — then, to mimic "move the next top card to the bottom," pop the following front slot and push it to the back. Because slots are consumed in the exact order the reveal would visit them, placing sorted cards into them guarantees an increasing reveal. Each slot enters and leaves the queue O(1) times amortized thanks to the two-stack pouring.

### Reference implementation

```python
class _TwoStackQueue:
    def __init__(self):
        self._in = []
        self._out = []

    def push(self, x):
        self._in.append(x)

    def _shift(self):
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def pop(self):
        self._shift()
        return self._out.pop()

    def empty(self):
        return not self._in and not self._out


class Solution:
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        slots = _TwoStackQueue()
        for i in range(n):
            slots.push(i)
        result = [0] * n
        for card in sorted(deck):
            result[slots.pop()] = card
            if not slots.empty():
                slots.push(slots.pop())
        return result
```
