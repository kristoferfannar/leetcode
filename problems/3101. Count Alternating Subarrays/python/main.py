from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        last = -1
        curr = 0

        total = 1
        for curr in range(1, len(nums)):
            if nums[curr] == nums[curr - 1]:
                last = curr - 1

            total += curr - last

        return total


if __name__ == "__main__":
    s = Solution()

    assert s.countAlternatingSubarrays([0, 1, 1, 1]) == 5
    assert s.countAlternatingSubarrays([1, 0, 1, 0]) == 10
