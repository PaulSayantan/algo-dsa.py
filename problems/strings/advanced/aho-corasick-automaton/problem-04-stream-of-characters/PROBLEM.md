# Stream of Characters

**Difficulty:** Hard

**Source:** LeetCode 1032 — Stream of Characters

## Description

Design an algorithm that accepts a stream of characters and checks, after each
new character arrives, whether some suffix of the characters queried so far
spells one of a fixed set of `words`.

Implement the `StreamChecker` class:

- `StreamChecker(words)` — initializes the object with the array of strings
  `words`.
- `query(letter)` — accepts a new character from the stream and returns `True`
  if **any** word in `words` is a **suffix** of the string formed by the stream
  of characters queried so far (in order); otherwise returns `False`.

Because characters arrive one at a time and you must answer immediately, you
cannot re-scan the whole history on every query — you need an online matcher.

## Constraints

- `1 <= words.length <= 2000`
- `1 <= words[i].length <= 200`
- `words[i]` consists of lowercase English letters.
- `letter` is a lowercase English letter.
- At most `4 * 10^4` calls will be made to `query`.

## Examples

### Example 1

```
Input:
["StreamChecker", "query", "query", "query", "query", "query", "query",
 "query", "query", "query", "query", "query", "query"]
[[["cd","f","kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"],
 ["i"], ["j"], ["k"], ["l"]]

Output:
[null, false, false, false, true, false, true, false, false, false, false,
 false, true]

Explanation:
StreamChecker sc = new StreamChecker(["cd","f","kl"]);
sc.query("a"); // "a"            -> no word is a suffix -> false
sc.query("b"); // "ab"           -> false
sc.query("c"); // "abc"          -> false
sc.query("d"); // "abcd"         -> "cd" is a suffix    -> true
sc.query("e"); // "abcde"        -> false
sc.query("f"); // "abcdef"       -> "f" is a suffix     -> true
sc.query("g"); // "abcdefg"      -> false
sc.query("h"); // ...            -> false
sc.query("i"); //                -> false
sc.query("j"); //                -> false
sc.query("k"); // "...k"         -> false
sc.query("l"); // "...kl"        -> "kl" is a suffix    -> true
```

### Example 2

```
Input:
["StreamChecker", "query", "query", "query", "query", "query"]
[[["ab","ba"]], ["a"], ["a"], ["b"], ["a"], ["b"]]

Output:
[null, false, false, true, true, true]

Explanation:
stream = "a"      -> false
stream = "aa"     -> false
stream = "aab"    -> "ab" is a suffix -> true
stream = "aaba"   -> "ba" is a suffix -> true
stream = "aabab"  -> "ab" is a suffix -> true
```

## Hint

Build an **Aho–Corasick Automaton** over `words`. Maintain a single "current
node" that advances by one automaton transition per `query`. A word is a suffix
of the stream exactly when the current node (or one of its nodes reachable via
dictionary-suffix links) is terminal — precompute a per-node
"is-any-suffix-a-word" flag so each `query` is `O(1)`.
