from typing import List


class Solution:
    def __find(self, numbers: List[int], target, l) -> int:
        h = len(numbers) - 1

        # print(f"target-{target}")

        while l <= h:
            m = l + (h - l) // 2
            # print(f"l-{l}, h-{h} | m-{m} (numbers[{m}] = {numbers[m]})")
            if numbers[m] < target:
                l = m + 1
            elif numbers[m] > target:
                h = m - 1
            else:
                return m

        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            found = self.__find(numbers, target - num, idx + 1)
            if found != -1:
                return [idx + 1, found + 1]

        return []


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]
    assert Solution().twoSum([-1, 0], -1) == [1, 2]
