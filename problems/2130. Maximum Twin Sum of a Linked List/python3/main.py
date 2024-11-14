from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        items = []

        curr = head
        while curr:
            items.append(curr.val)
            curr = curr.next

        max_twin = items[0] + items[-1]
        for i in range(len(items) // 2):
            max_twin = max(max_twin, items[i] + items[len(items) - i - 1])

        return max_twin


def to_ln(lis):
    if not lis:
        return None

    front = ListNode(val=lis[0])
    curr = front

    for item in lis[1:]:
        new = ListNode(item)
        curr.next = new
        curr = new

    return front


def from_ln(ln):
    lis = []

    while ln:
        lis.append(ln.val)
        ln = ln.next

    return lis


if __name__ == "__main__":
    assert Solution().pairSum(to_ln([5, 4, 2, 1])) == 6
    assert Solution().pairSum(to_ln([4, 2, 2, 3])) == 7
    assert Solution().pairSum(to_ln([1, 100000])) == 100001
