# Valid Parenthesis String — Solution

## Optimal Approach

Sweep left to right tracking the minimum (`low`) and maximum (`high`) number of
unmatched `(` still open, given every possible interpretation of the `*` seen so
far. A `(` bumps both; a `)` drops both; a `*` could be either, so it drops `low`
and raises `high`. If `high` ever goes negative there are too many `)` no matter
what, so return `False`. Clamp `low` at 0 (extra `*`/`(` can always be dropped or
matched later). The string is valid iff `low` can reach 0 at the end.

### Reference implementation

```python
class Solution:
    def checkValidString(self, s):
        low = high = 0
        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1
                high += 1
            if high < 0:
                return False
            if low < 0:
                low = 0
        return low == 0
```
