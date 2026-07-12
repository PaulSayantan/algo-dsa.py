# LFU Cache

An **LFU (least-frequently-used) cache** evicts the entry accessed the fewest times, breaking ties by least-recently-used. The O(1) design keeps a value map, a per-key frequency map, and one `OrderedDict` bucket per frequency (preserving LRU order within a frequency) plus a running `minfreq`. Every access moves a key up one frequency bucket; eviction pops the front of the `minfreq` bucket.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [LFU Cache](problem-01-lfu-cache-design/PROBLEM.md) | Freq buckets + minfreq | Hard |
| 2 | [LFU Cache — Final Contents](problem-02-lfu-final-contents/PROBLEM.md) | Resident-set snapshot | Hard |
