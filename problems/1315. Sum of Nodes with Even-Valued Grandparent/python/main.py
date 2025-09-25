from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tn(lis, idx=1):
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
    def add(self, node: Optional[TreeNode], parent_val: int) -> int:
        total = 0

        if node is None:
            return total

        if node.left:
            if parent_val % 2 == 0:
                total += node.left.val

            total += self.add(node.left, node.val)

        if node.right:
            if parent_val % 2 == 0:
                total += node.right.val

            total += self.add(node.right, node.val)

        return total

    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        total = 0

        if root is None:
            return total

        total += self.add(root.left, root.val)
        total += self.add(root.right, root.val)

        return total


if __name__ == "__main__":
    org = [1, 2, 3, 4]
    new = lis(tn(org))
    assert org == new

    s = Solution()

    l = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
    n = lis(tn(l))

    assert l == n

    assert (
        s.sumEvenGrandparent(
            tn([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5])
        )
        == 18
    )
