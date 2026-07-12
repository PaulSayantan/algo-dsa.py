# Rendezvous & Jump Consistent Hashing

Two modern alternatives to the ring. **Rendezvous (HRW) hashing** assigns each key to the node with the highest `hash(node, key)` score; adding or removing a node only ever changes the winner for keys near that node, so remapping stays minimal — with no ring or virtual-node bookkeeping. **Jump consistent hashing** (Lamping & Veach) maps a key and a bucket count to a bucket in O(1) memory and O(log n) time using nothing but a linear-congruential generator — ideal when buckets are numbered 0..n-1 and only grow. Both are fully deterministic given fixed constants.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Rendezvous (HRW) get_node](problem-01-rendezvous-hrw/PROBLEM.md) | HRW / argmax score | Medium |
| 2 | [Jump Consistent Hash](problem-02-jump-consistent-hash/PROBLEM.md) | Jump hash LCG | Medium |
| 3 | [Jump Hash Bucket Distribution](problem-03-jump-hash-distribution/PROBLEM.md) | Bucket assignment | Medium |
