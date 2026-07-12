# LRU Cache

An **LRU (least-recently-used) cache** evicts the entry untouched for the longest time when it exceeds capacity. The classic design pairs a hash map (for O(1) lookup) with a doubly linked list ordered by recency, so both `get` and `put` run in O(1). Python's `OrderedDict` bundles both: `move_to_end` marks recency and `popitem(last=False)` evicts the oldest. Every `get` both returns a value and updates recency.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [LRU Cache](problem-01-lru-cache-design/PROBLEM.md) | Hash map + DLL / OrderedDict | Medium |
| 2 | [LRU Cache — Final Contents](problem-02-lru-final-contents/PROBLEM.md) | Resident-set snapshot | Medium |
