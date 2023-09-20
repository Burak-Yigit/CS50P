from bank import value
import pytest

def test_greeting():
    assert value("hello bro") == 0
    assert value("HELLO MATE") == 0
    assert value("hire me") == 20
    assert value("HIRE ME") == 20
    assert value("thats lame bro") == 100
    assert value("THATS LAME BRO") == 100