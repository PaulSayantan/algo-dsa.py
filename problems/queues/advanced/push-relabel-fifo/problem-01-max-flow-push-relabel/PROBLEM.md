# Maximum Flow (FIFO Push–Relabel)

**Difficulty:** Hard

**Source:** Classic — FIFO push–relabel max-flow

## Description

Given `n` nodes, directed capacity edges `[u, v, cap]`, a source `s`, and a sink `t`, return the maximum flow from `s` to `t` using the FIFO push–relabel method (a queue of active nodes).

## Hint

Initialize preflow from s (height n); push excess to lower neighbors, relabel when stuck; queue active nodes.
