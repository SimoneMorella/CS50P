from plates import is_valid

def test_alphabetic_start():
    assert is_valid("4444") == False
    assert is_valid("CS50") == True

def test_length():
    assert is_valid("X") == False
    assert is_valid("TOOMUCH300") == False
    assert is_valid("TOOGG7") == True

def test_num_placement():
    assert is_valid("CS50X") == False
    assert is_valid("CAP69") == True
    assert is_valid("SHT21X") == False

def test_zero_placement():
    assert is_valid("CS050") == False
    assert is_valid("CSP50") == True

def test_alphanumeric():
    assert is_valid("PS4") == True
    assert is_valid("CS%=") == False
