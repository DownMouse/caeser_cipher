from valident import *
import pytest

def test_valid_key():
    assert v_key("5") == 5

def test_negative_key():
    assert v_key("-3") == -3

def test_invalid():
    with pytest.raises(ValueError):
        v_key("abc")
