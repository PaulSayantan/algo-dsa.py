# Circular Deque — Empty Handling and Wrap-Around

**Difficulty:** Medium

**Source:** LeetCode 641 — Design Circular Deque (variant sequence)

## Description

Exercise the same circular deque on a capacity-2 buffer, focusing on the boundary cases: querying an empty deque must return `-1`, deleting from an empty deque returns `False`, inserting into a full deque returns `False`, and repeated inserts/deletes must correctly wrap the head index around the physical array.

## Hint

getFront/getRear return -1 when count is 0; insert fails when count == capacity. Indices wrap with modulo.
