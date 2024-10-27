from typing import List

from test import lis as LIS


class Solution:
    def is_ones(self, matrix, start_x, start_y, last_x, last_y):
        for x in range(start_x, last_x + 1):
            for y in range(start_y, last_y + 1):
                if matrix[y][x] == 0:
                    return False
        return True

    def countSquares(self, matrix: List[List[int]]) -> int:
        dim = min(len(matrix), len(matrix[0]))
        squares = 0
        for d in range(dim):
            for y in range(len(matrix) - d):
                last_y = y + d
                for x in range(len(matrix[y]) - d):
                    last_x = x + d
                    if self.is_ones(matrix, x, y, last_x, last_y):
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
