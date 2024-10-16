from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        results = [0] * len(temperatures)
        for idx, tmp in enumerate(temperatures):
            while days and days[-1][0] < tmp:
                day = days.pop()
                results[day[1]] = idx - day[1]
            days.append((tmp, idx))

        return results


if __name__ == "__main__":
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]

    assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
