from userinput import userinput
import pytest


def test_ip(monkeypatch):
    user_input = "127.0.0.1"
    monkeypatch.setattr('builtins.input', lambda x: user_input)
    assert userinput("user_input", validator="ip", cache=False)
