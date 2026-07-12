# Retroactive Stack

A retroactive data structure lets you insert or delete operations *in the past* and then query the present as if history had always included them. A partially-retroactive stack supports inserting a push/pop at an earlier time and asking for the current top — implemented here by replaying the timeline of operations after each edit.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Partially-Retroactive Stack](problem-01-retroactive-stack/PROBLEM.md) | Timeline replay | Hard |
