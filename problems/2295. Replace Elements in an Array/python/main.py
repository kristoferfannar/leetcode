from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        forward = {num: num for num in nums}
        backward = {num: num for num in nums}

        for from_op, to_op in operations:
            actual = backward[from_op]

            forward[actual] = to_op
            backward[to_op] = actual

        return [forward[num] for num in nums]


if __name__ == "__main__":
    s = Solution()

    assert s.arrayChange([1, 2, 4, 6], [[1, 3], [4, 7], [6, 1]]) == [3, 2, 7, 1]
    assert s.arrayChange([1, 2], [[1, 3], [2, 1], [3, 2]]) == [2, 1]
