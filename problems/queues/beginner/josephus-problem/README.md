# Josephus Problem

In the Josephus problem, `n` people stand in a circle and every `k`-th person is eliminated until one survivor remains. A queue models the circle directly: rotate the front `k-1` people to the back (they are skipped), then dequeue the `k`-th (eliminated). Repeat until one is left. The same loop, recording each removed person, yields the full elimination order.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Josephus Survivor](problem-01-josephus-survivor/PROBLEM.md) | Circular-queue elimination | Medium |
| 2 | [Josephus Elimination Order](problem-02-elimination-order/PROBLEM.md) | Full elimination sequence | Medium |
| 3 | [Josephus K-th Eliminated](problem-03-kth-eliminated/PROBLEM.md) | Indexing into the elimination order | Easy |
| 4 | [Josephus Last Two Survivors](problem-04-last-two-survivors/PROBLEM.md) | Stopping the loop at two remaining | Easy |
| 5 | [Josephus Circle of Names](problem-05-circle-of-names/PROBLEM.md) | Circular elimination over labels | Easy |
