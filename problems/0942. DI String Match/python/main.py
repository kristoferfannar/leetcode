from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo = 0
        hi = len(s)

        out = [-1] * (len(s) + 1)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "D":
                out[i + 1] = lo
                lo += 1
            else:
                out[i + 1] = hi
                hi -= 1

        assert lo == hi
        out[0] = lo

        return out


def is_good(text, arr):
    for i in range(len(text)):
        if text[i] == "I":
            if arr[i] >= arr[i + 1]:
                return False
        if text[i] == "D":
            if arr[i] <= arr[i + 1]:
                return False

    return True


if __name__ == "__main__":
    s = Solution()
    assert is_good("IDID", s.diStringMatch("IDID"))
    assert is_good("III", s.diStringMatch("III"))
    assert is_good("DDI", s.diStringMatch("DDI"))
