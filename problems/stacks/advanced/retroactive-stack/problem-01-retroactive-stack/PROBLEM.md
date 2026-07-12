# Partially-Retroactive Stack

**Difficulty:** Hard

**Source:** Classic — retroactive data structures (Demaine)

## Description

Implement a partially-retroactive stack over a timeline of operations. `insertPush(t, x)` inserts a *push x* at time `t`; `insertPop(t)` inserts a *pop* at time `t`; `top()` returns the top of the stack after applying the full timeline in time order (or `-1` if empty). Times are inserted in arbitrary order; ties break by insertion order.

## Hint

Keep the timeline as an ordered list of ops; after each edit, replay all ops in time order to answer top().
