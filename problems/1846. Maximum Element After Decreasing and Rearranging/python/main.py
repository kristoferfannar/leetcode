from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        curr = 1
        for i in range(1, len(arr)):
            curr = min(curr + 1, arr[i])

        return curr


if __name__ == "__main__":
    s = Solution()
    assert s.maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]) == 2
    assert s.maximumElementAfterDecrementingAndRearranging([100, 1, 1000]) == 3
    assert s.maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5]) == 5
