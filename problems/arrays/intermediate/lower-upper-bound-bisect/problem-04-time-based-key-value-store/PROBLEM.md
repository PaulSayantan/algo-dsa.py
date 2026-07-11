# Time Based Key-Value Store

**Difficulty:** Medium

**Source:** LeetCode 981 — Time Based Key-Value Store

## Description

Design a time-based key-value data structure that can store multiple values for the same key at
different timestamps, and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:

- `TimeMap()` initializes the object.
- `void set(String key, String value, int timestamp)` stores the key `key` with the value `value`
  at the given time `timestamp`.
- `String get(String key, int timestamp)` returns a value such that `set(key, value, timestamp_prev)`
  was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it
  returns the value associated with the **largest** `timestamp_prev`. If there are no values, it
  returns `""` (empty string).

It is guaranteed that all the timestamps passed to `set` for a given key are **strictly increasing**.

## Constraints

- `1 <= key.length, value.length <= 100`
- `key` and `value` consist of lowercase English letters and digits.
- `1 <= timestamp <= 10^7`
- All the timestamps of `set` for a particular `key` are strictly increasing.
- At most `2 * 10^5` calls will be made to `set` and `get`.

## Examples

### Example 1
```
Input:
  TimeMap()
  set("foo", "bar", 1)
  get("foo", 1)   -> "bar"
  get("foo", 3)   -> "bar"
  set("foo", "bar2", 4)
  get("foo", 4)   -> "bar2"
  get("foo", 5)   -> "bar2"

Output: [null, null, "bar", "bar", null, "bar2", "bar2"]
Explanation:
  get("foo", 1): the only value stored at or before time 1 is "bar" (set at t=1).
  get("foo", 3): the latest value at or before time 3 is still "bar" (t=1), since
                 "bar2" was not set until t=4.
  get("foo", 4): "bar2" was set exactly at t=4, so it is returned.
  get("foo", 5): the latest value at or before t=5 is "bar2" (set at t=4).
```

### Example 2
```
Input:
  TimeMap()
  set("love", "high", 10)
  set("love", "low", 20)
  get("love", 5)    -> ""
  get("love", 10)   -> "high"
  get("love", 25)   -> "low"

Output: [null, null, null, "", "high", "low"]
Explanation:
  get("love", 5): no value was set at or before time 5, so return the empty string.
  get("love", 10): "high" was set exactly at t=10.
  get("love", 25): the latest value at or before t=25 is "low" (set at t=20).
```

## Hint

For each key, the timestamps arrive in increasing order, so store them in a sorted list. A `get`
asks for the value at the **largest timestamp `<= query`** — a floor/predecessor query. Compute it
with a **Lower/Upper Bound (bisect)** search: `upper_bound(query) - 1`.
