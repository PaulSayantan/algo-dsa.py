# Solution — Repeated String Match

## Brute Force

Keep appending copies of `a` until the built string is long enough to possibly
contain `b`, checking `b in repeated` at each step, and give up once it is
clearly too long.

```python
def repeatedStringMatch(a, b):
    repeated = a
    count = 1
    while len(repeated) < len(b):
        repeated += a
        count += 1
    if b in repeated:            # b in repeated uses Python's substring search
        return count
    repeated += a                # one extra copy to cover an offset start
    count += 1
    return count if b in repeated else -1
```

The logic is right, but `b in repeated` hides the actual matching. The point of
this problem is to do that search yourself with Boyer–Moore, and to reason about
*why only two counts need to be tried*.

- **Time:** `O((n + m) · m)` if the inner `in` is naive, where `n = len(a)`,
  `m = len(b)`.
- **Space:** `O(n + m)` for the built string.

## Optimal Approach — Boyer–Moore (string search)

### How many copies do we ever need?

Let `count = ceil(len(b) / len(a))`. Then `a * count` is the shortest repetition
at least as long as `b`.

- If `b` occurs in `a * count`, the answer is `count`.
- Otherwise, `b` might start partway through an `a` block and spill over the end,
  needing **one more** copy: `a * (count + 1)`.
- If `b` does not occur in `a * (count + 1)` either, it never will — any longer
  repetition only adds full periods of `a` at the end and cannot introduce a new
  alignment of `b` that was not already visible within a window of length
  `len(b) + len(a) - 1` characters (which `a * (count + 1)` already covers).

So we test **at most two** candidate strings.

```python
import math

def repeatedStringMatch(a, b):
    count = max(1, math.ceil(len(b) / len(a)))
    for k in (count, count + 1):
        if boyer_moore_search(a * k, b) != -1:
            return k
    return -1
```

`boyer_moore_search(text, pattern)` is the standard right-to-left matcher with
bad-character and good-suffix tables (see Problem 1). We only need existence.

### Why it is correct

- **Lower bound.** `a * k` must be at least `len(b)` long to contain `b`, so
  `k >= ceil(len(b)/len(a)) = count`. No smaller `k` can work.
- **Upper bound / termination.** Suppose `b` is a substring of `a * K` for some
  large `K`, starting at some index `p`. The starting offset within a period is
  `p mod len(a)`, one of only `len(a)` possibilities, and the match spans at most
  `len(b)` characters, i.e. lives inside a window of `len(b) + len(a) - 1`
  characters. `a * (count + 1)` has length
  `(count + 1) · len(a) >= len(b) + len(a)`, which is at least that window, and
  it contains every possible period-offset alignment. Hence if `b` occurs
  anywhere, it occurs in `a * count` or `a * (count + 1)`. (Verified
  exhaustively on random small inputs.)
- Boyer–Moore returning the first index correctly decides substring membership
  (see Problem 1).

### Step-by-step on Example 1 (`a = "abcd"`, `b = "cdabcdab"`)

- `count = ceil(8 / 4) = 2`. Candidate `a*2 = "abcdabcd"`. Boyer–Moore searches
  for `"cdabcdab"` (length 8) in a length-8 text — the only alignment `s = 0`
  fails (`"abcdabcd" != "cdabcdab"`) → not found.
- Try `count + 1 = 3`. Candidate `a*3 = "abcdabcdabcd"` (length 12). Boyer–Moore
  finds `"cdabcdab"` at index 2 → return `3`.

### Complexity

- **Preprocess `b`:** `O(m + |Σ|)`.
- **Search:** at most two searches over strings of length `O(n + m)`, so
  `O((n + m) · m)` worst case, typically sublinear per search.
- **Space:** `O(n + m)` for the repeated string plus `O(m + |Σ|)` tables.

## Key Insights & Edge Cases

- **Only two candidates** (`count` and `count + 1`) ever need checking — this
  bound is the heart of the problem; testing unboundedly many copies would loop
  forever on `b = "wxyz"`, `a = "abc"`.
- **`count = max(1, ...)`** guards the case `len(b) < len(a)` where the ceiling
  is 1 but you must still try at least one copy (and then two).
- **Character set check (optional fast reject):** if `b` contains a character not
  in `a`, the answer is immediately `-1`; this can skip the searches entirely.
- **`a` shorter than `b` by a lot** is the common case where the two-candidate
  bound matters most; do not conflate `len(a * count) >= len(b)` with "`b` is
  contained" — you still must search.
