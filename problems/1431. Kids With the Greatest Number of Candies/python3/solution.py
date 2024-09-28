from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)

        greatest = [False] * len(candies)

        for idx in range(len(greatest)):
            greatest[idx] = candies[idx] + extraCandies >= maxCandies

        return greatest


if __name__ == "__main__":
    s = Solution().kidsWithCandies([2, 3, 5, 1, 3], 3)
    print(s)
    assert s == [True, True, True, False, True]
