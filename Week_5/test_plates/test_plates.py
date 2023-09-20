from plates import is_valid
import pytest

def test_twoletters():
    assert is_valid("CS") == True
    assert is_valid("C5") == False
    assert is_valid("50") == False
    assert is_valid("4") == False


def test_platelength():
    assert is_valid("THIS50") == True
    assert is_valid("CS") == True
    assert is_valid("THISISCS50") == False



def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False



def test_punctuations():
    assert is_valid("CS50.") == False