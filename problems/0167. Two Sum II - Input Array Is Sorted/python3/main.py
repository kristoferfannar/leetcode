from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, h = 0, len(numbers) - 1

        while l < h:
            if numbers[l] + numbers[h] < target:
                l += 1
            elif numbers[l] + numbers[h] > target:
                h -= 1
            else:
                return [l + 1, h + 1]

        return []


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]
    assert Solution().twoSum([-1, 0], -1) == [1, 2]
