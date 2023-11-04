from twttr import shorten

def test_lower():
    assert shorten("ciao") == "c"
    assert shorten("hello") == "hll"
    assert shorten("hello, my name is simone") == "hll, my nm s smn"

def test_upper():
    assert shorten("HOW") == "HW"
    assert shorten("GUMMY BEAR") == "GMMY BR"
    assert shorten("WE ARE IN OCTOBER") == "W R N CTBR"

def test_mixed():
    assert shorten("Hi, TODAY is THE deadLINE") == "H, TDY s TH ddLN"
    assert shorten("I LK CS50 very much") == " LK CS50 vry mch"

