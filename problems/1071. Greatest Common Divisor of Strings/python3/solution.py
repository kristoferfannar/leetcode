class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_divisors = [x for x in range(1, len(str1) + 1) if len(str1) % x == 0]
        str2_divisors = [x for x in range(1, len(str2) + 1) if len(str2) % x == 0]

        divisors = [x for x in str1_divisors if x in str2_divisors]

        # print(str1_divisors)
        # print(str2_divisors)
        # print(divisors)

        best_curr_gcd = ""
        for div in divisors:
            valid = True
            div_idx = div - 1
            if str1[div_idx] != str2[div_idx]:
                return best_curr_gcd

            candidate = str1[:div]

            for idx in range(0, len(str1), div):
                if str1[idx : div + idx] != candidate:
                    # try next divisor
                    valid = False

            for idx in range(0, len(str2), div):
                if str2[idx : div + idx] != candidate:
                    # try next divisor
                    valid = False

            # candidate is valid
            if valid:
                best_curr_gcd = candidate

        return best_curr_gcd


if __name__ == "__main__":
    str1, str2 = "abab", "ab"
    s = Solution().gcdOfStrings(str1, str2)
    print(s)
    assert s == "ab"

    str1, str2 = "ABABAB", "ABAB"
    s = Solution().gcdOfStrings(str1, str2)
    print(s)
    assert s == "AB"

    s = Solution().gcdOfStrings("ABCDEF", "ABC")
    print(s)
    assert s == ""
