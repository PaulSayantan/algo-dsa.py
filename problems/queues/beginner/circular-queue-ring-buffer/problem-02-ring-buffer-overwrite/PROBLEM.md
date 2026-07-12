# Ring Buffer with Overwrite

**Difficulty:** Medium

**Source:** Classic — overwriting ring buffer

## Description

Implement a fixed-capacity ring buffer. `write(x)` appends `x` at the rear; when the buffer is already full it **overwrites the oldest** element (advancing the front). `snapshot()` returns the live elements from oldest to newest, and `size()` returns the current element count (which never exceeds the capacity).

## Hint

When size < capacity just grow; once full, each write advances head so the oldest slot is reused.
