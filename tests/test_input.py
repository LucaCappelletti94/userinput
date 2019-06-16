from userinput import userinput
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
    with pytest.raises(ValueError):
        userinput("url", default=url, validator="urls")