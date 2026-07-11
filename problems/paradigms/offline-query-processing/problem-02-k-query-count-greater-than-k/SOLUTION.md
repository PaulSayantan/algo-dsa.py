# Solution - K-query: Count Elements Greater Than k in a Range

## Brute Force

For each query, walk the subarray and count elements above the threshold.

```python
def k_query(a, queries):
    ans = []
    for (i, j, k) in queries:
        cnt = sum(1 for p in range(i - 1, j) if a[p] > k)
        ans.append(cnt)
    return ans
```

- **Time:** `O(n * q)`. With `n = 3*10^4` and `q = 2*10^5` that is `6*10^9`
  comparisons — too slow.
- **Space:** `O(1)` extra.

## Optimal Approach (Offline Query Processing)

The difficulty online is the interaction between the *range* `[i, j]` and the
*threshold* `k`: a single query mixes both. Offline processing decouples them.

Idea: if we could guarantee the Fenwick tree contains a `1` at position `p`
**exactly when** `a[p] > k`, then "how many `> k` in `[i, j]`" becomes a range
sum `prefix(j) - prefix(i - 1)`. To achieve that per query without rebuilding the
tree, sort so the set of "large" elements only *grows*:

1. **Sort array values in decreasing order** as `(value, position)` pairs.
2. **Sort queries in decreasing order of `k`**, remembering each query's original
   index.
3. Sweep the queries from the largest `k` down. Before answering a query with
   threshold `k`, insert (set to `1`) the Fenwick position of every array element
   whose `value > k` that has not been inserted yet. Because `k` is decreasing,
   the pool of inserted elements is monotone — we never remove.
4. Answer the query as `prefix(j) - prefix(i - 1)` on the Fenwick tree.
5. Write the answer to the query's original index.

```python
def k_query(a, queries):
    n = len(a)
    tree = [0] * (n + 1)                       # 1-indexed Fenwick tree

    def update(pos, delta):
        while pos <= n:
            tree[pos] += delta
            pos += pos & (-pos)

    def prefix(pos):                            # sum of a[1..pos] flags
        s = 0
        while pos > 0:
            s += tree[pos]
            pos -= pos & (-pos)
        return s

    # (value, 1-indexed position), sorted by value descending
    elems = sorted(((v, p + 1) for p, v in enumerate(a)), reverse=True)
    order = sorted(range(len(queries)), key=lambda t: queries[t][2], reverse=True)

    ans = [0] * len(queries)
    ptr = 0
    for t in order:
        i, j, k = queries[t]
        while ptr < n and elems[ptr][0] > k:    # insert everything > k
            update(elems[ptr][1], 1)
            ptr += 1
        ans[t] = prefix(j) - prefix(i - 1)
    return ans
```

### Why it is correct

Process queries with thresholds `k_1 >= k_2 >= ...`. Maintain the invariant:
*before answering a query with threshold `k`, the Fenwick tree holds a `1` at
position `p` iff `a[p] > k`.* The pointer `ptr` walks the value-sorted elements
and inserts every element strictly greater than the current `k`. Since thresholds
only decrease, any element inserted for an earlier query (larger threshold) is
still `> k` for the current one, so it must remain — hence "insert only, never
remove" preserves the invariant. Given the invariant, the count of `> k` elements
in `[i, j]` is exactly the number of set bits in that index range, i.e.
`prefix(j) - prefix(i - 1)`.

### Step-by-step (Example 1)

`a = [5,1,2,3,4]`. Value-sorted `(value, pos)`:
`(5,1), (4,5), (3,4), (2,3), (1,2)`.
Queries sorted by `k` descending: `(4,4,4)[k=4]`, `(1,5,2)[k=2]`, `(2,4,1)[k=1]`.

| query        | insert while value>k | positions set | prefix(j)-prefix(i-1) | answer |
|--------------|----------------------|---------------|-----------------------|--------|
| `(4,4,4)` k=4| insert `(5,1)`       | {1}           | prefix(4)-prefix(3)=0 | 0      |
| `(1,5,2)` k=2| insert `(4,5),(3,4)` | {1,4,5}       | prefix(5)-prefix(0)=3 | 3      |
| `(2,4,1)` k=1| insert `(2,3)`       | {1,3,4,5}     | prefix(4)-prefix(1)=2 | 2      |

Scattering to original order `[(2,4,1),(4,4,4),(1,5,2)]` gives `[2, 0, 3]`.

- **Time:** `O((n + q) log n + q log q)` — each of the `n` elements is inserted
  once (`O(log n)` each), each query does two prefix queries (`O(log n)`), plus
  the sorts.
- **Space:** `O(n + q)`.

## Key Insights & Edge Cases

- **Decoupling range from threshold** is the crux: sorting by `k` freezes the
  threshold dimension so a plain prefix sum handles the range dimension.
- **Strict vs. non-strict:** the condition is `a[p] > k`, so insert while
  `value > k`. If the problem asked for `>= k`, change the loop to `value >= k`.
- **No coordinate compression needed on values** here because the Fenwick tree is
  indexed by *array position* (`1..n`), not by value. Values only drive the sort
  order.
- **Positions, not values, go into the tree.** A frequent mistake is building a
  value-indexed BIT and then being unable to restrict to `[i, j]`; indexing by
  position is what makes the range query work.
- **Ties in `k`:** processing equal thresholds consecutively is fine — the
  `while value > k` guard uses the same `k`, so all such queries see an identical
  inserted set.
- **Empty answer:** if the whole range has no element above `k`, the two prefix
  sums are equal and the result is `0`, as in query `(4,4,4)`.
