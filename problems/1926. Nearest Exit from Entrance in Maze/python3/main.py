from typing import List


class Solution:
    def __init__(self) -> None:
        self.explored = set()

    def is_valid(
        self, maze: List[List[str]], entrance: List[int], pos: tuple[int, int]
    ) -> bool:
        if (
            pos[0] < 0
            or len(maze) <= pos[0]
            or pos[1] < 0
            or len(maze[0]) <= pos[1]
            or entrance == pos
        ):
            return False

        return not maze[pos[0]][pos[1]] == "+"

    def is_exit(self, maze: List[List[str]], pos: tuple[int, int]) -> bool:
        # we have already validated that this position is neither a wall nor the entrance
        return (
            pos[0] == 0
            or pos[1] == 0
            or pos[0] == len(maze) - 1
            or pos[1] == len(maze[0]) - 1
        )

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.explored.add((entrance[0], entrance[1]))

        # (pos, cost)
        frontier: List[tuple[tuple[int, int], int]] = [((entrance[0], entrance[1]), 0)]

        while len(frontier) > 0:
            curr, cost = frontier.pop(0)

            dirs = [
                (curr[0] + 1, curr[1]),
                (curr[0] - 1, curr[1]),
                (curr[0], curr[1] + 1),
                (curr[0], curr[1] - 1),
            ]

            for dir in dirs:
                if dir in self.explored:
                    continue
                self.explored.add(dir)
                if not self.is_valid(maze, entrance, dir):
                    continue

                if self.is_exit(maze, dir):
                    return cost + 1

                frontier.append((dir, cost + 1))

        return -1


if __name__ == "__main__":
    s = Solution().nearestExit(
        [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]
    )
    print(s)
    assert s == 1
    #
    assert (
        Solution().nearestExit(
            [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]
        )
        == 2
    )

    assert Solution().nearestExit([[".", "+"]], [0, 0]) == -1
    #
    s = Solution().nearestExit(
        [
            ["+", ".", "+", "+", "+", "+", "+"],
            ["+", ".", "+", ".", ".", ".", "+"],
            ["+", ".", "+", ".", "+", ".", "+"],
            ["+", ".", ".", ".", "+", ".", "+"],
            ["+", "+", "+", "+", "+", ".", "+"],
        ],
        [0, 1],
    )

    print(s)
    assert s == 12

    s = Solution().nearestExit(
        [
            [".", ".", ".", ".", ".", "+", ".", ".", "."],
            [".", "+", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "+", ".", "+", ".", "+", ".", "+"],
            [".", ".", ".", ".", "+", ".", ".", ".", "."],
            [".", ".", ".", ".", "+", "+", ".", ".", "."],
            ["+", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "+", ".", ".", ".", ".", "."],
            [".", ".", ".", "+", ".", ".", ".", ".", "+"],
            ["+", ".", ".", "+", ".", "+", "+", ".", "."],
        ],
        [8, 4],
    )
    print(s)
    assert s == 5
