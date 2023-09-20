from twttr import shorten
import pytest

def test_twttr():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('hello world') == 'hll wrld'
    assert shorten('TWITTER WORLD') == 'TWTTR WRLD'
    assert shorten('TW1TT3R W0RLD!') == 'TW1TT3R W0RLD!'