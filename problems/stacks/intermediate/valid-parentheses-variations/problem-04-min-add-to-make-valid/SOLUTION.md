# Minimum Add to Make Parentheses Valid — Solution

## Optimal Approach

Scan left to right maintaining `open`, the number of `(` still waiting for a
partner. Each `)` either cancels an open `(` (`open -= 1`) or, if none is
available, is itself unmatched and forces an inserted `(` — count that in `adds`.
After the scan, any `open` still positive counts as `(` needing an inserted `)`.
The total insertions are `adds + open`. A stack of open indices would give the
same count; the counter is that stack collapsed to its height.

### Reference implementation

```python
class Solution:
    def minAddToMakeValid(self, s):
        adds = 0
        open_count = 0
        for c in s:
            if c == '(':
                open_count += 1
            else:  # ')'
                if open_count > 0:
                    open_count -= 1
                else:
                    adds += 1
        return adds + open_count
```
