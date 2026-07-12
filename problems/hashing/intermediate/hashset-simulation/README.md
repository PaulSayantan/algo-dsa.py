# Hash-Set Simulation & Cycle Detection

When a process iterates a deterministic transition (digit transforms, linear-congruential steps, or following a successor pointer), storing every visited state in a Hash Set detects when it loops. A Hash Map from state to its first-seen step additionally recovers the cycle length. This is the hashing counterpart to Floyd's tortoise-and-hare and the basis of repeated-state and happy-number problems.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Happy Number](problem-01-happy-number/PROBLEM.md) | Seen-set loop detection | Easy |
| 2 | [Find the Duplicate Number (Seen Set)](problem-02-find-duplicate-seen-set/PROBLEM.md) | First repeated element | Medium |
| 3 | [Digit-Square Sequence Length](problem-03-digit-square-cycle-length/PROBLEM.md) | Distinct states before repeat | Medium |
| 4 | [Steps Until a Sequence Repeats](problem-04-lcg-steps-to-repeat/PROBLEM.md) | Seen-set step counting | Medium |
| 5 | [Cycle Length in a Functional Graph](problem-05-functional-graph-cycle-length/PROBLEM.md) | First-seen step map | Medium |
