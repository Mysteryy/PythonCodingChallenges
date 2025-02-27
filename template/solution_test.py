import pytest
from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "input_a, expected_output",
    [
        (1, True),
        (2, False)
    ]
)
def test_solution(solution, input_a, expected_output):
    assert solution.solution(input_a) == expected_output
