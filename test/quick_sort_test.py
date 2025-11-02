from tinypysort.quick_sort import quick_sort
import pytest


@pytest.mark.parametrize(
    ["input", "output"],
    [
        ([4, 3, 2, 0, -1, 4, 3], [-1, 0, 2, 3, 3, 4, 4]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        (
            [5, 4, 1, 13, 345, 1, 403, -14, -5, 1],
            [-14, -5, 1, 1, 1, 4, 5, 13, 345, 403],
        ),
    ],
)
def test_quick_sort(input, output):
    assert quick_sort(input) == output
