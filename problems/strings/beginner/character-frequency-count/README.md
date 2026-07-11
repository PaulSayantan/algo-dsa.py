# Character Frequency Count

**Character Frequency Count** (also called a *tally array* or *count array*) is a
foundational string/array technique. You allocate a small fixed-size integer
array — `26` for lowercase English letters, `52` for mixed case, `128` for ASCII,
or `256` for all bytes — and use each character's numeric code as an index into
that array. Every time you see a character you increment its bucket; to compare or
undo you decrement.

Because the array size is a constant that does not grow with the input, tallying
`n` characters costs **O(n)** time and **O(1)** extra space (the alphabet size is
a fixed constant). This beats sorting-based approaches (O(n log n)) and beats
nested-loop scanning (O(n^2)) for the same questions.

## When to reach for it

- Deciding whether two strings are **anagrams** (same multiset of characters).
- Checking **uniqueness** (does any character repeat? which is the first unique one?).
- Verifying one string can be **built from** the characters of another.
- Finding the **most / least frequent** character, or sorting by frequency.
- Producing a **canonical signature** for a string so anagrams collapse to one key.
- Any question of the form "how many of each character?" where the alphabet is small.

The Python idiom is either a `list` of length `26`/`128` indexed by
`ord(ch) - ord('a')`, or `collections.Counter`, which is a hash-map generalization
of the same idea and works for any (even unbounded) alphabet.

## Complexity at a glance

| Metric | Cost |
| --- | --- |
| Build the tally over a string of length `n` | O(n) time |
| Extra space | O(k) where `k` is the alphabet size — O(1) when `k` is fixed |
| Compare two full tallies | O(k) time |

## Problems

| # | Problem | Summary | Difficulty |
| --- | --- | --- | --- |
| 1 | [Valid Anagram](problem-01-valid-anagram/PROBLEM.md) | Do two strings contain exactly the same characters with the same counts? | Easy |
| 2 | [Ransom Note](problem-02-ransom-note/PROBLEM.md) | Can a note be assembled from the letters available in a magazine? | Easy |
| 3 | [First Unique Character in a String](problem-03-first-unique-character/PROBLEM.md) | Return the index of the first non-repeating character. | Easy |
| 4 | [Find the Difference](problem-04-find-the-difference/PROBLEM.md) | Find the one extra letter added when `s` is shuffled into `t`. | Easy |
| 5 | [Sort Characters By Frequency](problem-05-sort-characters-by-frequency/PROBLEM.md) | Rebuild a string with characters ordered by decreasing frequency. | Medium |
| 6 | [Group Anagrams](problem-06-group-anagrams/PROBLEM.md) | Group words that are anagrams of one another using a frequency signature. | Medium |
