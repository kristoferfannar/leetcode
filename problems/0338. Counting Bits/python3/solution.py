from typing import List


class Solution:
    def getBits(self, i: int) -> int:
        ones = 0

        while i > 0:
            ones += i & 1
            i = i >> 1

        return ones

    def countBits(self, n: int) -> List[int]:
        bits = []

        for i in range(n + 1):
            bits.append(self.getBits(i))

        return bits


if __name__ == "__main__":
    s = Solution().countBits(2)
    print(s)
    assert s == [0, 1, 1]

    s = Solution().countBits(5)
    print(s)
    assert s == [0, 1, 1, 2, 1, 2]
