from typing import List


def mid(l, r):
    return l + (r - l) // 2


class Segment:
    def __init__(self, arr, l, r) -> None:
        self.l = l
        self.r = r
        self.left = self.right = None
        if l == r:
            self.val = arr[l]
            return

        m = mid(l, r)
        self.left = Segment(arr, l, m)
        self.right = Segment(arr, m + 1, r)

        self.val = self.left.val + self.right.val

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def update(self, idx, val):
        # print(f"update({idx}, {val}) on [{self.l}, {self.r}]")
        if self.l == self.r == idx:
            self.val = val
            return

        if idx < self.l or self.r < idx:
            raise Exception("This shouldn't happen")

        m = mid(self.l, self.r)

        if idx <= m:
            self.left.update(idx, val)

        elif m < idx:
            self.right.update(idx, val)

        self.val = self.left.val + self.right.val

    def sum(self, l, r):
        # print(f"sum({l}, {r}) on [{self.l}, {self.r}]")
        if l <= self.l and self.r <= r:
            return self.val

        sum = 0

        m = mid(self.l, self.r)

        if l <= m:
            sum += self.left.sum(l, r)

        if m < r:
            sum += self.right.sum(l, r)

        return sum

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = f"[{self.l},{self.r}]={self.val}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = f"[{self.l},{self.r}]={self.val}"
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = f"[{self.l},{self.r}]={self.val}"
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = f"[{self.l},{self.r}]={self.val}"
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class NumArray:
    def __init__(self, nums: List[int]):
        self.tree = Segment(nums, 0, len(nums) - 1)
        # self.tree.display()

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.sum(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


if __name__ == "__main__":
    na = NumArray([1, 8, 4, 10, 3, 0, -10, 50])
    assert na.sumRange(0, 3) == 23
    assert na.sumRange(0, 4) == 26
    assert na.sumRange(2, 6) == 7
    na.update(0, 4)
    assert na.sumRange(0, 3) == 26
    assert na.sumRange(0, 4) == 29
    assert na.sumRange(2, 6) == 7

    na = NumArray([1, 3, 5])
    assert na.sumRange(0, 2) == 9
    na.update(1, 2)
    assert na.sumRange(0, 2) == 8

    na = NumArray([0, 9, 5, 7, 3])
    assert na.sumRange(4, 4) == 3
    assert na.sumRange(2, 4) == 15
    assert na.sumRange(3, 3) == 7
    na.update(4, 5)
    # [0, 9, 5, 7, 5]
    na.update(1, 7)
    # [0, 7, 5, 7, 5]
    na.update(0, 8)
    # [8, 7, 5, 7, 5]
    assert na.sumRange(1, 2) == 12
    na.update(1, 9)
    # [8, 9, 5, 7, 5]
    assert na.sumRange(4, 4) == 5
    na.update(3, 4)
