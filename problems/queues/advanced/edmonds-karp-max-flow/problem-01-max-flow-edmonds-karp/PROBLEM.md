# Maximum Flow (Edmonds–Karp)

**Difficulty:** Hard

**Source:** Classic — Edmonds–Karp max-flow (cf. SPOJ FASTFLOW)

## Description

Given `n` nodes, a list of directed capacity edges `[u, v, cap]`, a source `s`, and a sink `t`, return the maximum flow from `s` to `t` using the BFS-augmenting-path (Edmonds–Karp) method.

## Examples

### Example 1

```
Input:  classic 6-node network
Output: 23
```

## Hint

Repeatedly BFS for an s-t path with residual capacity; augment by the bottleneck until none remains.
