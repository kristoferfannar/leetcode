from typing import List
from math import ceil


def search(spotions: List[int], target) -> int:
    if len(spotions) == 1:
        return int(target <= spotions[0])

    def bounded_search(spotions, lo, hi, target) -> int:
        mid = int((hi + lo) / 2)

        if spotions[mid - 1] < target and target <= spotions[mid]:
            return mid

        if lo == hi:
            if lo == len(spotions) - 1:
                return len(spotions)
            if hi == 1:
                return 0
            return mid

        if target <= spotions[mid]:
            return bounded_search(spotions, lo, mid, target)

        return bounded_search(spotions, mid + 1, hi, target)

    mid_idx = bounded_search(spotions, 0, len(spotions) - 1, target)
    return len(spotions) - mid_idx


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        outcome = []
        spotions = sorted(potions)

        for spell in spells:
            target = ceil(success / spell)
            found = search(spotions, target)
            outcome.append(found)

        return outcome


if __name__ == "__main__":
    s = Solution().successfulPairs([5], [1, 2, 3, 4, 5], 7)
    print(s)
    assert s == [4]

    s = Solution().successfulPairs([1], [1, 2, 3, 4, 5], 7)
    print(s)
    assert s == [0]

    s = Solution().successfulPairs([1], [10, 10, 10, 10], 7)
    print(s)
    assert s == [4]

    s = Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7)
    print(s)
    assert s == [4, 0, 3]

    s = Solution().successfulPairs([5], [0, 0, 0, 0, 1, 2, 2, 2, 5, 10], 7)
    print(s)
    assert s == [5]

    s = Solution().successfulPairs([5, 1, 3], [0, 0, 0, 0, 1, 2, 2, 2, 5, 10], 7)
    print(s)
    assert s == [5, 1, 2]

    s = Solution().successfulPairs([15, 14, 39], [22], 224)
    print(s)
    assert s == [1, 1, 1]
