"""Dota2 Senate — LeetCode 649 (two FIFO queues built from stacks)."""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # TODO: one two-stack queue of indices per party; smaller index bans
        # the other, winner re-enqueued at index + n
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.predictPartyVictory("RD"))  # expected: 'Radiant'
    print(sol.predictPartyVictory("RDD"))  # expected: 'Dire'
    print(sol.predictPartyVictory("DDRRR"))  # expected: 'Dire'
    print(sol.predictPartyVictory("RRDDD"))  # expected: 'Radiant'
