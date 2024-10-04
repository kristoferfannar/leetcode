# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        num = (
            high + low
        ) >> 1  # more performant than dividing by 2 and wrapping int() around
        while (ans := guess(num)) != 0:
            # print(f"guess: {num}")
            if ans == -1:
                high = num
            else:
                low = num + 1  # >> 1 floors the float
            num = (high + low) >> 1

        return num
