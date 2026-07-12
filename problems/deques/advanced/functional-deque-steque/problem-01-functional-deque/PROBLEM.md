# Immutable Functional Deque

**Difficulty:** Hard

**Source:** Classic — Okasaki functional deque

## Description

Implement a persistent (immutable) deque with a version model. `pushFront(v, x)` / `pushBack(v, x)` return a new version id; `popFront(v)` / `popBack(v)` return `(new_version, value)`; `front(v)` / `back(v)` peek. Version `0` is empty and stays valid after later operations. Use a two-list (front, back) representation.

## Hint

Store each version as (front_tuple, back_tuple); rebalance by halving when a side is empty on a pop.
