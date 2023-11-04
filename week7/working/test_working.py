from working import convert
import pytest


def test_syntax():
    with pytest.raises(ValueError):
        assert convert("9.00 AM to 5.00 PM")
    with pytest.raises(ValueError):
        assert convert("9:00 AM 5:00 PM")
    with pytest.raises(ValueError):
        assert convert("9:00AM to 5:00PM")
    with pytest.raises(ValueError):
        assert convert("9:00 am to 5:00 pm")
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_hours():
    with pytest.raises(ValueError):
        assert convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        assert convert("9:00 AM to 13:00 PM")
    with pytest.raises(ValueError):
        assert convert("0:00 AM to 11:00 PM")
    with pytest.raises(ValueError):
        assert convert("9:00 AM 00:00 PM")
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_minutes():
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        assert convert("9:00 AM to 5:60 PM")
    with pytest.raises(ValueError):
        assert convert("9:59 AM to 5:70 PM")
    with pytest.raises(ValueError):
        assert convert("9:70 AM to 5:00 PM")
    assert convert("9:59 AM to 5:59 PM") == "09:59 to 17:59"
