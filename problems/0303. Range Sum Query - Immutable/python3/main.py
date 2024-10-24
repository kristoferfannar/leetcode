from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        self.sums[0] = nums[0]

        for i in range(1, len(nums)):
            self.sums[i] = nums[i] + self.sums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]

        return self.sums[right] - self.sums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


if __name__ == "__main__":
    na = NumArray([-2, 0, 3, -5, 2, -1])
    assert na.sumRange(0, 2) == 1
    assert na.sumRange(2, 5) == -1
    assert na.sumRange(0, 5) == -3
