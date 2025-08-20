from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0

        curr = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                curr += 1
                count += curr
            else:
                curr = 0

            i += 1

        return count


if __name__ == "__main__":
    s = Solution()
    assert s.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6
    assert s.zeroFilledSubarray([0, 0, 0, 2, 0, 0]) == 9
