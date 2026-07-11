# Assign Cookies — Solution

## Brute Force

Try to match children to cookies by searching, for each child, for any unused cookie
that satisfies its greed. In the worst case you scan all cookies for each child.

- Even worse, without any structure you might consider all assignments (a bipartite
  matching), which is far more expensive than needed.
- A naive per-child linear scan of remaining cookies is `O(n * m)` time where
  `n = len(g)` and `m = len(s)`, with `O(1)` extra space.

This ignores a key fact: it never pays to "waste" a big cookie on a low-greed child when
a smaller cookie would have done, so an unordered search does redundant work.

## Optimal Approach (Sorting as Preprocessing)

**Idea:** Sort both arrays ascending. Then greedily give the **smallest cookie that is
big enough** to the **least greedy child still unsatisfied**, using two pointers.

**Why it is correct (exchange argument):** Suppose an optimal assignment gives cookie
`c` to the least-greedy child `k`, but a smaller adequate cookie `c'` also exists.
Swapping so that `k` receives `c'` (the smaller one) never reduces the count of content
children and frees the larger cookie for a greedier child. Repeating this argument shows
that always spending the smallest sufficient cookie on the least greedy child is optimal.
Sorting is what makes "smallest sufficient" and "least greedy" available in one linear
sweep.

**Step by step:**

1. Sort `g` ascending and `s` ascending.
2. Keep a pointer `i` into `g` (current child) and `j` into `s` (current cookie).
3. Walk `j` forward. For each cookie `s[j]`:
   - If `s[j] >= g[i]`, this cookie satisfies child `i`: advance `i` (one more content
     child) and advance `j`.
   - Otherwise the cookie is too small for even the least greedy remaining child, so
     discard it: advance `j` only.
4. Stop when either array is exhausted. The number of children satisfied is `i`.

```python
def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:   # smallest adequate cookie for least greedy child
            i += 1
        j += 1             # cookie consumed either way (used, or too small to ever help)
    return i
```

- **Time:** `O(n log n + m log m)` for the two sorts, then `O(n + m)` for the sweep.
- **Space:** `O(1)` beyond the in-place sort (or `O(n + m)` if the sort is not in place).

## Key Insights & Edge Cases

- **Sorting is the whole trick:** once both arrays are sorted, the greedy "smallest
  sufficient cookie" decision is a single monotone pass — no backtracking.
- **A too-small cookie is thrown away, not the child.** If the current smallest cookie
  can't satisfy the current least-greedy child, no larger child will accept it either,
  so we skip the cookie and keep the child.
- **Empty cookies (`s = []`):** the loop never enters; answer is `0`.
- **More cookies than children / more children than cookies:** the `while` condition on
  both pointers handles both cases automatically.
- **Duplicate greed factors or sizes** are fine — sorting keeps equal values adjacent
  and the comparison `s[j] >= g[i]` still works.
- **Large values** (`2^31 - 1`) are no problem in Python; in fixed-width languages use a
  wide enough integer type.
