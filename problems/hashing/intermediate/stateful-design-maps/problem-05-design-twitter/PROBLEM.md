# Design Twitter

**Difficulty:** Medium

**Source:** LeetCode 355 — Design Twitter

## Description

Design a mini Twitter: `postTweet(userId, tweetId)`, `getNewsFeed(userId)` (the 10 most recent tweet ids from the user and everyone they follow, newest first), `follow`, and `unfollow`. A user implicitly follows themselves.

## Examples

### Example 1

```
Input:  post 5 by user1; feed(1)
Output: [5]
```

## Hint

Global clock stamps tweets; feed merges self+followees' tweets and sorts by time desc.
