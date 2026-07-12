# Queue with max_value

**Difficulty:** Medium

**Source:** LCOF 59-II — Queue with max_value (design)

## Description

Design a queue supporting `push_back(x)`, `pop_front()` (return the dequeued value or `-1` if empty), and `max_value()` (the maximum current element, or `-1` if empty) — all in amortized O(1).

## Hint

Keep the data queue plus a helper deque of decreasing candidates; front of the helper is the max.
