# Sort a Stack

You can sort a stack using only one auxiliary stack: repeatedly pop from the source and insert into the auxiliary in sorted order, temporarily moving back any elements that are out of place. It's insertion sort expressed with stack pushes and pops — O(n²) but using no other data structure.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Sort a Stack Using One Auxiliary Stack](problem-01-sort-stack/PROBLEM.md) | Insertion via aux stack | Medium |
| 2 | [Sort a Stack Using Recursion](problem-02-sort-stack-recursion/PROBLEM.md) | Recursive sort + sorted insert | Medium |
| 3 | [Insert an Element into a Sorted Stack](problem-03-insert-into-sorted-stack/PROBLEM.md) | Recursive sorted insert primitive | Medium |
| 4 | [Design a Self-Sorting Stack](problem-04-sortable-stack-design/PROBLEM.md) | Incremental insertion on push | Medium |
| 5 | [Sort a Stack in Descending Order](problem-05-sort-stack-descending/PROBLEM.md) | Aux-stack insertion (flipped compare) | Medium |
