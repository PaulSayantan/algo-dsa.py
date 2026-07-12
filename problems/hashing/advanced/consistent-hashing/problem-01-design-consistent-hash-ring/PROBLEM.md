# Design a Consistent Hash Ring

**Difficulty:** Hard

**Source:** Classic — Karger et al. consistent hashing

## Description

Implement a consistent-hash ring with virtual nodes. The constructor takes `vnodes` (virtual copies per server). Support `add_node(name)`, `remove_node(name)`, `get_node(key)` (the server that owns `key`), and `num_vnodes()` (total ring positions). Use a **fixed arithmetic hash** so the mapping is identical across runs — never Python's salted builtin `hash()`. Trace the ring by hand: each server places `vnodes` positions, and a key is owned by the first position clockwise (wrapping past the largest position back to the smallest).

## Examples

### Example 1

```
Input:  vnodes=3; add "alpha","beta","gamma"; get_node("apple")
Output: "gamma"
```

**Explanation:** With 3 servers x 3 virtual nodes = 9 ring positions, 'apple' hashes just before one of gamma's positions.

## Hint

Keep a sorted list of ring positions and a position->server map. get_node = bisect_left(positions, hash(key)), wrapping to index 0 at the end.
