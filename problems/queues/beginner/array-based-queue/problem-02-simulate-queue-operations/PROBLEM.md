# Simulate Queue Operations

**Difficulty:** Easy

**Source:** Classic — op-sequence simulation

## Description

Given a list of operations — each of `["enqueue", v]`, `["dequeue"]`, `["front"]`, or `["empty"]` — apply them to an initially empty FIFO queue and return the list of results, one per **query** operation (`dequeue`, `front`, `empty`), in the order they occur.

## Hint

Maintain a list; enqueue appends, dequeue pops index 0, front reads index 0, empty checks the length.
