# Compare Version Numbers

**Difficulty:** Medium

**Source:** LeetCode 165 — Compare Version Numbers

## Description

Given two version strings, `version1` and `version2`, compare them.

A version string consists of **revisions** separated by dots `'.'`. Each revision
consists of digits and may contain leading zeros. Every revision has at least one
character. Revisions are **0-indexed from left to right**, with the leftmost
revision being revision 0, the next revision being revision 1, and so on. For
example, `2.5.33` and `0.1` are valid version strings.

To compare version strings, compare their revisions in **left-to-right order**.
Revisions are compared using their **integer value**, ignoring any leading zeros.
This means that revisions `1` and `001` are considered **equal**. If a version
string does not specify a revision at an index, then treat the revision as `0`.
For example, version `1.0` is less than version `1.1` because their revision 0s
are the same, but their revision 1s are `0` and `1` respectively, and `0 < 1`.

Return the following:

- If `version1 < version2`, return `-1`.
- If `version1 > version2`, return `1`.
- Otherwise, return `0`.

## Constraints

- `1 <= version1.length, version2.length <= 500`
- `version1` and `version2` only contain digits and `'.'`.
- `version1` and `version2` are valid version numbers.
- All the given revisions in `version1` and `version2` can be stored in a 32-bit
  integer.

## Examples

**Example 1**

```
Input:  version1 = "1.2", version2 = "1.10"
Output: -1
Explanation: version1's revision 1 is "2" and version2's revision 1 is "10".
Compared as integers, 2 < 10, so version1 < version2.
```

**Example 2**

```
Input:  version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeros, both revision 1s are the integer 1, so the
versions are equal.
```

**Example 3**

```
Input:  version1 = "1.0", version2 = "1.0.0.0"
Output: 0
Explanation: version1 has no revisions at indices 2 and 3; they are treated as 0
and match the trailing zeros of version2, so the versions are equal.
```

## Hint

Use **String Tokenization / Split**: split each version on `'.'`, convert the
revision tokens to integers, and compare them index by index (padding the shorter
list with zeros).
