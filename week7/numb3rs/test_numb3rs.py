from numb3rs import validate

def test_all_byte():
    assert validate("255.13.13.290") == False
    assert validate("255.299.0.3") == False
    assert validate("255.255.255.255") == True
    assert validate("192.168.256.0") == False

def test_limits():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("256.0.0.0") == False