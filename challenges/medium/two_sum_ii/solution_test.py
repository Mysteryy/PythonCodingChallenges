import pytest
from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "input_a, input_b, expected_output",
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2])
    ]
)
def test_solution(solution, input_a, input_b, expected_output):
    assert solution.twoSum(input_a, input_b) == expected_output
