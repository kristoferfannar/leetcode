from typing import List
import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        numsi = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(numsi)

        for _ in range(k):
            num, i = heapq.heappop(numsi)
            nums[i] *= multiplier
            heapq.heappush(numsi, (num * multiplier, i))

        return nums


if __name__ == "__main__":
    assert Solution().getFinalState([2, 1, 3, 5, 6], 5, 2) == [8, 4, 6, 5, 6]
