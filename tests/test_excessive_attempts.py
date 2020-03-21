from userinput import userinput
import pytest

def test_excessive_attempts(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "\n")
    with pytest.raises(ValueError):
        while True:
            userinput("test_excessive_attempts", default="not_url", validator="url")
