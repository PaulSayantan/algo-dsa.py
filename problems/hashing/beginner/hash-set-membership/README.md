# Hash Set Membership Testing

A **hash set** answers one question extremely well: *"have I seen this value before?"* Insertion, deletion, and membership tests all run in expected **O(1)**, turning many quadratic scans into single linear passes. The pattern is always the same: walk the input once, ask `x in seen` before acting, then `seen.add(x)`. It underlies duplicate checks, cycle detection, complement lookups, and "is every required element present?" queries.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Contains Duplicate](problem-01-contains-duplicate/PROBLEM.md) | Seen-set membership | Easy |
| 2 | [Happy Number](problem-02-happy-number/PROBLEM.md) | Cycle detection via set | Easy |
| 3 | [Single Number](problem-03-single-number/PROBLEM.md) | Pair cancellation in a set | Easy |
| 4 | [Missing Number](problem-04-missing-number/PROBLEM.md) | Presence set over a known range | Easy |
| 5 | [Two-Sum Existence](problem-05-two-sum-exists/PROBLEM.md) | Complement lookup in a set | Easy |
| 6 | [Check if the Sentence Is Pangram](problem-06-check-if-pangram/PROBLEM.md) | Distinct-letter set size | Easy |
