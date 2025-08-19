class Solution:
    def minTimeToType(self, word: str) -> int:
        secs = len(word)

        last = "a"
        for c in word:
            l = ord(min(c, last))
            r = ord(max(c, last))
            secs += min(r - l, 26 - (r - l))

            last = c

        print(secs)
        return secs


if __name__ == "__main__":
    s = Solution()
    assert s.minTimeToType("abc") == 5
    assert s.minTimeToType("bza") == 7
