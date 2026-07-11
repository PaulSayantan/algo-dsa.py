# Longest Common Path

**Difficulty:** Medium

Source: Classic systems/interview problem ("longest common directory of a set of file
paths"); a segment-wise variant of LeetCode 14.

## Description

You are given a list of absolute Unix-style file paths, e.g.
`"/usr/local/bin/python"`. Return the **longest common directory prefix** shared by every
path, as a normalized path string.

The key twist: the common prefix must align on **whole path segments** (the parts between
`/`), not on arbitrary characters. For example `"/usr/lib"` and `"/usr/libexec"` share
the character prefix `"/usr/lib"`, but their longest common *path* is only `"/usr"` — the
segment `"lib"` differs from `"libexec"`.

Rules for the output:
- Split each path on `/`, drop empty pieces (from the leading `/` or any doubled `//`),
  producing a list of segments.
- Find the longest list of segments that is a **prefix of every** path's segment list.
- Return it joined as `"/" + "/".join(common_segments)`. If there are no common
  segments, return `"/"` (the root, which every absolute path shares).

## Constraints

- `1 <= paths.length <= 10^4`
- Each path starts with `/` and has length `1 <= len <= 3000`.
- Segments consist of letters, digits, `.`, `-`, and `_`.
- Comparison is case-sensitive.

## Examples

### Example 1
- **Input:** `paths = ["/usr/local/bin", "/usr/local/lib", "/usr/local/bin/python"]`
- **Output:** `"/usr/local"`
- **Explanation:** As segment lists: `[usr, local, bin]`, `[usr, local, lib]`,
  `[usr, local, bin, python]`. Column 0 is `usr` everywhere, column 1 is `local`
  everywhere, column 2 reads `bin`, `lib`, `bin` — a mismatch — so the common path is
  `/usr/local`.

### Example 2
- **Input:** `paths = ["/usr/lib", "/usr/libexec"]`
- **Output:** `"/usr"`
- **Explanation:** Segment lists `[usr, lib]` and `[usr, libexec]` agree only on `usr`.
  The character prefix `"/usr/lib"` is *not* a valid path prefix because `lib` and
  `libexec` are different segments.

### Example 3
- **Input:** `paths = ["/a/b/c", "/x/y/z"]`
- **Output:** `"/"`
- **Explanation:** The very first segments differ (`a` vs `x`), so the only shared path
  is the root `/`.

### Example 4
- **Input:** `paths = ["/data/logs", "/data/logs/2026", "/data/logs/2026/07"]`
- **Output:** `"/data/logs"`
- **Explanation:** `[data, logs]` is a prefix of all three segment lists; the shortest
  path caps the common prefix at 2 segments.

## Hint

Use the **Longest Common Prefix (vertical/binary)** technique — but on the *segment
lists* rather than raw characters. Scan segment columns left to right until one disagrees
(or a path runs out of segments), or binary search on the number of common segments.
