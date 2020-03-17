from userinput import userinput
import pytest


def test_ip(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "127.0.0.1")
    assert userinput("user_input", validator="ip", cache=False)
    monkeypatch.setattr('builtins.input', lambda x: "")
    assert userinput("user_input", validator="ip", cache=False, maximum_attempts=3) is None
    monkeypatch.setattr('builtins.input', lambda x: "255.254.253.252")
    assert userinput("user_input", validator="ip", cache=False, maximum_attempts=3) is None
