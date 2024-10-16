from typing import List
import heapq as hq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        hq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                hq.heappop(heap)
                hq.heappush(heap, num)

        return heap[0]


if __name__ == "__main__":
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
