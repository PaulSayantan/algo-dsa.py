# Minimum Insertions to Balance a Parentheses String — Solution

## Optimal Approach

This is the same open-count bookkeeping as the plain "minimum add" variation, but
each `(` now owes **two** `)` instead of one. Scan left to right maintaining
`right`, the number of `)` still owed by already-opened `(`, and `res`, the
insertions forced so far.

- On `(`: it must sit on an even boundary of owed closes. If `right` is odd, the
  previous group is missing one `)`, so insert it (`right -= 1; res += 1`) before
  opening. Then this `(` owes two closes: `right += 2`.
- On `)`: consume one owed close (`right -= 1`). If that drops `right` to `-1`,
  there was no open `(` to match, so insert a `(` (conceptually) and treat this as
  the start of a fresh owed pair: `right = 1; res += 1`.

At the end, any `right` still owed must be inserted as literal `)`, so the answer
is `res + right`. The single running counter is the index/height stack collapsed
to a number, exactly as in the min-add variation.

### Reference implementation

```python
class Solution:
    def minInsertions(self, s):
        res = 0
        right = 0  # ')' still owed by opened '('
        for c in s:
            if c == '(':
                if right % 2:
                    right -= 1
                    res += 1
                right += 2
            else:  # ')'
                right -= 1
                if right == -1:
                    right = 1
                    res += 1
        return right + res
```
