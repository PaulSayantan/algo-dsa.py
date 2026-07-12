"""Design Twitter — LeetCode 355."""
from collections import defaultdict  # noqa: F401
from typing import List


class Twitter:
    def __init__(self) -> None:
        # TODO: global clock; user -> tweets; user -> followees set
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        # TODO
        pass

    def getNewsFeed(self, userId: int) -> List[int]:
        # TODO: 10 most recent tweet ids from self + followees, newest first
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        # TODO
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # TODO
        pass


if __name__ == "__main__":
    tw = Twitter()
    tw.postTweet(1, 5)
    print(tw.getNewsFeed(1))  # expected: [5]
    tw.follow(1, 2)
    tw.postTweet(2, 6)
    print(tw.getNewsFeed(1))  # expected: [6, 5]
    tw.unfollow(1, 2)
    print(tw.getNewsFeed(1))  # expected: [5]
