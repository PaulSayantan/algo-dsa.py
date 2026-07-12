"""Design Authentication Manager — LeetCode 1797."""


class AuthenticationManager:
    def __init__(self, timeToLive: int) -> None:
        # TODO: tokenId -> expiry time
        pass

    def generate(self, tokenId: str, currentTime: int) -> None:
        # TODO
        pass

    def renew(self, tokenId: str, currentTime: int) -> None:
        # TODO: only if the token exists and is unexpired
        pass

    def countUnexpiredTokens(self, currentTime: int) -> int:
        # TODO
        pass


if __name__ == "__main__":
    am = AuthenticationManager(5)
    am.generate("aaa", 1)
    am.generate("bbb", 2)
    print(am.countUnexpiredTokens(3))  # expected: 2
    am.renew("aaa", 4)
    print(am.countUnexpiredTokens(6))  # expected: 2
    am.renew("bbb", 8)
    print(am.countUnexpiredTokens(8))  # expected: 1
