from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        dummy = ListNode()
        current = dummy
        while l1 or l2 or remainder:
            current_a = 0 if not l1 else l1.val
            current_b = 0 if not l2 else l2.val
            current_sum = current_a + current_b + remainder
            remainder = current_sum // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            new_node = ListNode(current_sum % 10)
            current.next = new_node
            current = current.next

        return dummy.next
