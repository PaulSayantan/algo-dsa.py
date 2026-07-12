# Strongly Connected Components (Gabow)

**Difficulty:** Hard

**Source:** Classic — Gabow's two-stack SCC

## Description

Given a directed graph as `n` and an edge list `edges`, find its strongly connected components using Gabow's two-stack algorithm. Return the components as a sorted list of sorted vertex lists.

## Hint

Keep a path stack and a boundary stack; on a back edge pop boundaries until the target's order; close an SCC at a boundary match.
