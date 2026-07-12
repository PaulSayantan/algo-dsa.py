# Reverse a Queue

A queue preserves order, so to *reverse* it you borrow a **stack**: dequeue every element and push it, then pop them all back — LIFO undoes FIFO. This is the classic bridge between the two structures, and a small twist (reverse only the first k) shows how a stack lets you flip a prefix while leaving the remainder untouched. Both run in O(n).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Reverse a Queue](problem-01-reverse-queue/PROBLEM.md) | Stack-assisted reversal | Easy |
| 2 | [Reverse First K Elements of a Queue](problem-02-reverse-first-k/PROBLEM.md) | Reverse a prefix | Medium |
| 3 | [Reverse Last K Elements of a Queue](problem-03-reverse-last-k/PROBLEM.md) | Reverse a suffix | Easy |
| 4 | [Palindrome Check on a Queue](problem-04-queue-palindrome-check/PROBLEM.md) | Reverse-and-compare | Easy |
| 5 | [Reverse a Queue in Groups of K](problem-05-reverse-queue-in-groups/PROBLEM.md) | Reverse each block | Easy |
