# Solution - Maximum XOR With an Element From Array

## Brute Force

For each query, scan all of `nums`, keep only values `<= m_i`, and track the best
XOR with `x_i`.

```python
def maximizeXor(self, nums, queries):
    ans = []
    for x, m in queries:
        best = -1
        for v in nums:
            if v <= m:
                best = max(best, v ^ x)
        ans.append(best)
    return ans
```

- **Time:** `O(n * q)`. With `n = q = 10^5` this is `10^10` — too slow.
- **Space:** `O(1)` extra.

## Optimal Approach (Offline Query Processing + Binary Trie)

Two tools combine here:

- A **binary trie** (bitwise prefix tree) over the fixed-width binary
  representations of the numbers lets us, given `x`, find the stored number that
  maximizes `v ^ x`: at each bit from the most significant down, greedily walk
  toward the branch whose bit differs from `x`'s bit (that sets the XOR bit to
  `1`); fall back to the only available branch otherwise. One walk is `O(B)` where
  `B` is the bit width (about 30 for values up to `10^9`).
- The trouble is the cap `nums[j] <= m_i`. Rebuilding the trie per query is
  expensive, so process **offline**: the allowed set grows monotonically with the
  cap `m`.

Algorithm:

1. **Sort `nums` ascending.**
2. **Sort the queries by cap `m` ascending**, remembering original indices.
3. Sweep queries from smallest `m` to largest. Maintain a pointer over sorted
   `nums`; before answering a query with cap `m`, insert into the trie every
   `nums` value `<= m` not yet inserted. Because `m` only increases, previously
   inserted values stay valid — insert only, never delete.
4. If the trie is empty (no value `<= m`), the answer is `-1`; otherwise query the
   trie for the max XOR with `x`.
5. Scatter each answer back to its original query index.

```python
def maximizeXor(self, nums, queries):
    B = 30  # 2^30 > 10^9
    root = {}

    def insert(v):
        node = root
        for b in range(B, -1, -1):
            bit = (v >> b) & 1
            node = node.setdefault(bit, {})

    def query(x):                      # max (v ^ x) over inserted v; -1 if empty
        if not root:
            return -1
        node = root
        best = 0
        for b in range(B, -1, -1):
            bit = (x >> b) & 1
            want = 1 - bit             # prefer differing bit -> XOR bit = 1
            if want in node:
                best |= (1 << b)
                node = node[want]
            else:
                node = node[bit]
        return best

    nums.sort()
    order = sorted(range(len(queries)), key=lambda i: queries[i][1])
    ans = [0] * len(queries)
    ptr = 0
    for i in order:
        x, m = queries[i]
        while ptr < len(nums) and nums[ptr] <= m:
            insert(nums[ptr])
            ptr += 1
        ans[i] = query(x)
    return ans
```

### Why it is correct

Two invariants:

- **Trie contents:** processing caps in ascending order `m_1 <= m_2 <= ...`, the
  pointer inserts exactly the values `<= m` when handling that query. A value
  inserted for an earlier (smaller) cap is `<= m` for the current cap too, so it
  legitimately stays. Thus, before each query the trie holds precisely
  `{v in nums : v <= m}`.
- **Greedy XOR maximization:** processing bits from most to least significant, a
  differing bit contributes `2^b` to the XOR, which outweighs *all* lower bits
  combined. So always taking the differing branch when it exists is optimal; when
  it does not exist, that bit is forced and we take the only branch. This yields
  the maximum `v ^ x` over the stored values.

Together they give the maximum XOR against exactly the allowed subset. When no
value is allowed the trie is empty and we return `-1`.

### Step-by-step (Example 1)

`nums` sorted: `[0, 1, 2, 3, 4]`. Queries sorted by `m`:
`[3,1] (m=1)`, `[1,3] (m=3)`, `[5,6] (m=6)`.

| query    | insert while <= m | trie holds        | max XOR                    | answer |
|----------|-------------------|-------------------|----------------------------|--------|
| `[3,1]`  | `0, 1`            | {0,1}             | `3^0=3`, `3^1=2` -> `3`     | 3      |
| `[1,3]`  | `2, 3`            | {0,1,2,3}         | `1^2=3` is the max         | 3      |
| `[5,6]`  | `4`               | {0,1,2,3,4}       | `5^2=7` is the max         | 7      |

Scatter to original order (queries were already in this order) -> `[3, 3, 7]`.

- **Time:** `O((n + q) * B + q log q)` — each value inserted once at `O(B)`, each
  query one `O(B)` walk, plus sorting. With `B ~ 30` this is comfortably fast.
- **Space:** `O(n * B)` for the trie in the worst case.

## Key Insights & Edge Cases

- **`-1` for an empty allowed set** (Example 2, query `[8,1]`): guard by checking
  whether the trie is empty (or whether any value has been inserted yet) before
  the trie walk.
- **Fixed bit width matters.** Insert and query must use the *same* number of
  bits (here `B = 30`, covering values up to `10^9`). Mismatched widths corrupt
  the greedy comparison.
- **Duplicates in `nums`** are harmless — inserting a value twice just retraces
  existing trie nodes; it neither breaks correctness nor changes answers.
- **Preserve original order.** As always in offline processing, carry the query
  index and write `ans[i]`, never append in sorted order.
- **Alternative without a trie:** sort queries by `m`, and for each incrementally
  maintain a structure; but the trie is the idiomatic tool for max-XOR. Note the
  cap is on `nums[j]`, not on the XOR result, which is exactly what makes the
  ascending-cap sweep work.
