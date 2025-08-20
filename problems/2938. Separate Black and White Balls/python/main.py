class Solution:
    def minimumSteps(self, s: str) -> int:
        whiteIdxs = 0
        whiteSeen = 0

        for i in range(len(s)):
            if s[i] == "0":
                whiteSeen += 1
                whiteIdxs += i

        return whiteIdxs - int((whiteSeen * (whiteSeen - 1) / 2))


if __name__ == "__main__":
    s = Solution()
    assert s.minimumSteps("101") == 1
    assert s.minimumSteps("100") == 2
