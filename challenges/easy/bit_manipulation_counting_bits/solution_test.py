import pytest
from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "input_a, expected_output",
    [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2])
    ]
)
def test_solution(solution, input_a, expected_output):
    assert solution.countBits(input_a) == expected_output
