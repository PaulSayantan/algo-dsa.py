# Versioned Persistent Stack

**Difficulty:** Hard

**Source:** Classic — persistent (functional) stack

## Description

Implement a persistent stack. `push(version, x)` returns a new version id for the stack with `x` on top of `version`; `pop(version)` returns `(new_version, popped_value)`; `top(version)` peeks; `empty(version)` tests emptiness. Version `0` is the initial empty stack. Old versions stay valid after later operations.

## Hint

Represent each version as a node (value, parent-node); share structure. Keep a list of version heads.
