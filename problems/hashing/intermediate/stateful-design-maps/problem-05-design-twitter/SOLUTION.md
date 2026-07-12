# Design Twitter — Solution

## Optimal Approach

Timestamp tweets; merge candidate lists and take the 10 newest.

### Reference implementation

```python
class Twitter:
    def __init__(self):
        self._time = 0
        self._tweets = defaultdict(list)
        self._follows = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self._tweets[userId].append((self._time, tweetId))
        self._time += 1

    def getNewsFeed(self, userId):
        cand = list(self._tweets[userId])
        for f in self._follows[userId]:
            cand.extend(self._tweets[f])
        cand.sort(reverse=True)
        return [tid for _, tid in cand[:10]]

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self._follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self._follows[followerId].discard(followeeId)
```

### Complexity

Feed O(total tweets log).

## Key Insights & Edge Cases

After following user2 who posts 6, feed is [6,5]; unfollow reverts to [5].
