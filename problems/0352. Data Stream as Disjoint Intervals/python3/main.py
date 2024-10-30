from typing import List, Optional
import random


class BST:
    def __init__(self, val: int, l=None, r=None) -> None:
        self.val = val
        self.l = l or val
        self.r = r or val
        self.left = None
        self.right = None

    def add(self, val: int):
        if val < self.val:
            if self.left:
                self.left.add(val)
            else:
                self.left = BST(val)
                return self.left
        elif self.val < val:
            if self.right:
                self.right.add(val)
            else:
                self.right = BST(val)
                return self.right

    def get_interval(self, val: int) -> Optional[tuple[int, int]]:
        if val < self.val:
            if not self.left:
                return None
            return self.left.get_interval(val)

        elif self.val < val:
            if not self.right:
                return None
            return self.right.get_interval(val)

        return (self.l, self.r)

    def exists(self, val: int) -> bool:
        if val < self.val:
            if not self.left:
                return False
            return self.left.exists(val)

        if self.val < val:
            if not self.right:
                return False
            return self.right.exists(val)

        return True

    def set_interval(self, val: int, l: int, r: int) -> None:
        if val == self.val:
            self.l = l
            self.r = r

        elif val < self.val:
            if not self.left:
                return None
            return self.left.set_interval(val, l, r)

        elif self.val < val:
            if not self.right:
                return None
            return self.right.set_interval(val, l, r)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = f"{self.val}"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = f"{self.val}"
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = f"{self.val}"
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = f"{self.val}"
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


class SummaryRanges:
    def __init__(self):
        self.tree: Optional[BST] = None

        # use union find to group items in intervals
        self.intervals: dict[tuple[int, int], set[int]] = dict()

    def addNum(self, value: int) -> None:
        if not self.tree:
            self.tree = BST(value)
        elif self.tree.exists(value):
            return
        else:
            self.tree.add(value)

        i1 = self.tree.get_interval(value - 1)
        i2 = self.tree.get_interval(value + 1)

        if i1 and i2:
            # combine intervals for all values in i1 and i2
            i1_nums = self.intervals[i1]
            i2_nums = self.intervals[i2]

            new_i = (i1[0], i2[1])
            new_nums = i1_nums.union(i2_nums)
            new_nums.add(value)

            # set new interval for all numbers in i1 and i2
            # combining intervals with union find is slow...
            # we might need to convert to WQU
            for num in list(new_nums):
                self.tree.set_interval(num, new_i[0], new_i[1])

            self.intervals[new_i] = new_nums

            del self.intervals[i1]
            del self.intervals[i2]

        elif i1:
            i1_nums = self.intervals[i1]
            i1_nums.add(value)

            new_i = (i1[0], value)

            for num in list(i1_nums):
                self.tree.set_interval(num, new_i[0], new_i[1])

            del self.intervals[i1]
            self.intervals[new_i] = i1_nums

        elif i2:
            i2_nums = self.intervals[i2]
            i2_nums.add(value)

            new_i = (value, i2[1])

            for num in list(i2_nums):
                self.tree.set_interval(num, new_i[0], new_i[1])

            del self.intervals[i2]
            self.intervals[new_i] = i2_nums
        else:
            # initialize interval with
            self.intervals[(value, value)] = set([value])

    def getIntervals(self) -> List[List[int]]:
        ints = []
        for interval in self.intervals.keys():
            ints.append(interval)

        ints.sort(key=lambda i: i[0])

        return ints


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()


if __name__ == "__main__":
    # sr = SummaryRanges()
    # lis = list(set([random.randint(0, 20) for _ in range(20)]))
    # random.shuffle(lis)
    # for num in lis:
    #     sr.addNum(num)
    #     input("ENTER: ")

    # sr = SummaryRanges()
    # sr.addNum(1)
    # assert sr.getIntervals() == [(1, 1)]
    # sr.addNum(3)
    # assert sr.getIntervals() == [(1, 1), (3, 3)]
    # sr.addNum(7)
    # assert sr.getIntervals() == [(1, 1), (3, 3), (7, 7)]
    # sr.addNum(2)
    # assert sr.getIntervals() == [(1, 3), (7, 7)]
    # sr.addNum(6)
    # assert sr.getIntervals() == [(1, 3), (6, 7)]

    sr = SummaryRanges()
    sr.addNum(6)
    assert sr.getIntervals() == [(6, 6)]
    sr.addNum(6)
    assert sr.getIntervals() == [(6, 6)]
    sr.addNum(0)
    assert sr.getIntervals() == [(0, 0), (6, 6)]
    sr.addNum(4)
    assert sr.getIntervals() == [(0, 0), (4, 4), (6, 6)]
    sr.addNum(8)
    assert sr.getIntervals() == [(0, 0), (4, 4), (6, 6), (8, 8)]
    sr.addNum(7)
    assert sr.getIntervals() == [(0, 0), (4, 4), (6, 8)]
    sr.addNum(6)
    assert sr.getIntervals() == [(0, 0), (4, 4), (6, 8)]
    sr.addNum(4)
    assert sr.getIntervals() == [(0, 0), (4, 4), (6, 8)]
    sr.addNum(7)
    assert sr.getIntervals() == [(0, 0), (4, 4), (6, 8)]
    sr.addNum(5)
    assert sr.getIntervals() == [(0, 0), (4, 8)]
