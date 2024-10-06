from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1.difference(set2)), list(set2.difference(set1))]


if __name__ == "__main__":
    s = Solution().findDifference([1, 2, 3], [2, 4, 6])
    print(s)
    assert s == [[1, 3], [4, 6]]
