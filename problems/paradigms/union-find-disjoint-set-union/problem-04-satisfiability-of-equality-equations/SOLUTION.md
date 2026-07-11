# Solution — Satisfiability of Equality Equations

## Brute Force

Build a graph whose edges are the `==` constraints, then for each `!=` constraint run a BFS/DFS
to test whether its two variables are reachable from each other. If any `!=` pair is connected,
return `False`.

```python
def equationsPossible(equations):
    adj = {c: [] for c in "abcdefghijklmnopqrstuvwxyz"}
    for eq in equations:
        if eq[1] == '=':
            adj[eq[0]].append(eq[3])
            adj[eq[3]].append(eq[0])
    def connected(s, t):
        # BFS from s, return True if t reached
        ...
    for eq in equations:
        if eq[1] == '!' and connected(eq[0], eq[3]):
            return False
    return True
```

- **Time:** `O(E · (V + E))` — a traversal per `!=` equation. With only 26 variables `V` is tiny,
  but the reachability search is repeated for every inequality.
- **Space:** `O(V + E)`.

## Optimal Approach (Union-Find / Disjoint Set Union)

Equality is an equivalence relation, so the `==` equations partition the (at most 26) variables
into equivalence classes. Two variables *must* be equal iff they land in the same class. A `!=`
equation is violated exactly when it names two variables in the same class.

**Two-pass algorithm:**

1. **Pass 1 — unite.** For every `"a==b"` equation, `union(a, b)`. Skip `!=` for now. Order does
   not matter here because equality is symmetric and transitive.
2. **Pass 2 — verify.** For every `"a!=b"` equation, if `find(a) == find(b)`, the two variables
   are forced equal yet required distinct → return `False`.

If pass 2 finds no conflict, return `True`.

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1

class Solution:
    def equationsPossible(self, equations):
        dsu = DSU(26)
        for eq in equations:
            if eq[1] == '=':
                dsu.union(ord(eq[0]) - 97, ord(eq[3]) - 97)
        for eq in equations:
            if eq[1] == '!':
                if dsu.find(ord(eq[0]) - 97) == dsu.find(ord(eq[3]) - 97):
                    return False
        return True
```

**Why the two-pass order matters.** All equalities must be fully merged *before* any inequality
is checked, otherwise a later `==` could create a contradiction with an already-passed `!=`.
Processing all `==` first guarantees the equivalence classes are final when we test `!=`.

- **Time:** `O(n · α(26))` ≈ `O(n)`, where `n = len(equations)`.
- **Space:** `O(1)` — a fixed 26-element `parent`/`rank` array.

## Key Insights & Edge Cases

- Map letters to indices with `ord(c) - ord('a')`, giving a constant-size universe of 26.
- Self equations like `"a==a"` are harmless no-op unions. But `"a!=a"` must return `False`, and
  the algorithm handles it automatically: `find(a) == find(a)` is always true, so any reflexive
  inequality triggers the conflict check.
- The character at index `2` is always `'='`; only index `1` (`'='` vs `'!'`) distinguishes the
  two forms, so branch on `eq[1]`.
- Because there are at most 26 variables, ranks stay tiny and the structure is trivially fast;
  the exercise is really about the *two-pass* discipline, which generalizes to larger domains.
