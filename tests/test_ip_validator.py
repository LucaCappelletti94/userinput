from userinput import userinput
import pytest


def test_ip(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "127.0.0.1")
    assert userinput("user_input", validator="ip", cache=False)
    monkeypatch.setattr('builtins.input', lambda x: "")
    with pytest.raises(ValueError):
        userinput("user_input", validator="ip", cache=False, maximum_attempts=3)
    monkeypatch.setattr('builtins.input', lambda x: "255.254.253.252")
    with pytest.raises(ValueError):
        userinput("user_input", validator="ip", cache=False, maximum_attempts=3)