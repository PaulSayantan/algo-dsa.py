# Solution — Longest Palindromic Substring

## Brute Force

Check every substring for the palindrome property and keep the longest.

- Enumerate `O(n^2)` substrings and test each in `O(n)` → `O(n^3)` time.
- With DP palindrome tables (`is_pal[i][j]`) it drops to `O(n^2)` time and
  `O(n^2)` space.
- Expand-around-center gives `O(n^2)` time, `O(1)` extra space; Manacher's
  algorithm gives `O(n)` time. These are the classic answers for LeetCode 5.

We use the **eertree** because it generalizes: the same structure answers
counting, occurrence, and factorization questions on the same string.

## Optimal Approach — Palindromic Tree (Eertree)

### Idea

Each node of the eertree is a distinct palindromic substring and stores its
`length`. The longest palindromic substring is therefore the **node with the
maximum length**. To output the actual characters, remember for each node the
end index at which it was created; then the palindrome is
`s[end - length + 1 : end + 1]`.

### Why this is correct

The eertree, after processing all of `s`, contains a node for **every** distinct
palindromic substring of `s` (construction adds one node the first time each
palindrome appears as the longest palindromic suffix of a prefix). Since it
contains all palindromic substrings, the maximum-length node is a longest
palindromic substring. The stored end index recovers a genuine occurrence
because we set it exactly when the palindrome was created as a suffix of the
prefix ending at that index.

### Steps

1. Initialize the two roots (len `-1`, len `0`).
2. For each `i`, `add(s[i])`:
   - climb suffix links from `last` to find the node that `s[i]` can extend;
   - if the extended palindrome is new, create a node with
     `length = parent_len + 2` and record `end_index = i`; assign its suffix
     link by climbing from the parent's suffix link.
3. After the build, scan the nodes for the maximum `length` and reconstruct the
   substring from its stored `end_index`.

### Reference implementation

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        length = [-1, 0]
        suffix = [0, 0]
        edges = [dict(), dict()]
        end_idx = [-1, -1]        # end position where the node was created
        last = 1

        def get_link(v: int, i: int) -> int:
            while i - length[v] - 1 < 0 or s[i - length[v] - 1] != s[i]:
                v = suffix[v]
            return v

        for i, c in enumerate(s):
            cur = get_link(last, i)
            if c in edges[cur]:
                last = edges[cur][c]
                continue
            new = len(length)
            length.append(length[cur] + 2)
            edges.append(dict())
            end_idx.append(i)
            if length[new] == 1:
                suffix.append(1)
            else:
                link = get_link(suffix[cur], i)
                suffix.append(edges[link][c])
            edges[cur][c] = new
            last = new

        best = max(range(2, len(length)), key=lambda v: length[v], default=None)
        if best is None:          # empty string only
            return ""
        L, e = length[best], end_idx[best]
        return s[e - L + 1 : e + 1]
```

- **Time:** `O(n · log |Σ|)` to build plus `O(n)` to scan nodes.
- **Space:** `O(n)` nodes and edges.

## Key Insights & Edge Cases

- **Reconstruct from an end index, not a start index.** A palindrome created at
  index `i` occupies `s[i - length + 1 : i + 1]`; recording `i` at creation time
  is the simplest way to recover the characters.
- **Ties** are allowed by the problem — `"babad"` may return `"bab"` or `"aba"`;
  taking the first max-length node is fine.
- **Single character** (`"a"`): one node of length 1, answer `"a"`.
- **No multi-char palindrome** (`"abc"`): all nodes have length 1, answer is any
  single character (e.g. `"a"`).
- **Empty string** guarded up front returns `""` (no non-root nodes exist).
- For pure LeetCode 5 within its small constraints, Manacher / expand-around-
  center are simpler; prefer the eertree when the same string will be queried
  for several palindrome statistics.
