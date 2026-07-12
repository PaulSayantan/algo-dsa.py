# Sliding Window Rate Limiter

**Difficulty:** Medium

**Source:** Classic — sliding-window-log rate limiting

## Description

You are given a chronologically sorted list of request timestamps `requests` (non-decreasing integers, in seconds), a `limit`, and a `window` size (in seconds). Process the requests in order and decide, for each one, whether it is **allowed** or **rejected**.

A request at time `t` is **allowed** iff, counting only previously-allowed requests whose timestamp is strictly greater than `t - window`, fewer than `limit` remain. An allowed request then counts toward the window for later requests; a rejected request does not.

Return a list of booleans, one per request, where `True` means allowed and `False` means rejected.

## Examples

### Example 1

```
Input:  requests = [1, 2, 3, 11, 12], limit = 2, window = 5
Output: [True, True, False, True, True]
```

**Explanation:** Requests at `1` and `2` are allowed (window holds 0 then 1). At `3` the window `(−2, 3]` already holds 2 allowed requests, so it is rejected. By time `11` both early requests have aged out (`1, 2 <= 11 - 5`), so `11` and `12` are allowed again.

## Hint

Keep a queue of allowed timestamps; for each request, pop the front while it is `<= t - window`, then allow only if the queue length is below `limit`.
