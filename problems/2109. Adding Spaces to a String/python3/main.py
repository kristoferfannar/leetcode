from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        newstr = [""] * (len(s) + len(spaces))
        new_i = 0
        s_i = 0

        for i in range(len(s)):
            # print(f"new_i-{new_i}, i-{i} | {newstr}")
            while len(spaces) > s_i and new_i - s_i == spaces[s_i]:
                newstr[new_i] = " "
                s_i += 1
                new_i += 1

            newstr[new_i] = s[i]
            new_i += 1

        # print("".join(newstr))
        return "".join(newstr)


if __name__ == "__main__":

    assert (
        Solution().addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15])
        == "Leetcode Helps Me Learn"
    )
