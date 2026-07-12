# Doubly-Linked-List Deque

A deque can also be built from a **doubly linked list**: each node stores `prev` and `next`, so inserting or removing at either end is O(1) worst-case with no resizing. Using two sentinel (dummy) nodes for the head and tail removes all the null-pointer edge cases — every real node always has a neighbor on both sides. This is exactly how CPython's `collections.deque` is structured internally (as a linked list of blocks).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Design a Doubly-Linked Deque](problem-01-design-linked-deque/PROBLEM.md) | Sentinel nodes, O(1) ends | Easy |
| 2 | [Interleaved Deque Operations](problem-02-interleaved-deque-ops/PROBLEM.md) | Interleaved both-end ops | Easy |
| 3 | [Design Circular Deque](problem-03-design-circular-deque/PROBLEM.md) | Fixed capacity, isFull/isEmpty | Easy |
| 4 | [Palindrome Check with a Deque](problem-04-palindrome-check-deque/PROBLEM.md) | Both-end pop-and-compare | Easy |
| 5 | [Moving Average from Data Stream](problem-05-moving-average-stream/PROBLEM.md) | Sliding window + running sum | Easy |
