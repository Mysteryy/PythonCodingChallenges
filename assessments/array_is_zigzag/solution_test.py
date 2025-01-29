import pytest
from .solution import solution


@pytest.mark.parametrize(
    "input_a, expected_output",
    [
        ([1, 2, 1, 3, 4], [1, 1, 0]),
        ([1, 2, 3, 4], [0, 0]),
        ([1, 3, 4, 5, 6, 14, 14], [0, 0, 0, 0, 0]),
        ([11, 14, 3, 17, 16, 13, 3, 7, 19, 8], [1, 1, 1, 0, 0, 1, 0, 1]),
    ]
)
def test_solution(input_a, expected_output):
    assert solution(input_a) == expected_output
