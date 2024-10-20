from typing import List


class Solution:
    def check_exhaustion(self, nums1, nums2, l_idx, r_idx):
        return [len(nums1) <= l_idx, len(nums2) <= r_idx]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        med = (len(nums1) + len(nums2)) / 2
        is_odd = med != int(med)
        med = int(med) + 1
        l_idx, r_idx = 0, 0

        exhausted = [False, False]
        curr, old = 0, 0

        while l_idx + r_idx < med:
            exhausted = self.check_exhaustion(nums1, nums2, l_idx, r_idx)
            old = curr

            if exhausted[0]:
                curr = nums2[r_idx]
                r_idx += 1
            elif exhausted[1]:
                curr = nums1[l_idx]
                l_idx += 1

            elif nums1[l_idx] < nums2[r_idx]:
                curr = nums1[l_idx]
                l_idx += 1
            else:
                curr = nums2[r_idx]
                r_idx += 1

        if is_odd:
            return curr
        return (old + curr) / 2.0


if __name__ == "__main__":
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
    assert Solution().findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8]) == 5.0
    assert Solution().findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == 5.5
    assert Solution().findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7, 8, 9]) == 5.0
    assert Solution().findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7, 8, 9, 10]) == 5.5
    assert Solution().findMedianSortedArrays([], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
    assert Solution().findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], []) == 5.5
    assert Solution().findMedianSortedArrays([1], []) == 1
    assert Solution().findMedianSortedArrays([1, 2], []) == 1.5
    assert Solution().findMedianSortedArrays([], [1]) == 1
