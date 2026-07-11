# Solution — Time Based Key-Value Store

## Brute Force

Store, for each key, a list of `(timestamp, value)` pairs. On `get`, scan the whole list and keep
the pair with the largest timestamp `<= query`.

```python
class TimeMap:
    def __init__(self):
        self.store = {}                      # key -> list of (timestamp, value)

    def set(self, key, value, timestamp):
        self.store.setdefault(key, []).append((timestamp, value))

    def get(self, key, timestamp):
        best = ""
        for t, v in self.store.get(key, []):
            if t <= timestamp:
                best = v                     # list is in insertion (increasing) order
        return best
```

- **Time:** `set` `O(1)`; `get` `O(m)` where `m` is the number of values stored for that key.
- **Space:** `O(total number of set calls)`.

With up to `2 * 10^5` operations, an `O(m)` `get` degrades to `O(n^2)` overall in the worst case.

## Optimal Approach — Floor query via Upper Bound (bisect)

Because timestamps for a given key are **strictly increasing**, appending on `set` keeps the
per-key timestamp list **sorted**. A `get(key, query)` asks for the value at the **largest
timestamp `<= query`** — the *floor* (a.k.a. predecessor-or-equal). That is `upper_bound(query) - 1`:

- `upper_bound(query)` = first index whose timestamp is `> query`.
- Subtracting 1 gives the last index whose timestamp is `<= query`.
- If that index is `-1`, no timestamp is `<= query`, so return `""`.

```python
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.times = {}     # key -> sorted list of timestamps
        self.vals = {}      # key -> values parallel to times

    def set(self, key, value, timestamp):
        self.times.setdefault(key, []).append(timestamp)
        self.vals.setdefault(key, []).append(value)

    def get(self, key, timestamp):
        ts = self.times.get(key)
        if not ts:
            return ""
        idx = bisect_right(ts, timestamp) - 1   # floor index
        return self.vals[key][idx] if idx >= 0 else ""
```

Hand-rolled upper bound (identical to `bisect_right`), for clarity:

```python
def upper_bound(ts, x):        # first index i with ts[i] > x
    lo, hi = 0, len(ts)
    while lo < hi:
        mid = (lo + hi) // 2
        if ts[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

### Why it is correct

The upper bound gives the count of timestamps `<= query` (call it `k`). Those occupy indices
`0..k-1`, sorted ascending, so index `k - 1` holds the **largest** timestamp `<= query` — precisely
the value we must return. When `k == 0`, no stored timestamp qualifies and we return `""`.

Using `upper_bound` (`<=` in the comparison) rather than `lower_bound` matters for the case
`query == some stored timestamp`: we want to **include** the exact match, so we need the position
*after* equal elements, then step back by one. (Since timestamps are distinct per key here, lower
and upper bound differ by exactly 1 at a match, but the floor formula `ub - 1` is the robust one.)

### Step-by-step on `get("foo", 3)` after `set("foo","bar",1)`, `set("foo","bar2",4)`

`times["foo"] = [1, 4]`, `vals["foo"] = ["bar", "bar2"]`, query = 3.

| lo | hi | mid | ts[mid] | `<= 3`? | action |
|----|----|-----|---------|---------|--------|
| 0  | 2  | 1   | 4       | no      | hi = 1 |
| 0  | 1  | 0   | 1       | yes     | lo = 1 |
| 1  | 1  | —   | —       | end     | `ub = 1` |

`idx = 1 - 1 = 0` → `vals["foo"][0] = "bar"`. ✓

- **Time:** `set` `O(1)` amortized; `get` `O(log m)`.
- **Space:** `O(n)` for `n` total `set` calls.

## Key Insights & Edge Cases

- **Floor = `upper_bound - 1`.** Memorize this: the last element `<= x` sits one slot before the
  first element `> x`. (Symmetrically, the last element `< x` is `lower_bound(x) - 1`.)
- **`idx == -1` guard** handles "query earlier than every stored timestamp" (Example 2, `get("love", 5)`
  → `""`). Skipping this guard would wrap around to the last element in Python — a subtle bug.
- **Missing key** returns `""` immediately; do not index into a nonexistent list.
- **Exact timestamp match** (Example 1, `get("foo", 4)`) returns the value set at that exact time
  because upper bound places the boundary *after* the equal timestamp, and `ub - 1` lands on it.
- Parallel arrays (`times`, `vals`) let us binary-search the numeric timestamps directly; storing
  `(timestamp, value)` tuples and bisecting on `(timestamp, chr(255)*...)` sentinels also works but
  is clumsier. Prefer separate arrays or `bisect` with a key.
