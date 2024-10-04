from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            max_area = max(
                max_area,
                (right - left) * min(height[left], height[right]),
            )

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    s = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(s)
    assert s == 49

    s = Solution().maxArea([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(s)
    assert s == 25

    length = 20000
    arr = [min(x, length - 1 - x) + 1 for x in range(length)]
    # print(arr)
    s = Solution().maxArea(arr)
    print(s)
    assert s == 50000000
