class Solution:
    def removeStars(self, s: str) -> str:
        items = []

        for c in s:
            # this operation is guaranteed to be possible
            if c == "*":
                items.pop()
            else:
                items.append(c)

        return "".join(items)


if __name__ == "__main__":
    assert Solution().removeStars("leet**cod*e") == "lecoe"
