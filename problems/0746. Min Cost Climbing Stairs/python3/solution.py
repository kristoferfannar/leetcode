from typing import List


class Solution:
    def __init__(self):
        self.cost_dict = dict()

    def minCost(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost) <= 2:
            return cost[-1]

        if (len(cost) - 2) not in self.cost_dict:
            self.cost_dict[len(cost) - 2] = self.minCost(cost[:-1])
        if (len(cost) - 3) not in self.cost_dict:
            self.cost_dict[len(cost) - 3] = self.minCost(cost[:-2])

        short = self.cost_dict[len(cost) - 2]
        long = self.cost_dict[len(cost) - 3]

        this = cost[-1] + min(long, short)
        self.cost_dict[len(cost) - 1] = this

        return this

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.minCost(cost), self.minCost(cost[:-1]))


if __name__ == "__main__":
    s = Solution().minCostClimbingStairs([1, 2])
    print(s)
    print()
    assert s == 1

    s = Solution().minCostClimbingStairs([10, 15, 20])
    print(s)
    print()
    assert s == 15

    s = Solution().minCostClimbingStairs([100, 1, 1])
    print(s)
    print()
    assert s == 1

    s = Solution().minCostClimbingStairs([100, 1, 1, 100])
    print(s)
    print()
    assert s == 2

    s = Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print(s)
    print()
    assert s == 6
