# Count and Say

**Difficulty:** Medium

Source: LeetCode 38 — "Count and Say"

## Description

The **count-and-say** sequence is a sequence of digit strings defined by the
recurrence:

- `countAndSay(1) = "1"`.
- `countAndSay(n)` is obtained by reading `countAndSay(n - 1)` aloud as
  consecutive runs and writing, for each run, the run length followed by the
  digit. This "read it aloud" step is exactly **Run-Length Encoding** in
  `count + digit` order.

For example, to produce the term after `"3322251"`: there are two `3`s, three
`2`s, one `5`, one `1`, which is written `"23" + "32" + "15" + "11"` =
`"23321511"`.

Given a positive integer `n`, return the `n`-th term of the count-and-say
sequence.

## Constraints

- `1 <= n <= 30`

## Examples

### Example 1
```
Input:  n = 1
Output: "1"
Explanation: The base case, by definition.
```

### Example 2
```
Input:  n = 4
Output: "1211"
Explanation:
  countAndSay(1) = "1"
  countAndSay(2) = RLE("1")    = "11"    (one 1)
  countAndSay(3) = RLE("11")   = "21"    (two 1s)
  countAndSay(4) = RLE("21")   = "1211"  (one 2, then one 1)
```

### Example 3
```
Input:  n = 6
Output: "312211"
Explanation: Continuing the chain:
  countAndSay(5) = RLE("1211")   = "111221"  (one 1, one 2, two 1s)
  countAndSay(6) = RLE("111221") = "312211"  (three 1s, two 2s, one 1)
```

## Hint

Each term is just the **Run-Length Encoding** of the previous term written as
`count` then `digit`. Start from `"1"` and apply the RLE "say" step `n - 1` times.
