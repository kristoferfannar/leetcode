from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ones = 0
        zeros = 0

        while ones < len(nums) - 1 and zeros < len(nums) - 1:
            while ones < len(nums) and nums[ones] == 0:
                ones += 1
            while zeros < len(nums) and nums[zeros] != 0:
                zeros += 1

            if max(ones, zeros) >= len(nums):
                break

            if ones < zeros:
                ones = zeros
            nums[ones], nums[zeros] = nums[zeros], nums[ones]
            # print(f"{ones}, {zeros}", nums)


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(nums)
    Solution().moveZeroes(nums)
    print(nums)
    print()
    assert nums == [1, 3, 12, 0, 0]

    nums = [1, 0, 3, 12]
    print(nums)
    Solution().moveZeroes(nums)
    print(nums)
    print()
    assert nums == [1, 3, 12, 0]

    nums = [0, 0]
    print(nums)
    Solution().moveZeroes(nums)
    print(nums)
    print()
    assert nums == [0, 0]

    nums = [1, 0]
    print(nums)
    Solution().moveZeroes(nums)
    print(nums)
    print()
    assert nums == [1, 0]
