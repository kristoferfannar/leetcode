from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)

        for i in range(n + 1):
            bits[i] = bits[i >> 1] + (i & 1)

        return bits


if __name__ == "__main__":
    s = Solution().countBits(2)
    print(s)
    assert s == [0, 1, 1]

    s = Solution().countBits(5)
    print(s)
    assert s == [0, 1, 1, 2, 1, 2]
