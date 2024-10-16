from typing import List
import heapq as hq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            hq.heappush(heap, num)

        print("heap", heap)
        return hq.nlargest(k, heap)[-1]


if __name__ == "__main__":
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
