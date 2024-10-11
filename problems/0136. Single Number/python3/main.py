from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        # XOR-ing the same number with itself returns zero
        for num in nums:
            ans = ans ^ num  # XOR

        return ans


if __name__ == "__main__":
    s = Solution().singleNumber([2, 2, 1])
    assert s == 1

    s = Solution().singleNumber([4, 1, 2, 1, 2])
    assert s == 4

    assert Solution().singleNumber([1]) == 1
