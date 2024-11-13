from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        shots = 0
        spoints = sorted(points)

        while spoints:
            l, r = spoints[0]
            included = 1

            while included < len(spoints):
                nl, nr = spoints[included]

                if nl > r:
                    break

                l = max(l, nl)
                r = min(r, nr)
                included += 1

            spoints = spoints[included:]
            shots += 1

        return shots


if __name__ == "__main__":
    assert Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert (
        Solution().findMinArrowShots(
            [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
        )
        == 2
    )

    assert (
        Solution().findMinArrowShots(
            [[4, 12], [7, 8], [7, 9], [7, 9], [2, 8], [6, 7], [5, 14], [4, 13]]
        )
        == 1
    )
