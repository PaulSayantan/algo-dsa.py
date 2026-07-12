# Fully-Persistent Deque

**Difficulty:** Hard

**Source:** Classic — persistent deque (cf. Library Checker persistent_queue)

## Description

Implement a fully persistent deque. Each operation takes a version index and returns a new version: `pushBack(v, x)`, `pushFront(v, x)`, `popFront(v)` and `popBack(v)` (return `(new_version, value)`), plus `front(v)`/`back(v)` peeks. Version 0 is empty. Any past version can be operated on again, branching history.

## Hint

Store each version as an immutable tuple of contents; each op builds a new tuple sharing nothing observable.
