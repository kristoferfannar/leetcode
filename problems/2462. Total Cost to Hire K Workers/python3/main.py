import heapq
from typing import List


class Solution:
    def select_min(self, min_heap, max_heap):
        if len(min_heap) == 0:
            return False
        if len(max_heap) == 0:
            return True

        return min_heap[0] <= max_heap[0]

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # len = 8, candidates = 4 for this to kick in
        if len(costs) <= candidates * 2:
            l = len(costs) - 1
            r = 0
            min_heap = costs
            max_heap = []
        else:
            l = r = candidates
            min_heap = costs[:candidates]
            max_heap = costs[-candidates:]

        heapq.heapify(min_heap)
        heapq.heapify(max_heap)

        cost = 0
        for _ in range(k):
            should_select_min = self.select_min(min_heap, max_heap)

            if should_select_min:
                min_cost = heapq.heappop(min_heap)
                if l + r < len(costs):
                    heapq.heappush(min_heap, costs[l])
                    l += 1

            else:
                min_cost = heapq.heappop(max_heap)
                if l + r < len(costs):
                    heapq.heappush(max_heap, costs[-(r + 1)])
                    r += 1

            cost += min_cost

        return cost


if __name__ == "__main__":
    assert Solution().totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4) == 11
    assert Solution().totalCost([1, 2, 4, 1], 3, 3) == 4
