# Round-Robin Load Balancer

**Difficulty:** Medium

**Source:** Classic — round-robin request dispatch

## Description

Design a `RoundRobinBalancer` that hands out servers in round-robin order:

- `RoundRobinBalancer()` initializes an empty balancer.
- `addServer(server_id)` appends a server to the end of the rotation.
- `removeServer(server_id)` removes that server from the rotation (no-op if absent). The rotation must continue smoothly: the cursor stays pointing at the same *next* server it would have picked, adjusting its index if an earlier server was removed.
- `next()` returns the next server id in round-robin order and advances the cursor, or `-1` if there are no servers.

Constraints: server ids are distinct while present; at most a few thousand operations.

## Examples

### Example 1

```
Input:  addServer(10), addServer(20), addServer(30), next(), next(), next(), next()
Output: [10, 20, 30, 10]
```

**Explanation:** Requests cycle through the servers in insertion order, wrapping back to the first after the last.

## Hint

Keep the servers in a list plus a cursor index; `next()` reads `servers[idx]` and advances `idx = (idx + 1) % len`. On removal, decrement the cursor if the removed position was before it, then re-mod so the round-robin sequence resumes without skipping.
