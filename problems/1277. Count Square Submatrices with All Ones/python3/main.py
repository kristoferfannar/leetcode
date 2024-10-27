from typing import List
from numpy import array

from test import lis as LIS
from time import time


class Solution:
    def row_sums(self, matrix: List[List[int]]) -> List[List[int]]:
        sums = []

        for row in matrix:
            row_sum = [row[0]]

            for i in range(1, len(row)):
                row_sum.append(row[i] + row_sum[i - 1])
            sums.append(row_sum)

        return sums

    def area_sums(self, rsums: List[List[int]]) -> List[List[int]]:
        c_sums = [rsums[0]]

        for r in range(1, len(rsums)):
            sums = []
            for i in range(len(rsums[r])):
                sums.append(rsums[r][i] + c_sums[r - 1][i])

            c_sums.append(sums)

        return c_sums

    def is_ones(self, sums, x, y, d) -> bool:

        prev = left = up = 0
        if y - 1 >= 0 and x - 1 >= 0:
            prev = sums[y - 1][x - 1]
        if y - 1 >= 0:
            up = sums[y - 1][x + d]
        if x - 1 >= 0:
            left = sums[y + d][x - 1]

        curr = sums[y + d][x + d]

        return curr - left - up + prev == (d + 1) * (d + 1)

    def countSquares(self, matrix: List[List[int]]) -> int:
        dim = min(len(matrix), len(matrix[0]))

        # print(array(matrix))
        start = time()
        sums = self.row_sums(matrix)
        # print()
        # print(array(sums))
        sums = self.area_sums(sums)
        # print(array(sums))
        print(f"initialized sums in {time() - start} sec")

        squares = 0

        for d in range(dim):
            for y in range(len(matrix) - d):
                for x in range(len(matrix[y]) - d):

                    if self.is_ones(sums, x, y, d):
                        squares += 1

        return squares


if __name__ == "__main__":
    # s = Solution().countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]])
    # print(s)
    # assert s == 15

    print(f"LIS = x-{len(LIS[0])} y-{len(LIS)}")

    s = Solution().countSquares(LIS)
    print(s)
    assert s == 22859
