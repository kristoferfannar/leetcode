from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tn(lis: list, idx=1):
    if idx > len(lis) or lis[idx - 1] is None:
        return None

    t = TreeNode(lis[idx - 1])
    t.left = tn(lis, idx * 2)
    t.right = tn(lis, idx * 2 + 1)

    return t


def lis(t: Optional[TreeNode]):
    l = []
    nodes = [t]

    while nodes:
        n = nodes.pop(0)
        if n is None:
            l.append(None)
            continue

        l.append(n.val)

        nodes.append(n.left)
        nodes.append(n.right)

    for i in range(len(l) - 1, -1, -1):
        if l[i] is not None:
            return l[: i + 1]

    return l


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = [(0, root)]
        levels = {}

        # first run, put values in list
        while nodes:
            lvl, n = nodes.pop(0)
            if n is None:
                continue

            if lvl % 2 == 1:
                if lvl not in levels:
                    levels[lvl] = []
                levels[lvl].append(n.val)

            nodes.append((lvl + 1, n.left))
            nodes.append((lvl + 1, n.right))

        nodes = [(0, root)]
        while nodes:
            lvl, n = nodes.pop(0)

            if n is None:
                continue

            if lvl % 2 == 1:
                n.val = levels[lvl].pop()

            nodes.append((lvl + 1, n.left))
            nodes.append((lvl + 1, n.right))

        return root


if __name__ == "__main__":
    org = [1, 2, 3, 4]
    new = lis(tn(org))
    assert org == new

    s = Solution()
    org = [2, 3, 5, 8, 13, 21, 34]
    got = lis(s.reverseOddLevels(tn(org)))
    exp = [
        2,
        5,
        3,
        8,
        13,
        21,
        34,
    ]

    assert got == exp
