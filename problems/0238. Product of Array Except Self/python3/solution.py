from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_products = [nums[0]] * len(nums)
        for idx in range(1, len(nums)):
            l_products[idx] = nums[idx] * l_products[idx - 1]

        r_products = [nums[-1]] * len(nums)
        for idx in range(len(nums) - 2, -1, -1):
            r_products[idx] = nums[idx] * r_products[idx + 1]

        return [
            (l_products[idx - 1] if idx != 0 else 1)
            * (r_products[idx + 1] if idx != len(nums) - 1 else 1)
            for idx in range(len(nums))
        ]


if __name__ == "__main__":
    s = Solution().productExceptSelf([1, 2, 3, 4])
    print(s)
    assert s == [24, 12, 8, 6]

    s = Solution().productExceptSelf([-1, 1, 0, -3, 3])
    print(s)
    assert s == [0, 0, 9, 0, 0]
