from bank import value

def test_syntax():
    assert value("Hello my name is") == 0
    assert value("HI my friend") == 20
    assert value("HeLlO") == 0

def test_char():
    assert value("1 hot-dog") == 100
    assert value("...hello") == 100

def test_sentences():
    assert value("hi my name is Simone") == 20
    assert value("Goodevening, hello the weather is good") == 100

def test_repetition():
    assert value("hi, hello, buonasera") == 20
    assert value("ciao, hello, hi") == 100

