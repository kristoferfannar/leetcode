class Solution:
    def customSortString(self, order: str, s: str) -> str:
        keys = {c: idx for idx, c in enumerate(order)}

        custom = "".join(sorted(list(s), key=lambda c: keys[c] if c in keys else 0))
        return custom


if __name__ == "__main__":
    s = Solution()
    assert s.customSortString("cba", "abcd") == "cbad"
    assert s.customSortString("bcafg", "abcd") == "bcad"
