from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"LN({self.val}, {str(self.next)})"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_lis = None
        curr = head

        while curr != None:
            new = ListNode()
            new.val = curr.val
            new.next = new_lis
            new_lis = new
            curr = curr.next

        if new_lis == None:
            return new_lis

        return new_lis


def to_list(head: Optional[ListNode]) -> list:
    lis = []

    while head != None:
        lis.append(head.val)
        head = head.next

    return lis


def from_list(head: list) -> Optional[ListNode]:
    if not head:
        return None

    ln = ListNode(head[0])
    last = ln

    for num in head[1:]:
        last.next = ListNode(num)
        last = last.next

    return ln


if __name__ == "__main__":
    s = Solution().reverseList(from_list([1, 2, 3, 4, 5]))
    print(to_list(s))
    assert to_list(s) == [5, 4, 3, 2, 1]

    s = Solution().reverseList(from_list([1, 2]))
    print(to_list(s))
    assert to_list(s) == [2, 1]
