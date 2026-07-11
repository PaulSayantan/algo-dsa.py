# Assign Cookies — Solution

## Brute Force

Try every way of assigning cookies to children (a bipartite matching). You could
enumerate permutations of cookies against children, or model it as maximum bipartite
matching where an edge exists whenever `s[j] >= g[i]`.

- Naive permutation search: `O(n!)` — infeasible.
- Bipartite matching (Hopcroft–Karp): `O(E * sqrt(V))` — correct but far more machinery
  than this structured problem needs.

## Optimal Approach (Greedy)

**Idea:** Sort both `g` and `s` ascending. Walk a pointer through each. For the
current least-greedy unsatisfied child, give them the *smallest cookie that still
fits*. If the smallest available cookie is too small for even the least greedy child,
that cookie can never satisfy anyone (everyone else is greedier), so discard it.

```python
def findContentChildren(g, s):
    g.sort()
    s.sort()
    child = 0                 # index into greed factors
    for cookie in s:          # cookies in ascending size
        if child < len(g) and cookie >= g[child]:
            child += 1        # this child is content; move to next child
    return child
```

**Why it is correct (exchange argument):** Consider any optimal assignment. Take the
smallest cookie it uses. Whatever child that cookie satisfies, we could instead give
that cookie to the *least greedy* satisfiable child without reducing the count — the
originally-served child can take a cookie that is at least as large. Repeating this
exchange transforms any optimal solution into the greedy one, so greedy is optimal.
Equivalently: never spend a large cookie on a child a smaller cookie could satisfy,
and never waste a cookie that fits on nobody.

- **Time:** `O(n log n + m log m)` for the two sorts, then one linear pass.
- **Space:** `O(1)` extra (or `O(n)` if the sort is not in place).

## Key Insights & Edge Cases

- **Both sorts matter.** Sorting only one side breaks the "smallest fitting cookie"
  invariant.
- **Empty cookies** (`s = []`): the loop never advances, returns `0`. Handled naturally.
- **More cookies than children:** extra large cookies simply go unused; the child
  pointer stops at `len(g)`.
- **Duplicate greed / sizes** are fine — the `>=` comparison and single pass handle
  ties correctly.
- This is the canonical "match sorted supply to sorted demand" greedy pattern; the
  same shape appears in problems like *Boats to Save People* and *Advantage Shuffle*.
