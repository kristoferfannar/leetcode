from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TN({self.val}, {self.left}, {self.right})"


class Solution:
    def __sum_levels(self, root: TreeNode) -> dict[int, int]:
        levelsums = dict()
        frontier: list[tuple[int, TreeNode]] = [(1, root)]

        while frontier:
            lvl, curr = frontier.pop(0)
            if lvl not in levelsums:
                levelsums[lvl] = 0

            levelsums[lvl] += curr.val

            if curr.left:
                frontier.append((lvl + 1, curr.left))
            if curr.right:
                frontier.append((lvl + 1, curr.right))

        return levelsums

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        lvlsums = self.__sum_levels(root)

        cp_head = TreeNode(0)
        frontier: list[tuple[int, Optional[TreeNode], Optional[TreeNode]]] = [
            (1, cp_head, root)
        ]
        while frontier:
            lvl, cp, curr = frontier.pop(0)
            child_sum = 0

            if not curr:
                continue

            if curr.left:
                child_sum += curr.left.val
            if curr.right:
                child_sum += curr.right.val

            if curr.left:
                cp.left = TreeNode(lvlsums[lvl + 1] - child_sum)
            frontier.append((lvl + 1, cp.left, curr.left))

            if curr.right:
                cp.right = TreeNode(lvlsums[lvl + 1] - child_sum)
            frontier.append((lvl + 1, cp.right, curr.right))

        return cp_head


def from_tn(tn):
    lis = []
    frontier = [tn]

    while frontier:
        curr = frontier.pop(0)
        if curr is None:
            lis.append(None)
        else:
            lis.append(curr.val)
            frontier.extend([curr.left, curr.right])

    # remove trailing Nones
    for i in range(len(lis) - 1, -1, -1):
        if lis[i] is not None:
            break
        lis.pop()
    return lis


def to_tn(lis):
    if not lis:
        return None

    def create_tn(lis, pos):
        l = r = None
        if pos * 2 < len(lis) + 1:
            l = create_tn(lis, pos * 2)
        if pos * 2 + 1 < len(lis) + 1:
            r = create_tn(lis, pos * 2 + 1)

        if not lis[pos - 1]:
            return None
        return TreeNode(lis[pos - 1], l, r)

    return create_tn(lis, 1)


if __name__ == "__main__":
    lis = [5, 4, 9, 1, 10, None, 7]
    s = Solution().replaceValueInTree(to_tn(lis))
    s = from_tn(s)
    assert s == [
        0,
        0,
        0,
        7,
        7,
        None,
        11,
    ]

    s = from_tn(Solution().replaceValueInTree(to_tn([3, 1, 2])))
    assert s == [0, 0, 0]
