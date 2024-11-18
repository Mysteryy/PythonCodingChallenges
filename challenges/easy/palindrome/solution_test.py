import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "input_a, expected_output",
    [
        (121, True),   # Test case 1
        (-121, False), # Test case 2
        (10, False),   # Test case 3
    ],
)
def test_is_palindrome(input_a, expected_output):
    solution = Solution()
    assert solution.isPalindrome(input_a) == expected_output