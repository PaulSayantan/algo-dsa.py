# Build a Cartesian Tree (Parent Array)

**Difficulty:** Hard

**Source:** Classic — Cartesian tree (min-heap by value)

## Description

Given an array `nums` of distinct integers, build the min-Cartesian tree (each node is smaller than its children; an in-order walk yields the original array order) using a monotonic stack. Return the parent index of each element, with the root's parent as `-1`.

## Hint

Increasing stack; pop values > current, the last popped becomes current's left child, stack top its parent.
