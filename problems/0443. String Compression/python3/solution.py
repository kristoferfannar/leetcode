from typing import List


class Solution:
    def switch(self, chars, letter, seen, pos, next_print):
        if seen == 1:
            chars[next_print] = letter

            for idx in range(next_print + 1, next_print + 1 + (pos - next_print)):
                chars[idx] = None
            return next_print + 1

        chars[next_print] = letter
        for idx, num in enumerate(list(str(seen))):
            chars[next_print + 1 + idx] = num

        for idx in range(
            next_print + 1 + len(list(str(seen))),
            next_print + seen + (pos - next_print),
        ):
            chars[idx] = None

        return next_print + 1 + len(list(str(seen)))

    def compress(self, chars: List[str]) -> int:
        letter = chars[0]
        seen = 0
        next_print = 0

        for idx in range(len(chars)):
            if chars[idx] == letter:
                seen += 1

            else:
                next_print = self.switch(chars, letter, seen, idx - seen, next_print)
                letter = chars[idx]
                seen = 1

        if seen != 0:
            next_print = self.switch(chars, letter, seen, len(chars) - seen, next_print)

        for idx in range(len(chars)):
            if chars[idx] == None:
                return idx

        return len(chars)


if __name__ == "__main__":
    # chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c"]
    # print(chars)
    # Solution().switch(chars, "a", 1, 0)
    # print(chars)
    # Solution().switch(chars, "b", 12, 1)
    # print(chars)
    # Solution().switch(chars, "c", 2, 13)
    # print(chars)

    chars = ["a", "a", "a", "a", "e", "b", "b", "b", "c", "c", "c", "c"]
    print(chars)
    s = Solution().compress(chars)
    print(s)
    print(chars)
    print()
    assert s == 7

    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    print(chars)
    s = Solution().compress(chars)
    print(s)
    print(chars)
    print()
    assert s == 4

    chars = ["a", "b", "c", "c", "c", "r", "r", "t", "y", "y"]
    print(chars)
    s = Solution().compress(chars)
    print(s)
    print(chars)
    print()
    assert s == 9

    chars = ["a", "a", "a", "a", "c", "r", "r", "t", "y", "y"]
    print(chars)
    s = Solution().compress(chars)
    print(s)
    print(chars)
    print()
    assert s == 8

    chars = ["a", "a", "a", "a", "b", "a"]
    print(chars)
    s = Solution().compress(chars)
    print(s)
    print(chars)
    print()
    assert s == 4
