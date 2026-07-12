# Cycle Length in a Functional Graph

**Difficulty:** Medium

**Source:** Classic — successor-array cycle length

## Description

Given a functional graph as a successor array `succ` (each node has exactly one outgoing edge `i -> succ[i]`), follow edges from `start` until a node repeats, and return the length of the cycle you enter.

## Hint

Map each node to the step it was first seen; the cycle length is now - first-seen step.
