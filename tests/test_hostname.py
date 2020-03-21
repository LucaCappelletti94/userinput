from userinput import userinput
import pytest


def test_hostname(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "localhost")
    assert userinput("user_input", validator="hostname", cache=False)
    monkeypatch.setattr('builtins.input', lambda x: "guguwgjwgdwkdjgwkjdgj")
    with pytest.raises(ValueError):
        userinput("user_input", validator="hostname", cache=False, maximum_attempts=3)