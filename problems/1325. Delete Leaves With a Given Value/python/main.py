from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TN({self.val}, {str(self.left)}, {str(self.right)})"


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
            l.append(n)
            continue

        l.append(n.val)
        nodes.append(n.left)
        nodes.append(n.right)

    for i in range(len(l) - 1, -1, -1):
        if l[i] is not None:
            return l[: i + 1]

    return l


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        if root is None:
            return root

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.val == target and root.left is None and root.right is None:
            return None

        return root


if __name__ == "__main__":
    s = Solution()

    org = [1, 2, 3, 4, 5]
    new = lis(tn(org))
    assert org == new

    l = [1, 2, 3, 2, None, 2, 4]
    n = lis(tn(l))
    assert l == n

    got = lis(s.removeLeafNodes(tn(l), 2))
    exp = [
        1,
        None,
        3,
        None,
        4,
    ]
    assert got == exp
