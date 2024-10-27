from math import lcm, gcd
from typing import List, Optional


class Solution:
    def get_score(self, nums, i):
        if i == -1:
            return gcd(*nums) * lcm(*nums)

        else:
            return gcd(*nums[:i], *nums[i + 1 :]) * lcm(*nums[:i], *nums[i + 1 :])

    def maxScore(self, nums: List[int]) -> int:
        max_score = 0
        for i in range(-1, len(nums)):
            score = self.get_score(nums, i)

            if max_score < score:
                max_score = score

        return max_score
