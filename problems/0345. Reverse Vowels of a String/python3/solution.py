class Solution:
    VOWELS = "aeiou"

    def reverseVowels(self, s: str) -> str:
        new_s = list(s)

        vowels = [
            (idx, char) for idx, char in enumerate(s) if char.lower() in self.VOWELS
        ]

        low, high = 0, len(vowels) - 1

        while low < high:
            new_s[vowels[high][0]], new_s[vowels[low][0]] = (
                vowels[low][1],
                vowels[high][1],
            )

            low += 1
            high -= 1

        return "".join(new_s)


if __name__ == "__main__":
    s = Solution().reverseVowels("IceCreAm")
    print(s)
    assert s == "AceCreIm"

    s = Solution().reverseVowels("bbbbb")
    print(s)
    assert s == "bbbbb"
