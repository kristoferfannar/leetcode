from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == val:
            return root

        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)


if __name__ == "__main__":
    target = TreeNode(4)
    s = Solution().searchBST(
        TreeNode(
            10,
            TreeNode(2, None, TreeNode(5, target)),
            TreeNode(12, TreeNode(11), TreeNode(100)),
        ),
        4,
    )

    print(s)
    assert s == target
