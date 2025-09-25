from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        best = 0
        zeros = [-1]

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)

        zeros.append(len(nums))

        if len(zeros) == 2:
            return len(nums) - 1

        for i in range(len(zeros) - 2):
            curr = zeros[i + 2] - zeros[i] - 2
            best = max(best, curr)

        return best


if __name__ == "__main__":
    s = Solution()

    assert s.longestSubarray([1, 1, 0, 1]) == 3
    assert s.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
    assert s.longestSubarray([1, 1, 1]) == 2
    assert s.longestSubarray([1, 1, 0, 0, 1, 1, 1, 0, 1]) == 4
    assert s.longestSubarray([1, 0, 0, 0, 0]) == 1
