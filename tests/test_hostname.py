from userinput import userinput
import pytest


def test_hostname(monkeypatch):
    user_input = "google.it"
    monkeypatch.setattr('builtins.input', lambda x: user_input)
    assert userinput("user_input", validator="hostname", cache=False)
