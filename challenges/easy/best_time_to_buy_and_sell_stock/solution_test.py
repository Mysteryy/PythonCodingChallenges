import pytest
from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "input_a, expected_output",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0)
    ]
)
def test_solution(solution, input_a, expected_output):
    assert solution.maxProfit(input_a) == expected_output
