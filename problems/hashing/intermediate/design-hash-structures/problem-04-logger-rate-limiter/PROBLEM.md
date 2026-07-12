# Logger Rate Limiter

**Difficulty:** Easy

**Source:** LeetCode 359 — Logger Rate Limiter

## Description

Design a logger that receives a stream of messages with timestamps. `shouldPrintMessage(timestamp, message)` returns whether the message should be printed now — allowed only if the same message has not been printed in the last 10 seconds.

## Examples

### Example 1

```
Input:  t=1 "foo" then t=3 "foo"
Output: true then false
```

## Hint

Map message -> last-printed time; allow if timestamp >= last + 10, then update.
