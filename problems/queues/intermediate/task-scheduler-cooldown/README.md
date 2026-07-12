# Task Scheduler / Cooldown

Scheduling identical tasks with a mandatory cooldown between repeats is a queue/greedy problem: run the most frequent available task, park it in a cooldown queue with its ready-time, and advance time (idling if nothing is ready). The total time is the answer.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Task Scheduler](problem-01-task-scheduler/PROBLEM.md) | Cooldown scheduling | Medium |
| 2 | [Reorganize String](problem-02-reorganize-string/PROBLEM.md) | Cooldown with n=1 (max-heap) | Medium |
| 3 | [Rearrange String k Distance Apart](problem-03-rearrange-string-k-distance-apart/PROBLEM.md) | Cooldown queue of length k | Medium |
| 4 | [Task Scheduler II](problem-04-task-scheduler-ii/PROBLEM.md) | Per-type next-available day | Medium |
| 5 | [Distant Barcodes](problem-05-distant-barcodes/PROBLEM.md) | Cooldown fill even-then-odd | Medium |
