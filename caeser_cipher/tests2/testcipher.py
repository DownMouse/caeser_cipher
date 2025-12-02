from cipher import *

def test_encrypt_basic():
    assert cipher("abc", 1) == "bcd"

def test_decrypt_basic():
    assert cipher("bcd", 1, "decrypt") == "abc"

def test_russian():
    assert cipher("абв", 1) == "бвг"

def test_punctuation():
    assert cipher("a,b.c!", 1) == "b,c.d!"
