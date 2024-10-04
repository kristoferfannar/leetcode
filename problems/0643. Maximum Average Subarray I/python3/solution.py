from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[0:k])
        max_sum = curr_sum

        for i in range(k, len(nums)):
            inn = nums[i]
            out = nums[i - k]
            curr_sum = curr_sum - out + inn
            max_sum = max(max_sum, curr_sum)

        return max_sum / k


if __name__ == "__main__":
    s = Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4)
    print(s)
    assert s == 12.75

    s = Solution().findMaxAverage([0, 0, 0, 100], 1)
    print(s)
    assert s == 100
