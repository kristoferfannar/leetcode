class Solution:
    ins = "([{"
    outs = ")]}"

    pairs = {"(": ")", "[": "]", "{": "}"}

    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in self.outs:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if self.pairs[last] != c:
                    return False

            elif c in self.ins:
                stack.append(c)

        return len(stack) == 0


if __name__ == "__main__":
    assert Solution().isValid("()") == True
    assert Solution().isValid("()[]{}") == True
    assert Solution().isValid("(]") == False
