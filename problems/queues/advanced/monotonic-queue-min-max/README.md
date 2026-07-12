# Monotonic Queue (Min / Max)

A monotonic queue augments a FIFO queue with a helper deque of candidates so it can report the min or max of its current contents in amortized O(1). Dominated elements are discarded on push; the front of the helper deque is always the current extreme.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Sliding Window Maximum](problem-01-sliding-window-maximum/PROBLEM.md) | Window-max deque | Hard |
| 2 | [Queue with max_value](problem-02-max-queue/PROBLEM.md) | Max-queue design | Medium |
