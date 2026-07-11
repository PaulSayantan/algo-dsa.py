# Solution — Longest Common Path

Let `n = len(paths)` and `m = ` the fewest segments in any path. The result has at most
`m` segments.

## Brute Force

Compute the raw longest common *character* prefix of all paths (LeetCode 14 style), then
"walk back" to the last complete `/` boundary so you do not cut a segment in half.

The subtlety that trips people up: the character-LCP boundary is not always a valid path
boundary — `"/usr/lib"` vs `"/usr/libexec"` has character-LCP `"/usr/lib"`, and you must
retreat to `"/usr"`. Getting the trimming rules right (trailing slash? one path being a
true directory prefix of another?) is error-prone.

**Time:** `O(S)` to scan characters, where `S` is total characters. **Space:** `O(m)`.
It works, but treating characters as the unit invites boundary bugs, so we prefer to make
segments the unit directly.

## Optimal Approach — Vertical Scan on Segments

Split each path into its list of non-empty segments, then apply the vertical LCP scan
**with segments as the atoms** (instead of characters).

```python
def longest_common_path(paths: List[str]) -> str:
    seg_lists = [[p for p in path.split("/") if p] for path in paths]
    reference = seg_lists[0]
    common = 0                                   # number of matching leading segments
    for j, seg in enumerate(reference):          # segment column j
        if any(j >= len(sl) or sl[j] != seg for sl in seg_lists):
            break
        common += 1
    return "/" + "/".join(reference[:common])
```

**Why it is correct.** The loop invariant is *"the first `common` segments are shared by
every path."* We extend `common` only when an entire segment column matches, and stop at
the first column where some path is shorter or holds a different segment — at which point
no longer segment-aligned prefix can exist. Joining those segments and prepending `/`
yields a valid normalized path; when `common == 0` the join is empty and we return `"/"`,
the root shared by all absolute paths.

**Step by step for Example 1** (`[usr, local, bin]`, `[usr, local, lib]`,
`[usr, local, bin, python]`):

| column j | segments down the column | verdict |
|----------|--------------------------|---------|
| 0        | usr, usr, usr            | match (common=1) |
| 1        | local, local, local      | match (common=2) |
| 2        | bin, lib, bin            | mismatch -> stop |

Return `"/" + "/".join(["usr", "local"]) = "/usr/local"`.

**Time:** `O(S)` to split plus `O(n * L)` to scan, where `L` is the answer length in
segments — overall linear in the input size. **Space:** `O(S)` to hold the segment lists
(`O(1)` beyond that if you index into strings without materializing lists).

## Binary Search on Segment Count

`shared(L) = ` "do all paths agree on their first `L` segments?" is monotonic, so binary
search the largest `L` in `[0, m]`:

```python
def shared(seg_lists, L):
    ref = seg_lists[0]
    return all(len(sl) >= L and sl[:L] == ref[:L] for sl in seg_lists)
```

`O(log m)` guesses, each an `O(n * L)` check -> `O(n * m * log m)`. Handy when segment
equality is cheap (e.g. hash each segment once) or when only the depth is needed.

## Key Insights & Edge Cases

- **Segments, not characters, are the comparison unit** — this is the whole point and the
  fix for the `"/usr/lib"` vs `"/usr/libexec"` trap.
- **Single path:** returns that path (normalized), since nothing breaks the scan.
- **Shortest path caps the answer** — a path that is itself a directory prefix of the
  others (e.g. `"/data/logs"`) limits `common` to its own segment count.
- **No common first segment:** return `"/"` (root), never `""`.
- **Normalization:** dropping empty pieces from `split("/")` cleanly handles the leading
  slash, trailing slashes, and accidental `//`.
- Trailing `.` or `..` segments are treated as ordinary text here; if logical path
  resolution is required, canonicalize before comparing.
