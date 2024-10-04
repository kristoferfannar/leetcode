class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        while s != "" and t != "":
            if s[0] == t[0]:
                s = s[1:]
            t = t[1:]

        return s == ""


if __name__ == "__main__":
    s = Solution().isSubsequence("abc", "ahbgdc")
    assert s == True

    s = Solution().isSubsequence("axc", "ahbgdc")
    assert s == False
