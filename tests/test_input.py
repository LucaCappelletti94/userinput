from userinput import userinput, set_validator
import pytest


def test_input(monkeypatch):
    url = "http://google.com"
    monkeypatch.setattr('builtins.input', lambda x: url)
    assert url == userinput("url", validator="url")
    monkeypatch.setattr('builtins.input', lambda x: "3456789")
    assert userinput("url", validator="url", maximum_attempts=3) is None
    monkeypatch.setattr('builtins.input', lambda x: "")
    assert url == userinput("url", default=url, validator="url")
    assert url == userinput("url", default=url, validator=["url"])
    assert url == userinput("url", default=url, validator=lambda x: True)
    assert url == userinput("url", default=url, validator=[lambda x: True])
    assert url == userinput("url", default=url, validator=set_validator([
        url
    ]))
    assert userinput("url", default=url, maximum_attempts=3, validator=set_validator([
        "google.com"
    ])) is None
    with pytest.raises(ValueError):
        userinput("url", default=url, validator="urls")
    with pytest.raises(ValueError):
        userinput("url", default=url, validator="urlsqwertyuioplkjdswegwkuhdgqljhwdfg")
    with pytest.raises(ValueError):
        userinput("url", default=url, sanitizer="urls")
    with pytest.raises(ValueError):
        userinput("url", default=url, sanitizer="urlsqwertyuioplkjdswegwkuhdgqljhwdfg")
