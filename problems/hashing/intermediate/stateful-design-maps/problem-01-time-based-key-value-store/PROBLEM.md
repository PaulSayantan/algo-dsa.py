# Time Based Key-Value Store

**Difficulty:** Medium

**Source:** LeetCode 981 — Time Based Key-Value Store

## Description

Design a store where `set(key, value, timestamp)` records a value and `get(key, timestamp)` returns the value with the largest stored timestamp `<= timestamp`, or `""` if none exists. Timestamps for a key are strictly increasing.

## Examples

### Example 1

```
Input:  set("foo","bar",1); get("foo",1)
Output: "bar"
```

## Hint

key -> list of (timestamp, value); binary-search the largest timestamp <= query.
