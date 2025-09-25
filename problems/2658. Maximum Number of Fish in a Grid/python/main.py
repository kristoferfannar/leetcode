from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        checked: List[List[bool]] = [[False] * len(grid[0]) for _ in range(len(grid))]

        R = len(grid)
        C = len(grid[0])

        max_fish = 0
        for r in range(R):
            for c in range(C):
                if checked[r][c] or grid[r][c] == 0:
                    continue

                positions = [(r, c)]
                fish = 0

                while positions:
                    cr, cc = positions.pop(0)
                    if checked[cr][cc]:
                        continue

                    checked[cr][cc] = True

                    if grid[cr][cc] == 0:
                        continue

                    fish += grid[cr][cc]

                    if cr + 1 < R and not checked[cr + 1][cc]:
                        positions.append((cr + 1, cc))

                    if cc + 1 < C and not checked[cr][cc + 1]:
                        positions.append((cr, cc + 1))

                    if cc > 0 and not checked[cr][cc - 1]:
                        positions.append((cr, cc - 1))

                    if cr > 0 and not checked[cr - 1][cc]:
                        positions.append((cr - 1, cc))

                max_fish = max(max_fish, fish)

        return max_fish


if __name__ == "__main__":
    s = Solution()
    assert s.findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]) == 7
    assert s.findMaxFish([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]) == 1
    assert s.findMaxFish([[8, 6], [2, 6]]) == 22
