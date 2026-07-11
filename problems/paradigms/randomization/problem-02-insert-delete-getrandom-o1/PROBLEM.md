# Insert Delete GetRandom O(1)

**Difficulty:** Medium

**Source:** LeetCode 380 — Insert Delete GetRandom O(1)

## Description

Implement the `RandomizedSet` class, a set that supports insertion, deletion, and
returning a **uniformly random** element, each in **average O(1)** time:

- `RandomizedSet()` — Initializes the `RandomizedSet` object.
- `insert(val)` — Inserts an item `val` into the set if not present. Returns `true` if the
  item was not present (insertion happened), `false` otherwise.
- `remove(val)` — Removes an item `val` from the set if present. Returns `true` if the item
  was present (removal happened), `false` otherwise.
- `getRandom()` — Returns a random element from the current set of elements. Each element
  must have the **same probability** of being returned. It is guaranteed that at least one
  element exists when `getRandom` is called.

You must implement the functions so that each operation works in **average O(1)** time
complexity.

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- At most `2 * 10^5` calls will be made to `insert`, `remove`, and `getRandom`.
- There will be **at least one** element in the data structure when `getRandom` is called.

## Examples

### Example 1

```
Input:
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]

Output:
[null, true, false, true, 2, true, false, 2]
```

**Explanation:**
- `insert(1)` -> set is `{1}`, returns `true` (1 was not present).
- `remove(2)` -> 2 is not in the set, returns `false`.
- `insert(2)` -> set is `{1, 2}`, returns `true`.
- `getRandom()` -> returns 1 or 2 with probability 1/2 each; shown here returning `2`.
- `remove(1)` -> set is `{2}`, returns `true` (1 was present).
- `insert(2)` -> 2 is already present, returns `false`.
- `getRandom()` -> the set is `{2}`, so it must return `2`.

### Example 2

```
Input:
["RandomizedSet", "getRandom", "insert", "getRandom", "insert", "remove", "getRandom"]
[[], "skip", [5], [], [7], [5], []]

Output (with the invalid getRandom on an empty set skipped):
[null, true, 5, true, true, 7]
```

**Explanation:** (The first `getRandom` is only shown to note it would be invalid on an
empty set; per the constraints, `getRandom` is only called when non-empty.)
- `insert(5)` -> `{5}`, returns `true`.
- `getRandom()` -> set is `{5}`, must return `5`.
- `insert(7)` -> `{5, 7}`, returns `true`.
- `remove(5)` -> `{7}`, returns `true`.
- `getRandom()` -> set is `{7}`, must return `7`.

## Hint

Use **Randomization** together with a data-structure trick: keep the elements in a dynamic
array so a random index gives a uniform element in O(1), and use a hash map from value to
index so you can delete any element in O(1) by swapping it with the last element.
