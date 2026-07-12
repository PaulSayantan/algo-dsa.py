# Logger Rate Limiter

**Difficulty:** Medium

**Source:** LeetCode 359 — Logger Rate Limiter

## Description

Design a `Logger` that receives a stream of messages and their timestamps. Each unique message may be printed **at most once every 10 seconds**.

Implement `shouldPrintMessage(timestamp, message)`: return `True` if the `message` should be printed at the given `timestamp`, and `False` otherwise. A message is printable iff it has never been printed, or its last-printed time is more than 10 seconds before `timestamp` (i.e. `timestamp - last >= 10`). Every call that returns `True` updates that message's last-printed time.

Calls are made with non-decreasing `timestamp` values.

## Examples

### Example 1

```
Input:  shouldPrintMessage(1,"foo"); shouldPrintMessage(2,"bar"); shouldPrintMessage(3,"foo"); shouldPrintMessage(11,"foo")
Output: True, True, False, True
```

**Explanation:** `foo` and `bar` print on first sight at times `1` and `2`. `foo` again at `3` is within 10s of its last print (`1`), so it is throttled. At `11`, `11 - 1 = 10 >= 10`, so `foo` may print again.

## Hint

Track each message's most recent print time; on every call, expire (evict) entries older than 10 seconds and allow a message only when its recorded time has cleared the window.
