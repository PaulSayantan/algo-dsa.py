# Count Multi-Pattern Occurrences

**Difficulty:** Hard

**Source:** Classic — Aho–Corasick automaton

## Description

Given a list of `patterns` and a `text`, return the total number of occurrences of all patterns in `text` (overlaps count; duplicate patterns count each time). Build the Aho–Corasick automaton with BFS failure links and scan the text once.

## Hint

Build a trie; BFS to set failure links and output counts; then walk the text following goto/fail links.
