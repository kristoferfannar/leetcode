class Solution:
    VOWELS = set("aeiou")

    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = sum([c in self.VOWELS for c in s[:k]])
        curr = max_vowels

        for lo in range(0, len(s) - k):
            hi = lo + k
            curr = curr - int(s[lo] in self.VOWELS) + int(s[hi] in self.VOWELS)
            max_vowels = max(max_vowels, curr)

        return max_vowels


if __name__ == "__main__":
    s = Solution().maxVowels("abciiidef", 3)
    print(s)
    assert s == 3

    assert Solution().maxVowels("aeiou", 2) == 2
    assert Solution().maxVowels("leetcode", 3) == 2
