class Solution:
    def reverseWords(self, s: str) -> str:

        words = [word for word in s.strip().split(" ") if word != ""]
        words = words[::-1]
        return " ".join(words)


if __name__ == "__main__":
    s = Solution().reverseWords("Hello this is my world")
    print(s)
    assert s == "world my is this Hello"

    s = Solution().reverseWords("  hello world  ")
    print(s)
    assert s == "world hello"

    s = Solution().reverseWords("a good   example")
    print(s)
    assert s == "example good a"
