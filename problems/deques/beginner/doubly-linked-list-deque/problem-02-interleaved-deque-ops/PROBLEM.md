# Interleaved Deque Operations

**Difficulty:** Easy

**Source:** Classic — doubly-linked-list deque ADT

## Description

Using the doubly-linked-list deque, process an interleaved sequence of front/back pushes and pops and report the value returned by each pop. This confirms that pushes and pops at opposite ends do not interfere and that ordering is preserved.

## Hint

Front pushes prepend, back pushes append; a popFront returns the most-recently front-pushed remaining item.
