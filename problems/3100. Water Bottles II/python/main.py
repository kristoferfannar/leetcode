class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles

        while numBottles >= numExchange:
            numBottles -= numExchange - 1
            drank += 1
            numExchange += 1

        print(drank)
        return drank


if __name__ == "__main__":
    s = Solution()
    assert s.maxBottlesDrunk(13, 6) == 15
    assert s.maxBottlesDrunk(10, 3) == 13
