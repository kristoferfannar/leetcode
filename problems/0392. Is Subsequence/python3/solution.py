class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0
        t_i = 0
        while s_i < len(s) and t_i < len(t):
            # no way for the rest of s to fit in the rest of t
            if len(s) - s_i > len(t) - t_i:
                return False

            if s[s_i] == t[t_i]:
                s_i += 1
            t_i += 1

        return s_i == len(s)


if __name__ == "__main__":
    s = Solution().isSubsequence("abc", "ahbgdc")
    assert s == True

    s = Solution().isSubsequence("axc", "ahbgdc")
    assert s == False
