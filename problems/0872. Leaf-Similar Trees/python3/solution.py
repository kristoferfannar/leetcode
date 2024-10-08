from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TN({self.val}, {str(self.left)}, {str(self.right)})"


class Solution:
    def __leafs(self, root: TreeNode) -> list:
        if root.left == None and root.right == None:
            return [root.val]

        if root.right == None and root.left is not None:
            return self.__leafs(root.left)

        if root.left == None and root.right is not None:
            return self.__leafs(root.right)

        return self.__leafs(root.left) + self.__leafs(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = []
        leafs2 = []

        if root1 != None:
            leafs1 = self.__leafs(root1)
        if root2 != None:
            leafs2 = self.__leafs(root2)

        return leafs1 == leafs2


def to_tn(lis):
    return create_node(lis, 1)


def create_node(lis, idx):
    if len(lis) < idx or lis[idx - 1] is None:
        return None

    left = create_node(lis, idx * 2)
    right = create_node(lis, idx * 2 + 1)

    return TreeNode(lis[idx - 1], left, right)


if __name__ == "__main__":
    s = Solution().leafSimilar(
        to_tn([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
        to_tn([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]),
    )
    print(s)
    assert s == True
