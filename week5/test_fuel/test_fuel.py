from fuel import convert, gauge
import pytest

def test_int():
    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert convert("1/4") == 25
    assert convert("5/9") == 56

def test_valuerror():
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("6/1")

def test_zerodiverror():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_empty_tank():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_perc_tank():
    assert gauge(50) == "50%"
    assert gauge(80) == "80%"

def test_full_tank():
    assert gauge(99) == "F"
    assert gauge(100) == "F"