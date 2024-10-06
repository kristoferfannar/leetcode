from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = []
        rsum = []

        for num in nums:
            if len(lsum) == 0:
                lsum.append(num)
            else:
                lsum.append(num + lsum[-1])

        for num in nums[::-1]:
            if len(rsum) == 0:
                rsum.insert(0, num)
            else:
                rsum.insert(0, num + rsum[0])

        print(lsum)
        print(rsum)

        for idx in range(len(nums)):
            if lsum[idx] == rsum[idx]:
                return idx
        return -1


if __name__ == "__main__":
    s = Solution().pivotIndex([1, 7, 3, 6, 5, 6])
    print(s)
    assert s == 3

    s = Solution().pivotIndex([1, 2, 3])
    print(s)
    assert s == -1

    s = Solution().pivotIndex([2, 1, -1])
    print(s)
    assert s == 0

    s = Solution().pivotIndex([-1, -1, -1, -1, -1, 0])
    print(s)
    assert s == 2
