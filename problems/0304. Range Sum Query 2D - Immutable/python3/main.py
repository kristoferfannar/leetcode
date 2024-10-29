from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):

        self.matrix = matrix
        self.sums = []
        for y in range(len(matrix)):

            last_row_first = 0
            if y > 0:
                last_row_first = self.sums[y - 1][0]
            row = [last_row_first + matrix[y][0]]

            for x in range(1, len(matrix[y])):
                last_row_sum = 0
                if y > 0:
                    last_row_sum = self.sums[y - 1][x] - self.sums[y - 1][x - 1]
                row.append(last_row_sum + matrix[y][x] + row[x - 1])

            self.sums.append(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prev = left = up = 0
        if row1 > 0 and col1 > 0:
            prev = self.sums[row1 - 1][col1 - 1]
        if row1 > 0:
            up = self.sums[row1 - 1][col2]
        if col1 > 0:
            left = self.sums[row2][col1 - 1]
        curr = self.sums[row2][col2]

        return curr - left - up + prev


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


if __name__ == "__main__":
    nm = NumMatrix(
        [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
    )
    assert nm.sumRegion(2, 1, 4, 3) == 8
    assert nm.sumRegion(1, 1, 2, 2) == 11
    assert nm.sumRegion(1, 2, 2, 4) == 12
