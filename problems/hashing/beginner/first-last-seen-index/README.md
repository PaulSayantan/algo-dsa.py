# First-Seen / Last-Seen Index

Rather than storing counts, this technique stores an *index* per value — either the FIRST place it appeared or the MOST RECENT one. The most-recent index detects nearby duplicates and lets a sliding window jump past a repeat in O(1); the first index measures how far apart equal values can sit. It is the positional cousin of frequency counting and the backbone of no-repeat-window problems.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Contains Duplicate II](problem-01-contains-duplicate-ii/PROBLEM.md) | Last-seen index gap | Easy |
| 2 | [Longest Substring Without Repeating Characters](problem-02-longest-substring-without-repeating/PROBLEM.md) | Last-seen window jump | Medium |
| 3 | [Maximum Distance Between Equal Values](problem-03-max-distance-equal-values/PROBLEM.md) | First-seen index | Easy |
| 4 | [Minimum Distance Between Equal Values](problem-04-min-distance-equal-values/PROBLEM.md) | Last-seen index | Easy |
| 5 | [First Repeating Element](problem-05-first-repeating-element/PROBLEM.md) | Count then first-index scan | Easy |
| 6 | [First and Last Occurrence via Hash Map](problem-06-first-and-last-occurrence/PROBLEM.md) | First-seen + last-seen maps | Easy |
