from userinput import userinput


def test_hidden(monkeypatch):
    user_input = "yes"
    monkeypatch.setattr('builtins.input', lambda x: user_input)
    assert userinput("user_input", validator="human_bool", sanitizer="human_bool", auto_clear=True)