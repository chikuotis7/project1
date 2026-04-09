import pytest
from src.math_operations import add, sub, mul, div


class TestMathOperations:

    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0

    def test_sub(self):
        assert sub(5, 3) == 2
        assert sub(3, 5) == -2
        assert sub(0, 0) == 0

    def test_mul(self):
        assert mul(2, 3) == 6
        assert mul(-1, 5) == -5
        assert mul(0, 10) == 0

    def test_div(self):
        assert div(6, 3) == 2
        assert div(5, 2) == 2.5

    def test_div_by_zero(self):
        with pytest.raises(ValueError):
            div(10, 0)