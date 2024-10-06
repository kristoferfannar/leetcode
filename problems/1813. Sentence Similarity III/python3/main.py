class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")

        if len(words1) < len(words2):
            short = words1
            long = words2
        else:
            short = words2
            long = words1

        for split in range(len(short) + 1):
            l_rest = len(long) + split - len(short)

            s_pref = short[:split]
            l_pref = long[:split]
            s_suf = short[split:]
            l_suf = long[l_rest:]

            if s_pref == l_pref and s_suf == l_suf:
                return True

        return False


if __name__ == "__main__":
    s = Solution().areSentencesSimilar("Hello Jane", "Hello my name is Jane")
    print(s)
    assert s == True

    s = Solution().areSentencesSimilar("Eating right now", "Eating")
    print(s)
    assert s == True

    s = Solution().areSentencesSimilar("Ogn WtWj HneS", "Ogn WtWj HneS")
    print(s)
    assert s == True

    s = Solution().areSentencesSimilar(
        "xD iP tqchblXgqvNVdi", "FmtdCzv Gp YZf UYJ xD iP tqchblXgqvNVdi"
    )
    print(s)
    assert s == True

    s = Solution().areSentencesSimilar("of", "A lot of words")
    print(s)
    assert s == False
