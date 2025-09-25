class Solution:
    def addMinimum(self, word: str) -> int:
        chars = ["a", "b", "c"]
        ops = 0
        last = chars.index("c")

        for c in word:
            curr = chars.index(c)
            steps = (curr - (last + 1)) % len(chars)
            ops += steps
            last = curr

        ops += (chars.index("a") - (last + 1)) % len(chars)

        return ops


if __name__ == "__main__":
    s = Solution()
    assert s.addMinimum("b") == 2
    assert s.addMinimum("aaa") == 6
    assert s.addMinimum("abc") == 0
