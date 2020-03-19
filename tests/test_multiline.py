from userinput import userinput
from userinput.test import simulate_multiline


def test_multiline(monkeypatch):
    multiline_str = ".. image:: https://api.codeclimate.com/v1/badges/a9b6fb01c314931fbfb6/maintainability\n   :target: https://codeclimate.com/github/LucaCappelletti94/correlation_reports/maintainability\n   :alt: Maintainability"
    monkeypatch.setattr('builtins.input', simulate_multiline(multiline_str))
    assert userinput("user_input", cache=False,
                     multi_line=True) == multiline_str
