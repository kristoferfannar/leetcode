class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        first, second, third = 0, 1, 1

        for _ in range(n - 2):
            fourth = first + second + third
            first = second
            second = third
            third = fourth

        return third


if __name__ == "__main__":
    s = Solution().tribonacci(4)
    print(s)
    assert s == 4

    s = Solution().tribonacci(25)
    print(s)
    assert s == 1389537
