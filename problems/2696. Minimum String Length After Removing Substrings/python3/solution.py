class Solution:
    def minLength(self, s: str) -> int:

        while "AB" in s or "CD" in s:
            pos = s.find("AB")
            if pos != -1:
                s = s[:pos] + s[pos + 2 :]
            pos = s.find("CD")
            if pos != -1:
                s = s[:pos] + s[pos + 2 :]

        return len(s)


if __name__ == "__main__":
    s = Solution().minLength("ABFCACDB")
    print(s)
    assert s == 2
