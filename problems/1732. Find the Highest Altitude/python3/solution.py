from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        curr = 0

        for g in gain:
            curr += g
            max_alt = max(max_alt, curr)

        return max_alt


if __name__ == "__main__":
    s = Solution().largestAltitude([-5, 1, 5, 0, -7])
    print(s)
    assert s == 1

    s = Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2])
    print(s)
    assert s == 0
