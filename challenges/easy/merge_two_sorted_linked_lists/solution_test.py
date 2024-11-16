import unittest
from .solution import Solution, ListNode


# Helper functions
def list_to_linkedlist(arr):
    """Helper function to convert a list to a linked list."""
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linkedlist_to_list(node):
    """Helper function to convert a linked list back to a regular list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class SolutionTests(unittest.TestCase):
    def test1(self):
        sol = Solution()
        list1 = list_to_linkedlist([1, 2, 4])
        list2 = list_to_linkedlist([1, 3, 4])
        merged = sol.mergeTwoLists(list1, list2)
        self.assertEqual(linkedlist_to_list(merged), [1, 1, 2, 3, 4, 4])

    def test2(self):
        sol = Solution()
        list1 = list_to_linkedlist([])
        list2 = list_to_linkedlist([0])
        merged = sol.mergeTwoLists(list1, list2)
        self.assertEqual(linkedlist_to_list(merged), [0])

    def test3(self):
        sol = Solution()
        list1 = list_to_linkedlist([])
        list2 = list_to_linkedlist([])
        merged = sol.mergeTwoLists(list1, list2)
        self.assertEqual(linkedlist_to_list(merged), [])

    def test4(self):
        sol = Solution()
        list1 = list_to_linkedlist([5])
        list2 = list_to_linkedlist([3])
        merged = sol.mergeTwoLists(list1, list2)
        self.assertEqual(linkedlist_to_list(merged), [3, 5])
