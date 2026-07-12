# Count-Min Sketch

A **Count-Min Sketch** estimates item frequencies in a stream using a `d x w` table of counters and one hash per row. `update(x, c)` adds `c` to counter `(r, h_r(x))` in every row; `estimate(x)` returns the **minimum** of those `d` counters. Because collisions only ever *add* to a counter, the estimate is one-sided: `estimate(x) >= true_count(x)`, never less. Picking small collision-free inputs makes the estimate exact and hand-checkable.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Design Count-Min Sketch](problem-01-design-count-min-sketch/PROBLEM.md) | d rows, min estimate | Medium |
| 2 | [Frequency Estimation over a Stream](problem-02-stream-frequency-estimation/PROBLEM.md) | Streaming counts | Medium |
