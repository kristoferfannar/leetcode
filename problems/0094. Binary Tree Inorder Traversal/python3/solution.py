from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )


if __name__ == "__main__":
    s = Solution().inorderTraversal(
        TreeNode(4, TreeNode(3), TreeNode(10, TreeNode(11)))
    )
    print(s)
    assert s == [3, 4, 11, 10]
