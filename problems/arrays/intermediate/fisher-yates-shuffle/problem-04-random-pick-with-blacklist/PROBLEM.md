# Random Pick with Blacklist

**Difficulty:** Medium

**Source:** LeetCode 710 — Random Pick with Blacklist

## Description

You are given an integer `n` and an array of **unique** integers `blacklist`. Design an
algorithm to pick a random integer in the range `[0, n - 1]` that is **not** in
`blacklist`. Any such integer should be returned with **equal probability**.

Implement the `Solution` class:

- `Solution(n, blacklist)` initializes the object with the integer `n` and the
  blacklisted integers `blacklist`.
- `int pick()` returns a random integer in `[0, n - 1]` that is not in `blacklist`.

Let `m = n - len(blacklist)` be the number of allowed values. A naive `pick()` that
draws from `[0, n-1]` and retries when it hits a blacklisted number wastes time when
the blacklist is dense. The efficient idea is to **remap** the blacklisted values that
happen to fall in the compact front range `[0, m)` onto the allowed values that live in
the tail `[m, n)`, storing only those remaps in a hash map — then `pick()` is a single
draw from `[0, m)` followed by a map lookup. This remap is exactly a Fisher–Yates-style
"swap into a smaller region, remembering only the swaps" trick.

## Constraints

- `1 <= n <= 10^9`
- `0 <= len(blacklist) <= min(10^5, n - 1)`
- `0 <= blacklist[i] < n`
- All the values of `blacklist` are **unique**.
- At most `2 * 10^4` calls will be made to `pick`.

## Examples

### Example 1

```
Input:
["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
[[7, [2, 3, 5]], [], [], [], [], [], [], []]

Output:
[null, 0, 4, 1, 6, 1, 0, 4]

Explanation:
Solution solution = new Solution(7, [2, 3, 5]);
The allowed values are {0, 1, 4, 6}, so m = 7 - 3 = 4. Blacklisted values below m are
{2, 3}; allowed values at or above m are {4, 6}. We remap 2 -> 4 and 3 -> 6.
pick() draws x uniformly from [0, 3]: x in {0, 1} returns x directly, x == 2 returns 4,
x == 3 returns 6. Each of {0, 1, 4, 6} is returned with probability 1/4.
```

### Example 2

```
Input:
["Solution", "pick", "pick"]
[[4, [0]], [], []]

Output:
[null, 2, 3]

Explanation:
Allowed values are {1, 2, 3}, m = 4 - 1 = 3. The only blacklisted value is 0, which is
below m, so we remap 0 -> (an allowed value in [3, 4)) = 3. pick() draws x from [0, 2]:
x == 0 returns 3, x == 1 returns 1, x == 2 returns 2. Each of {1, 2, 3} has probability
1/3.
```

## Hint

Split `[0, n-1]` at `m = n - len(blacklist)`. Every returned value comes from the
compact range `[0, m)`. Use a hash map to redirect each blacklisted index below `m` to
a distinct allowed index in `[m, n)` — the same "remember only the swaps" idea behind a
map-backed **Fisher–Yates Shuffle**. Then `pick()` is one uniform draw plus a lookup.
