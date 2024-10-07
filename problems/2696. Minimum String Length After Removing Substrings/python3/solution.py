class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if len(stack) == 0:
                stack.append(char)
            elif char == "B" and stack[-1] == "A":
                stack.pop()
            elif char == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(char)

        return len(stack)


if __name__ == "__main__":
    s = Solution().minLength("ABFCACDB")
    print(s)
    assert s == 2

    s = Solution().minLength("ACBBD")
    print(s)
    assert s == 5
