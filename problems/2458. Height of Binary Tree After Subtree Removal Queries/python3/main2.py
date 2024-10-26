# From
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/solutions/3066381/python-simple-dfs
from typing import Optional, List
from collections import deque

from test import lis as LIS
from queries import queries as QUERIES

from functools import lru_cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TN({self.val}, {self.left}, {self.right})"


class Solution:

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        @lru_cache(None)
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return -1

            return max(height(node.left), height(node.right)) + 1

        d = dict()

        def dfs(node, depth, max_len):
            if not node:
                return

            d[node.val] = max_len

            dfs(node.left, depth + 1, max(max_len, depth + 1 + height(node.right)))
            dfs(node.right, depth + 1, max(max_len, depth + 1 + height(node.left)))

        dfs(root, 0, 0)

        return [d[i] for i in queries]


def to_tn_2(lis) -> Optional[TreeNode]:
    if not lis:
        return None

    root = TreeNode(lis[0])
    queue = deque([root])
    i = 1  # Start from the first child index

    while queue and i < len(lis):
        current = queue.popleft()

        # Add the left child if it's not None
        if i < len(lis) and lis[i] is not None:
            current.left = TreeNode(lis[i])
            queue.append(current.left)
        i += 1  # Move to the next element in the list

        # Add the right child if it's not None
        if i < len(lis) and lis[i] is not None:
            current.right = TreeNode(lis[i])
            queue.append(current.right)
        i += 1  # Move to the next element in the list

    return root


if __name__ == "__main__":
    # lis = [1, 3, 4, 2, None, 6, 5, None, None, None, None, None, 7]
    # tn = to_tn_2(lis)
    # s = Solution().treeQueries(tn, [4])
    # print(s)
    # assert s == [2]

    # lis = [5, 8, 9, 2, 1, 3, 7, 4, 6]
    # tn = to_tn_2(lis)
    # s = Solution().treeQueries(tn, [3, 2, 4, 8])
    # print(s)
    # assert s == [3, 2, 3, 2]

    # lis = [1, None, 5, 3, None, 2, 4]
    #         1
    #      -    5
    #     - -  3 -
    #    ---- 24--
    # tn = to_tn_2(lis)
    # s = Solution().treeQueries(tn, [3, 5, 4, 2, 4])
    # print(s)
    # assert s == [1, 0, 3, 3, 3]

    print(f"len(LIS)...")
    print(f"{len(LIS)}...")

    print(f"len(QUERIES)...")
    print(f"{len(QUERIES)}...")

    tn = to_tn_2(LIS)

    s = Solution().treeQueries(tn, QUERIES[:1000])
    print(s)
