from cipher import *

def test_encrypt_decrypt_cycle():
    text = "Привет, World!"
    key = 7
    enc = cipher(text, key)
    dec = cipher(enc, key, "decrypt")
    assert dec == text
