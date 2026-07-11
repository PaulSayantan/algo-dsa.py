# Solution — The Untended Antiquity

## Brute Force

Model walls explicitly and run a BFS/DFS on the grid for every type-3 query.

- **Time:** `O(q · n · m)` — each search visits up to `n·m = 6.25 × 10^6` cells,
  times `q = 10^5` queries → `~10^12`. Hopelessly slow.
- **Space:** `O(n · m)` for the wall set and visited array.

## Optimal Approach — random ids + 2D BIT (rectangle-add / point-read)

### The connectivity reduction

Barriers are guaranteed never to intersect or touch, so any two barrier
rectangles are either **strictly nested** or **disjoint** — they form a forest of
nested boxes. A token can move freely *within* a region bounded by barriers but
can never cross a wall. Therefore:

> Two cells are connected **iff they are enclosed by exactly the same set of
> barriers.**

(This equivalence was verified against a physical wall-based BFS on thousands of
random nested/disjoint configurations — it holds exactly.) So we never pathfind;
we just compare the *set of enclosing barriers* of the two cells.

### Fingerprinting a set with random ids

Comparing sets directly is expensive. Instead give each barrier a **random
64-bit id** and maintain, for every cell, the **sum of the ids of all barriers
currently enclosing it**. Adding a barrier means adding its id to every cell
strictly inside its rectangle; removing subtracts it.

Two cells with the *same* enclosing set have equal sums. Two cells with
*different* sets have equal sums only on a hash collision, whose probability is
about `1 / 2^64` per comparison — negligible across `10^5` queries. (XOR of ids
works equally well; sum is fine and slightly simpler to reason about.)

So a query reduces to: **is `value(r1,c1) == value(r2,c2)`?**

### Why a 2D BIT, range-update / point-query mode

- "Add id to every cell inside a rectangle" = **rectangle range-update**.
- "Read one cell's accumulated value" = **point query**.

That is exactly the mode of **Problem 2**: a rectangle add via four corner
difference stamps, and a point read via a 2D prefix sum of the difference grid.

```
def rect_add(self, r1, c1, r2, c2, delta):
    self._add(r1,   c1,   +delta)
    self._add(r2+1, c1,   -delta)
    self._add(r1,   c2+1, -delta)
    self._add(r2+1, c2+1, +delta)

def point_value(self, r, c):        # 2D prefix sum of the diff grid
    total, i = 0, r
    while i > 0:
        j = c
        while j > 0:
            total += self.tree[i][j]
            j -= j & (-j)
        i -= i & (-i)
    return total
```

Add and remove:

```
if kind == 1:
    id = random.getrandbits(63) + 1        # nonzero
    barrier_id[(r1,c1,r2,c2)] = id
    tree.rect_add(r1, c1, r2, c2, +id)
elif kind == 2:
    id = barrier_id.pop((r1,c1,r2,c2))
    tree.rect_add(r1, c1, r2, c2, -id)
else:  # kind == 3
    ans = "Yes" if tree.point_value(r1,c1) == tree.point_value(r2,c2) else "No"
```

### Worked check (Example 2)

- No barriers: `value(1,1) = value(3,3) = 0` → `Yes`.
- Add barrier around `(2,2)` with id `X`: only cell `(2,2)` gets `+X`.
- `(2,2)` has `X`, `(1,1)` has `0` → different → `No`.
- `(1,1)` and `(1,3)` both `0` → `Yes`. Matches the expected `Yes, No, Yes`.

- **Time:** `O(q · log n · log m)`; each add/remove/query is `O(log n · log m)`.
- **Space:** `O(n · m)` for the BIT plus `O(#barriers)` for the id map.

## Key Insights & Edge Cases

- **The whole trick is the reduction**: nested/disjoint barriers ⇒ connectivity =
  equal enclosing set ⇒ equal fingerprint. Without the non-touching guarantee this
  fails and you would need real connectivity structures.
- **Use a wide random range** (e.g. 63–64 random bits) and **nonzero** ids so an
  enclosed cell never accidentally reads `0` like an unenclosed one. With small
  ids (say 1..1000) collisions become likely and the hash breaks.
- **Remove must subtract the *same* id** that was added — key the id map by the
  exact corner tuple, which the problem guarantees is unique among active
  barriers.
- **Sum vs XOR:** both fingerprint the set. Sum with 64-bit random ids is the
  common choice; XOR is equally valid and avoids overflow reasoning in fixed-width
  languages.
- **Corner stamps reach `r2+1`, `c2+1`** (up to `n+1`, `m+1`); size the BIT to
  `(n+2) × (m+2)` so those stamps are not dropped.
- A cell being inside the query endpoints themselves is irrelevant — only the
  barriers matter, and a barrier encloses a cell strictly inside its rectangle
  (the corners passed to `rect_add` are the inclusive interior region).
