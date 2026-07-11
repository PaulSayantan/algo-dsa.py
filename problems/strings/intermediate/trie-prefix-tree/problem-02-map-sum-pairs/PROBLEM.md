# Map Sum Pairs

**Difficulty:** Medium

**Source:** LeetCode 677 — Map Sum Pairs

## Description

Design a map that allows you to store key-value pairs and then query the **sum of the
values of all keys that begin with a given prefix**.

Implement the `MapSum` class:

- `MapSum()` initializes the `MapSum` object.
- `void insert(String key, int val)` inserts the `key`-`val` pair into the map. If the
  `key` already existed, the original value is **overwritten** with the new `val`.
- `int sum(String prefix)` returns the sum of all the values whose key starts with the
  string `prefix`.

## Constraints

- `1 <= key.length, prefix.length <= 50`
- `key` and `prefix` consist of lowercase English letters `a`–`z`.
- `1 <= val <= 1000`
- At most `50` calls will be made to `insert` and `sum`.

## Examples

### Example 1

```
Input:
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]

Output:
[null, null, 3, null, 5]
```

**Explanation:**
- `insert("apple", 3)` stores apple=3.
- `sum("ap")` -> `3` (only "apple" starts with "ap", value 3).
- `insert("app", 2)` stores app=2.
- `sum("ap")` -> `5` (both "apple"=3 and "app"=2 start with "ap": 3 + 2 = 5).

### Example 2

```
Input:
["MapSum", "insert", "insert", "sum"]
[[], ["apple", 3], ["apple", 7], ["ap"]]

Output:
[null, null, null, 7]
```

**Explanation:**
- `insert("apple", 3)` stores apple=3.
- `insert("apple", 7)` overwrites the value of "apple" to 7 (it is **not** added; 3 is
  replaced).
- `sum("ap")` -> `7` (only key is "apple" with its current value 7).

## Hint

Store each key along a path in a **Trie (Prefix Tree)** and keep a running total on each
node. Handle overwrites by propagating the *delta* between the new and old value so prefix
sums stay correct.
