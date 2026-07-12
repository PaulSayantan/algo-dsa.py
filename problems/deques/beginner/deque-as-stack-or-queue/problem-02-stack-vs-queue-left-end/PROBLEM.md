# Deque as Stack vs Queue (Left End)

**Difficulty:** Easy

**Source:** Classic — deque duality

## Description

Mirror the previous problem driving the left end: `leftEndStack(values)` does `appendleft` then `popleft` (both on the left end) for LIFO, while `frontToBackQueue(values)` does `appendleft` then `pop` (opposite ends) for FIFO. Return each pop sequence. The choice of end is arbitrary — what matters is whether push and pop share an end or use opposite ends.

## Hint

Both ops on the left end -> LIFO; appendleft then pop from the right -> FIFO.
