from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TN({self.val}, {str(self.left)}, {str(self.right)})"


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        levels = [[root]]
        lvl = 0
        ls = []

        while lvl < len(levels) and (curr_lvl := levels[lvl]) != []:
            next_lvl = []
            for node in curr_lvl:
                if node.left is not None:
                    next_lvl.append(node.left)

                if node.right is not None:
                    next_lvl.append(node.right)

            ls.append(curr_lvl[-1].val)
            levels.append(next_lvl)
            lvl += 1

        return ls


def from_tn(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    frontier: List[Optional[TreeNode]] = [root]
    ls = []

    while len(frontier) > 0:
        curr = frontier.pop(0)
        if curr is None:
            ls.append(None)
        else:
            ls.append(curr.val)
            frontier.append(curr.left)
            frontier.append(curr.right)

    while ls[-1] is None:
        ls.pop()

    return ls


def to_tn(ls: List[Optional[int]]) -> Optional[TreeNode]:
    if ls == []:
        return None

    def create_branch(ls: List[Optional[int]], idx: int):
        if len(ls) <= idx - 1 or (item := ls[idx - 1]) is None:
            return None
        return TreeNode(
            item,
            left=create_branch(ls, idx * 2),
            right=create_branch(ls, idx * 2 + 1),
        )

    return create_branch(ls, 1)


if __name__ == "__main__":
    ls = [1, 2, 3, None, 5, None, 4]
    s = Solution().rightSideView(to_tn(ls))
    print(s)
    assert s == [1, 3, 4]

    s = Solution().rightSideView(to_tn([1, 2]))
    print(s)
    assert s == [1, 2]
