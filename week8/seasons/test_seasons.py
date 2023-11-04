from seasons import subtraction
import pytest

def test_subtraction():
    assert subtraction(2022, 10, 26) == 525600
    assert subtraction(2021, 10, 26) == 525600 * 2
    with pytest.raises(ValueError):
        assert subtraction(2022, 13, 11)
    with pytest.raises(ValueError):
        assert subtraction(2022, 12, 32)