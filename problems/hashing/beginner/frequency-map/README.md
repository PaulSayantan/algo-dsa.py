# Frequency Map (Counting)

A **frequency map** is a hash map from *element -> count*. Where a set only remembers presence, a frequency map answers *"how many times?"* — the key to anagram checks, majority/most-common queries, and "do I have enough of each?" problems. Python's `collections.Counter` is a dict subclass tailored for exactly this: build it in one linear pass, then compare, subtract, or rank counts. Two multisets are equal iff their counters are equal.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Valid Anagram](problem-01-valid-anagram/PROBLEM.md) | Counter equality | Easy |
| 2 | [First Unique Character in a String](problem-02-first-unique-character/PROBLEM.md) | Count then locate | Easy |
| 3 | [Majority Element](problem-03-majority-element/PROBLEM.md) | Most-common count | Easy |
| 4 | [Ransom Note](problem-04-ransom-note/PROBLEM.md) | Count-covering check | Easy |
| 5 | [Find the Difference](problem-05-find-the-difference/PROBLEM.md) | Counter subtraction | Easy |
| 6 | [Sort Characters By Frequency](problem-06-sort-characters-by-frequency/PROBLEM.md) | Rank by count | Medium |
