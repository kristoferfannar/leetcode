from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TN({self.val}, {self.left}, {self.right})"


class Solution:
    def create_mapping(
        self, root: Optional[TreeNode]
    ) -> dict[int, tuple[TreeNode, TreeNode, int]]:
        mapping: dict[int, tuple[TreeNode, TreeNode, int]] = dict()

        if root is None:
            return mapping

        nodes: List[tuple[TreeNode, TreeNode]] = [(root, root)]
        idx = 0

        while idx < len(nodes):
            curr, parent = nodes[idx]

            if curr.left:
                nodes.append((curr.left, curr))
            if curr.right:
                nodes.append((curr.right, curr))

            idx += 1

        # recursively find node's height
        def node_height(node, parent):
            if not node.left and not node.right:
                height = 0
            else:
                l = r = 0

                if node.left:
                    l = node_height(node.left, node)

                if node.right:
                    r = node_height(node.right, node)

                height = max(l, r) + 1

            mapping[node.val] = (node, parent, height)
            return height

        node_height(root, root)

        return mapping

    def get_ans(
        self, mapping: dict[int, tuple[TreeNode, TreeNode, int]], q: int
    ) -> int:
        node, parent, _ = mapping[q]
        # new node's height will be 0
        height = -1

        def get_new_parent_height(
            parent: TreeNode, changed_val: int, changed_height: int
        ) -> int:
            left_val = -float("inf")
            if parent.left is not None:
                if parent.left.val == changed_val:
                    left_val = changed_height
                else:
                    left_val = mapping[parent.left.val][2]

            right_val = -float("inf")
            if parent.right is not None:
                if parent.right.val == changed_val:
                    right_val = changed_height
                else:
                    right_val = mapping[parent.right.val][2]

            # print(
            #     f"TN({parent.val}, l-{left_val} r-{right_val}) = {int(max(float(left_val), float(right_val))) + 1}"
            # )

            return int(max(float(left_val), float(right_val))) + 1

        # node == parent when node == root
        while node != parent:
            height = get_new_parent_height(parent, q, height)
            # get the parent's parent,
            # move up a generation
            node, parent, _ = mapping[parent.val]
            q = node.val

        return height

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        mapping = self.create_mapping(root)

        # for k, v in mapping.items():
        #     print(f"{k} -> ({v[1].val}, {v[2]})")
        # print()

        ans = []

        for q in queries:
            ans.append(self.get_ans(mapping, q))

        return ans


def to_tn(lis) -> Optional[TreeNode]:

    def create_node(lis, i) -> Optional[TreeNode]:
        l = r = None
        if lis[i - 1] is None:
            return None

        if i * 2 - 1 < len(lis):
            l = create_node(lis, i * 2)
        if i * 2 < len(lis):
            r = create_node(lis, i * 2 + 1)

        return TreeNode(lis[i - 1], l, r)

    return create_node(lis, 1)


def from_tn(root: Optional[TreeNode]) -> List[Optional[int]]:
    lis = []

    frontier = [root]

    while frontier and any(frontier):
        curr = frontier.pop(0)

        if curr:
            lis.append(curr.val)
            frontier.append(curr.left)
            frontier.append(curr.right)
        else:
            lis.append(None)
            frontier.append(None)
            frontier.append(None)

    return lis


if __name__ == "__main__":
    lis = [1, 3, 4, 2, None, 6, 5, None, None, None, None, None, None, None, 7]
    tn = to_tn(lis)

    s = Solution().treeQueries(tn, [4])
    print(s)
    assert s == [2]

    lis = [5, 8, 9, 2, 1, 3, 7, 4, 6]
    tn = to_tn(lis)
    s = Solution().treeQueries(tn, [3, 2, 4, 8])
    print(s)
    assert s == [3, 2, 3, 2]

    lis = [1, None, 5, None, None, 3, None, None, None, None, None, 2, 4]
    #         1
    #      -    5
    #     - -  3 -
    #    ---- 24--
    tn = to_tn(lis)
    s = Solution().treeQueries(tn, [3, 5, 4, 2, 4])
    print(s)
    assert s == [1, 0, 3, 3, 3]
