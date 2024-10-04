from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        s1 = set()
        good1 = set()

        s2 = set()
        good2 = set()

        for w in words1:
            if w in s1:
                if w in good1:
                    good1.remove(w)
            else:
                s1.add(w)
                good1.add(w)

        for w in words2:
            if w in s2:
                if w in good2:
                    good2.remove(w)
            else:
                s2.add(w)
                good2.add(w)

        return len(good1.intersection(good2))


if __name__ == "__main__":
    s = Solution().countWords(["b", "bb", "bbb"], ["a", "aa", "aaa"])
    print(s)
    assert s == 0

    s = Solution().countWords(
        ["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]
    )
    print(s)
    assert s == 2

    s = Solution().countWords(["a", "ab"], ["a", "a", "a", "ab"])
    print(s)
    assert s == 1
