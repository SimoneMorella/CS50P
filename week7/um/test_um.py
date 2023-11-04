from um import count

def test_start():
    assert count("um, my name is") == 1
    assert count("ummus") == 0
    assert count("um,ok") == 1

def test_end():
    assert count("I think the word is um") == 1
    assert count("um um um") == 3
    assert count("mum") == 0

def test_case():
    assert count("UM OK") == 1
    assert count("ok HUMMUS is right") == 0
    assert count("yes man, UM right") == 1