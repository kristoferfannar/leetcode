from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        pixels = 0
        for c in s:
            i = ord(c) - ord("a")

            if pixels + widths[i] > 100:
                lines += 1
                pixels = 0

            pixels += widths[i]

        return [lines, pixels]


if __name__ == "__main__":
    s = Solution()

    assert [3, 60] == s.numberOfLines(
        [
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
            10,
        ],
        "abcdefghijklmnopqrstuvwxyz",
    )
