from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        players = [False] * n
        players[0] = True

        curr = 1
        round = 1
        while not players[(curr + round * k) % n - 1]:
            players[(curr + round * k) % n - 1] = True
            curr += round * k
            round += 1

        losers = [i + 1 for i, p in enumerate(players) if p == 0]
        return losers


if __name__ == "__main__":
    s = Solution()

    assert s.circularGameLosers(5, 2) == [4, 5]
    assert s.circularGameLosers(4, 4) == [2, 3, 4]
