from collections import defaultdict
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        seen = set()
        numset = set(nums)
        l = 0
        r = 0

        total = 0

        while r < len(nums):
            if len(seen) < len(numset):
                counter[nums[r]] += 1
                if counter[nums[r]] == 1:
                    seen.add(nums[r])
                r += 1

            else:
                total += len(nums) - (r - 1)
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0:
                    seen.remove(nums[l])
                l += 1

        while l < len(nums):
            if len(seen) == len(numset):
                total += 1
            counter[nums[l]] -= 1
            if counter[nums[l]] == 0:
                seen.remove(nums[l])
            l += 1

        return total


if __name__ == "__main__":
    s = Solution()
    assert s.countCompleteSubarrays([1, 3, 1, 2, 2]) == 4
    assert s.countCompleteSubarrays([5, 5, 5, 5]) == 10
    assert s.countCompleteSubarrays([1786, 1786, 1786, 114]) == 3
