# Palindrome Check via Deque

A deque makes palindrome testing read like its definition: repeatedly pop the front and the back and check they match. When only zero or one element remains, every mirrored pair agreed and the sequence is a palindrome. It's O(n) time and works uniformly on strings and arrays. Filtering the input first (keeping only alphanumerics, lowercased) yields the LeetCode 125 "valid palindrome" variant.

## Problems

| # | Problem | Technique focus | Difficulty |
|---|---------|-----------------|------------|
| 1 | [Palindrome Check with a Deque](problem-01-palindrome-deque/PROBLEM.md) | Front/back compare | Easy |
| 2 | [Valid Palindrome (Alphanumeric Only)](problem-02-valid-palindrome/PROBLEM.md) | Filtered palindrome | Easy |
| 3 | [Palindrome Linked List](problem-03-palindrome-linked-list/PROBLEM.md) | Values into deque, front/back compare | Easy |
| 4 | [Palindrome Number](problem-04-palindrome-number/PROBLEM.md) | Digits into deque, front/back compare | Easy |
| 5 | [First Palindromic String in the Array](problem-05-first-palindromic-string/PROBLEM.md) | Per-word deque palindrome check | Easy |
