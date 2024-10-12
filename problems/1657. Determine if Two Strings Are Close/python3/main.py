class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        chars1 = dict()
        chars2 = dict()
        set1 = set()
        set2 = set()

        for c in word1:
            set1.add(c)
            if c not in chars1:
                chars1[c] = 1
            else:
                chars1[c] += 1

        for c in word2:
            set2.add(c)
            if c not in chars2:
                chars2[c] = 1
            else:
                chars2[c] += 1

        occs1 = sorted(chars1.values())
        occs2 = sorted(chars2.values())

        return occs1 == occs2 and set1 == set2


if __name__ == "__main__":
    assert Solution().closeStrings("abc", "bca") == True
    assert Solution().closeStrings("uau", "ssx") == False
