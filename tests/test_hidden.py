from userinput import userinput


def test_hidden(monkeypatch):
    user_input = "yes"
    monkeypatch.setattr('getpass.getpass', lambda x: user_input)
    assert userinput("user_input", validator="human_bool", sanitizer="human_bool", cache=False, hidden=True)