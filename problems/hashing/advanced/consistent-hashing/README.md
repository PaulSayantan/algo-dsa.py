# Consistent Hashing (Ring)

**Consistent hashing** maps both servers and keys onto the same circular hash space (a *ring*). A key is owned by the first server encountered walking clockwise from the key's position. The payoff: adding or removing a server remaps only the keys in the arc it covers — on average K/N keys, not the whole keyspace as with `key % N` — which is exactly what a cache or sharded store needs when membership changes. **Virtual nodes** (several ring positions per physical server) even out the load so no single server owns a disproportionately large arc.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Design a Consistent Hash Ring](problem-01-design-consistent-hash-ring/PROBLEM.md) | Ring + virtual nodes | Hard |
| 2 | [Removing a Node Remaps Only Its Keys](problem-02-minimal-remap-on-removal/PROBLEM.md) | Minimal remap property | Hard |
