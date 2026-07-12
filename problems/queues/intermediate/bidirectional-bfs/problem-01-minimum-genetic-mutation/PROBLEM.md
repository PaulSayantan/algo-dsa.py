# Minimum Genetic Mutation

**Difficulty:** Medium

**Source:** LeetCode 433 — Minimum Genetic Mutation

## Description

A gene string is length-8 over `A C G T`. Given `startGene`, `endGene`, and a `bank` of valid genes, return the minimum number of single-character mutations to transform `startGene` into `endGene` (every intermediate must be in `bank`), or `-1` if impossible.

## Hint

Two frontiers (from start and end); expand the smaller; a state in the other frontier means they meet.
