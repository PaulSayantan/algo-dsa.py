# Design Authentication Manager

**Difficulty:** Medium

**Source:** LeetCode 1797 — Design Authentication Manager

## Description

Tokens live `timeToLive` seconds. `generate(id, t)` creates a token expiring at `t + ttl`; `renew(id, t)` extends an *unexpired* token to `t + ttl` (no-op otherwise); `countUnexpiredTokens(t)` counts tokens with expiry strictly greater than `t`.

## Examples

### Example 1

```
Input:  ttl=5; generate aaa@1, bbb@2; count@3
Output: 2
```

## Hint

Map tokenId -> expiry; renew only if present and expiry > t; count expiry > t.
