# Round-Robin Completion Order

**Difficulty:** Medium

**Source:** Classic — round-robin CPU scheduling

## Description

Given `burst` times for processes `0..n-1` (in arrival order) and a time `quantum`, simulate round-robin scheduling and return the list of process ids in the order they *complete*.

## Hint

Queue of (id, remaining); each turn run min(quantum, remaining); requeue if work remains, else record completion.
