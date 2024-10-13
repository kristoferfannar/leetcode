from typing import List


class City:
    def __init__(self, id) -> None:
        self.id = id
        self.roads: List[City] = []
        self.to_c = set()
        self.from_c = set()

    def __repr__(self) -> str:
        return f"City({self.id})"


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        cities = [City(i) for i in range(n)]
        seen = set([cities[0]])
        changes = 0

        for from_c, to_c in connections:
            cities[from_c].roads.append(cities[to_c])
            cities[from_c].to_c.add(cities[to_c])
            cities[to_c].roads.append(cities[from_c])
            cities[to_c].from_c.add(cities[from_c])

        frontier = [cities[0]]
        while frontier:
            curr = frontier.pop(0)

            for city in curr.roads:
                if city not in seen:
                    frontier.append(city)
                    seen.add(city)
                    if city in curr.to_c:
                        changes += 1

        return changes


if __name__ == "__main__":
    assert Solution().minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
    assert Solution().minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
    assert Solution().minReorder(6, [[4, 5], [0, 1], [1, 3], [2, 3], [4, 0]]) == 3
