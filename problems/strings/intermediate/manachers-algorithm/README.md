# Manacher's Algorithm

**Manacher's Algorithm** finds, in a single **O(n)** pass, the longest palindromic
substring centered at *every* position of a string. From that one array of
palindrome radii you can answer almost any palindrome-substring question
(longest palindrome, count of all palindromic substrings, longest palindromic
prefix/suffix, O(1) "is `s[i..j]` a palindrome?" queries, and more) without ever
paying the naive O(n^2) or O(n^3) cost.

## The Core Idea

A naive "expand around center" scan is O(n^2): for each of the ~2n centers
(n character centers + n-1 gap centers) you expand outward until the palindrome
breaks. Manacher makes this linear by **reusing work already done**. It keeps
track of the palindrome that currently reaches farthest to the right (its center
`c` and right boundary `r`). For a new center `i` inside that palindrome, the
palindrome at `i`'s mirror position `2*c - i` gives a free lower bound on the
radius at `i`, so expansion only ever starts from that bound. Because the right
boundary `r` only moves forward, the total expansion work across all centers is
O(n), giving overall **O(n) time** and **O(n) space**.

To handle even- and odd-length palindromes uniformly, the string is first
transformed by inserting a separator (e.g. `#`) between every character and at
both ends: `"abba"` becomes `"#a#b#b#a#"`. Every palindrome in the transformed
string has odd length, and the radius array maps directly back to real
substring lengths.

## When to Reach for It

- You need the **longest palindromic substring** and O(n^2) is too slow (large n).
- You need to **count all palindromic substrings**, or answer many palindrome
  queries over the same string.
- You need the **longest palindromic prefix or suffix** (e.g. to build the
  shortest palindrome by prepending/appending characters).
- You need **O(1) palindrome membership** checks `is s[i..j] a palindrome?`
  after O(n) preprocessing, often inside a larger DP or two-pointer scan.

If you only need a *single* palindrome check, or n is tiny, plain
expand-around-center is simpler and fast enough. Manacher shines when the
palindrome structure of the whole string must be known cheaply.

**Time:** O(n)   **Space:** O(n)

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Longest Palindromic Substring](problem-01-longest-palindromic-substring/PROBLEM.md) | Return the longest contiguous palindromic substring | Medium |
| 2 | [Palindromic Substrings (Count)](problem-02-palindromic-substrings-count/PROBLEM.md) | Count how many substrings are palindromes | Medium |
| 3 | [Shortest Palindrome](problem-03-shortest-palindrome/PROBLEM.md) | Prepend fewest chars to make the whole string a palindrome | Hard |
| 4 | [Palindrome Partitioning IV](problem-04-palindrome-partitioning-iv/PROBLEM.md) | Can the string be split into exactly 3 palindromes? | Hard |
| 5 | [Maximum Product of Two Palindromic Substrings](problem-05-maximum-product-two-palindromic-substrings/PROBLEM.md) | Max product of lengths of two non-overlapping odd palindromes | Hard |
