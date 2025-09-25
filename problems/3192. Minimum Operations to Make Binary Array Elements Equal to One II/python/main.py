from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        for i in range(len(nums)):
            if (nums[i] + flips) % 2 == 0:
                flips += 1

        return flips


if __name__ == "__main__":
    s = Solution()

    assert s.minOperations([0, 1, 1, 0, 1]) == 4
    assert s.minOperations([1, 0, 0, 0]) == 1
