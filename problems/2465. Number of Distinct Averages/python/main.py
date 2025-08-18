from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avgs = set()
        nums.sort()

        for i in range(int(len(nums) / 2)):
            avgs.add(nums[i] + nums[len(nums) - i - 1])

        return len(avgs)


if __name__ == "__main__":
    s = Solution()

    assert s.distinctAverages([4, 1, 4, 0, 3, 5]) == 2
