import unittest

from challenges.easy.merge_two_sorted_linked_lists.solution_test import linkedlist_to_list, list_to_linkedlist
from .solution import Solution, ListNode


def list_to_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head


def linked_list_to_list(head: ListNode):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        input_a = [2, 4, 3]
        input_b = [5, 6, 4]
        expected_output = [7, 0, 8]
        self.assertEqual(linked_list_to_list(solution.addTwoNumbers(list_to_linked_list(input_a), list_to_linked_list(input_b))), expected_output)

    def test2(self):
        solution = Solution()
        input_a = [0]
        input_b = [0]
        expected_output = [0]
        self.assertEqual(linked_list_to_list(solution.addTwoNumbers(list_to_linked_list(input_a), list_to_linked_list(input_b))), expected_output)

    def test3(self):
        solution = Solution()
        input_a = [9, 9, 9, 9, 9, 9, 9]
        input_b = [9, 9, 9, 9]
        expected_output = [8, 9, 9, 9, 0, 0, 0, 1]
        self.assertEqual(linked_list_to_list(solution.addTwoNumbers(list_to_linked_list(input_a), list_to_linked_list(input_b))), expected_output)

    def test4(self):
        solution = Solution()
        input_a = [1]
        input_b = [9, 9, 9]
        expected_output = [0, 0, 0, 1]
        self.assertEqual(linked_list_to_list(solution.addTwoNumbers(list_to_linked_list(input_a), list_to_linked_list(input_b))), expected_output)

    def test5(self):
        solution = Solution()
        input_a = [2, 4, 3]
        input_b = [5, 6, 4, 9]
        expected_output = [7, 0, 8, 9]
        self.assertEqual(linked_list_to_list(solution.addTwoNumbers(list_to_linked_list(input_a), list_to_linked_list(input_b))), expected_output)

    def test6(self):
        solution = Solution()
        input_a = [9, 9, 9]
        input_b = [1]
        expected_output = [0, 0, 0, 1]
        self.assertEqual(linked_list_to_list(solution.addTwoNumbers(list_to_linked_list(input_a), list_to_linked_list(input_b))), expected_output)

    def test7(self):
        solution = Solution()
        input_a = [5]
        input_b = [5]
        expected_output = [0, 1]
        self.assertEqual(linked_list_to_list(solution.addTwoNumbers(list_to_linked_list(input_a), list_to_linked_list(input_b))), expected_output)

    def test8(self):
        solution = Solution()
        input_a = [1, 8]
        input_b = [0]
        expected_output = [1, 8]
        self.assertEqual(linked_list_to_list(solution.addTwoNumbers(list_to_linked_list(input_a), list_to_linked_list(input_b))), expected_output)

    def test9(self):
        solution = Solution()
        input_a = [0]
        input_b = [1, 2, 3]
        expected_output = [1, 2, 3]
        self.assertEqual(linked_list_to_list(solution.addTwoNumbers(list_to_linked_list(input_a), list_to_linked_list(input_b))), expected_output)

    def test10(self):
        solution = Solution()
        input_a = [9, 9]
        input_b = [1]
        expected_output = [0, 0, 1]
        self.assertEqual(linked_list_to_list(solution.addTwoNumbers(list_to_linked_list(input_a), list_to_linked_list(input_b))), expected_output)
