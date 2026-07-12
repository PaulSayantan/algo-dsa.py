# Minimum / Constrained Covering Window

This family finds the smallest (or otherwise most constrained) window that covers a requirement. The canonical shape uses **two frequency maps** — `need` (what the target demands) versus `have` (what the current window supplies) — plus a single 'satisfaction' counter so you can test coverage in O(1) instead of comparing whole maps. You grow the right edge until the window is satisfied, then greedily shrink the left edge while it stays satisfied, recording the best window each time. Related variants replace the coverage test with a validity test (e.g. window length minus the most frequent char must be within a replacement budget).

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Minimum Window Substring](problem-01-minimum-window-substring/PROBLEM.md) | need/have maps + satisfaction counter | Hard |
| 2 | [Longest Repeating Character Replacement](problem-02-longest-repeating-char-replacement/PROBLEM.md) | Validity window: len - max_freq <= k | Medium |
| 3 | [Smallest Subarray Covering All Distinct Elements](problem-03-smallest-distinct-window/PROBLEM.md) | Cover all distinct, minimize length | Medium |
| 4 | [Minimum Window Covering a Multiset Target](problem-04-min-window-multiset/PROBLEM.md) | Multiset coverage, minimal length | Medium |
| 5 | [Replace the Substring for Balanced String](problem-05-balanced-string-replacement/PROBLEM.md) | Shrink window whose complement is balanceable | Medium |
