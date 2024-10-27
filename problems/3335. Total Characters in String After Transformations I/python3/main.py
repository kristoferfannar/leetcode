from collections import Counter
from functools import cache


class Solution:
    @cache
    def calc_score(self, letter, t) -> int:
        lord = ord("z") - ord(letter)

        if t <= lord:
            return 1

        new_t = t - lord - 1
        return self.calc_score("a", new_t) + self.calc_score("a", new_t + 1)

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        size = 0

        letters = Counter(s)

        for letter, count in letters.items():
            score = self.calc_score(letter, t)
            size = (size + count * score) % (10**9 + 7)

        return size


if __name__ == "__main__":
    s = Solution().lengthAfterTransformations("abcyy", 2)
    assert s == 7

    assert Solution().lengthAfterTransformations("azbk", 1) == 5

    assert Solution().lengthAfterTransformations("zz", 0) == 2
    assert Solution().lengthAfterTransformations("zz", 1) == 4
    assert Solution().lengthAfterTransformations("yy", 1) == 2
    assert Solution().lengthAfterTransformations("yyyyy", 2) == 10
    assert Solution().lengthAfterTransformations("z", 25) == 2
    assert Solution().lengthAfterTransformations("z", 26) == 3

    s = Solution().lengthAfterTransformations("jqktcurgdvlibczdsvnsg", 7517)
    print(s)
    assert s == 79033769

    s = Solution().lengthAfterTransformations("bheanuyzjlwflksvyzuku", 9433)
    print(s)
    assert s == 500060987
