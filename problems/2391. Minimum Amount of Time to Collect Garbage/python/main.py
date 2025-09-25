from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        pre = [0] * (len(travel) + 1)
        pre[1] = travel[0]
        for i in range(1, len(travel)):
            pre[i + 1] = travel[i] + pre[i]

        total = 0
        last_m = 0
        last_p = 0
        last_g = 0
        for i, g in enumerate(garbage):
            total += len(g)
            if "M" in g:
                last_m = i
            if "G" in g:
                last_g = i
            if "P" in g:
                last_p = i

        # print(f"total: {total} + m:{pre[last_m]} + p:{pre[last_p]} + g:{pre[last_g]}")
        return total + pre[last_m] + pre[last_p] + pre[last_g]


if __name__ == "__main__":
    s = Solution()

    assert s.garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]) == 21
    assert s.garbageCollection(["MMM", "PGM", "GP"], [3, 10]) == 37
