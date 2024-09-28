from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """Should ideally use dynamic programming for most optimal answer
        But the problem is rated easy so I didn't bother"""

        flowers_left = n

        if sum(flowerbed[:2]) == 0:
            flowerbed[0] = 1
            flowers_left -= 1

        for idx in range(1, len(flowerbed) - 1):
            if sum(flowerbed[idx - 1 : idx + 2]) == 0:
                flowerbed[idx] = 1
                flowers_left -= 1

        if sum(flowerbed[-2:]) == 0:
            flowerbed[-1] = 1
            flowers_left -= 1

        return flowers_left <= 0


if __name__ == "__main__":
    s = Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1)
    print(s)
    assert s == True

    s = Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2)
    print(s)
    assert s == False
