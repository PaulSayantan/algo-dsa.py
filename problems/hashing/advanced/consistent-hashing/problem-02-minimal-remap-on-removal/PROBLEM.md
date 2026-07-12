# Removing a Node Remaps Only Its Keys

**Difficulty:** Hard

**Source:** Classic — consistent hashing minimal-disruption property

## Description

Demonstrate consistent hashing's defining guarantee. Build a ring, record the owner of every key, remove one server, and check where the keys land now. Implement `analyze_removal(keys, node)` returning `[moved, only_its_keys]` where `moved` is how many of `keys` changed owner and `only_its_keys` is `True` iff every key that moved was previously owned by the removed `node` (no key belonging to a surviving server was disturbed). Restore the node afterward so the ring is reusable.

## Hint

Snapshot get_node for each key, remove the node, re-query. A moved key whose old owner wasn't `node` violates the minimal-remap property.
