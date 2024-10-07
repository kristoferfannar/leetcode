class Solution:
    def minLength(self, s: str) -> int:
        idx = 0

        while idx < len(s) - 1:
            if s[idx : idx + 2] in ["AB", "CD"]:
                s = s[:idx] + s[idx + 2 :]
                idx -= 1
                idx = max(0, idx)  # don't set idx = -1 if substrings found on idx = 0
            else:
                idx += 1

        return len(s)


if __name__ == "__main__":
    s = Solution().minLength("ABFCACDB")
    print(s)
    assert s == 2

    s = Solution().minLength("ACBBD")
    print(s)
    assert s == 5
