import pytest
from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "input_a, expected_output",
    [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False)
    ]
)
def test_solution(solution, input_a, expected_output):
    assert solution.canJump(input_a) == expected_output
