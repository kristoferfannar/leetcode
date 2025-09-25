from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        out = ""
        lookup = {k: v for k, v in knowledge}
        idx = 0

        while (open := s.find("(", idx)) != -1:
            close = s.find(")", open)
            substr = s[open + 1 : close]

            out += s[idx:open]

            if substr in lookup:
                out += lookup[substr]
            else:
                out += "?"

            idx = close + 1

        out += s[idx:]

        return out


if __name__ == "__main__":
    s = Solution()
    assert (
        s.evaluate("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]])
        == "bobistwoyearsold"
    )

    assert s.evaluate("hi(name)", [["a", "b"]]) == "hi?"

    assert s.evaluate("(a)(a)(a)aaa", [["a", "yes"]]) == "yesyesyesaaa"
