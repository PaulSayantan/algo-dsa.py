# Strongly Connected Components

**Difficulty:** Hard

**Source:** Classic — Tarjan's SCC

## Description

Given a directed graph as `n` (vertices `0..n-1`) and an edge list `edges`, find its strongly connected components using Tarjan's algorithm. Return the components as a sorted list of sorted vertex lists (canonical form).

## Hint

DFS with discovery/low-link and an on-stack set; pop an SCC when low[v] == disc[v].
