class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ss1 = sorted(s1)
        ss2 = sorted(s2)

        one = False
        two = False
        for i in range(len(s1)):
            if ss1[i] < ss2[i]:
                two = True
            if ss1[i] > ss2[i]:
                one = True

        return one != two


if __name__ == "__main__":
    s = Solution()

    assert s.checkIfCanBreak("abc", "xya") == True
    assert s.checkIfCanBreak("abe", "acd") == False
    assert s.checkIfCanBreak("leetcodee", "interview") == True
