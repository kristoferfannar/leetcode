from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        return [candies[i] + extraCandies >= maxCandy for i in range(len(candies))]


if __name__ == "__main__":
    s = Solution().kidsWithCandies([2, 3, 5, 1, 3], 3)
    print(s)
    assert s == [True, True, True, False, True]
