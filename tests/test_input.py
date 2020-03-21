from userinput import userinput, set_validator
import pytest


def test_input(monkeypatch):
    url = "http://google.com"
    monkeypatch.setattr('builtins.input', lambda x: url)
    assert url == userinput("url", validator="url")
    monkeypatch.setattr('builtins.input', lambda x: "3456789")
    with pytest.raises(ValueError):
        userinput("url", validator="url", maximum_attempts=3)
    monkeypatch.setattr('builtins.input', lambda x: "")
    assert url == userinput("url", default=url, validator="url")
    assert url == userinput("url", default=url, validator=["url"])
    assert url == userinput("url", default=url, validator=lambda x: True)
    assert url == userinput("url", default=url, validator=[lambda x: True])
    assert url == userinput("url", default=url, validator=set_validator([
        url
    ]))
    with pytest.raises(ValueError):
        userinput("url", default=url, maximum_attempts=3, validator=set_validator([
            "google.com"
        ]))
    with pytest.raises(ValueError):
        userinput("url", default=url, validator="urls")
    with pytest.raises(ValueError):
        userinput("url", default=url, validator="urlsqwertyuioplkjdswegwkuhdgqljhwdfg")
    with pytest.raises(ValueError):
        userinput("url", default=url, sanitizer="human_boolss")
    with pytest.raises(ValueError):
        userinput("url", default=url, sanitizer="urlsqwertyuioplkjdswegwkuhdgqljhwdfg")
