# Dota2 Senate — Solution

## Optimal Approach

Model each party as a FIFO queue of senator indices, built from two stacks. Each round the front senator of each party faces off; whoever has the smaller original index acts first and bans the other, so that banned index is dropped while the winner is re-enqueued with its index increased by `n` — this schedules it for the next round after everyone else, preserving the circular turn order. The loop ends when one queue empties, and that party's non-empty opponent wins. Each ban removes one senator, so the process is linear in the number of senators (amortized O(1) per queue operation via the two-stack pouring trick).

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
    def predictPartyVictory(self, senate):
        n = len(senate)
        radiant = _TwoStackQueue()
        dire = _TwoStackQueue()
        for i, c in enumerate(senate):
            (radiant if c == 'R' else dire).push(i)
        while not radiant.empty() and not dire.empty():
            ri = radiant.pop()
            di = dire.pop()
            if ri < di:
                radiant.push(ri + n)
            else:
                dire.push(di + n)
        return "Radiant" if not radiant.empty() else "Dire"
```
